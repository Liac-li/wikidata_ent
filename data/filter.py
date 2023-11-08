import glob
import os

from tqdm import tqdm

def get_files() -> list:
    txt_file = glob.glob("*.txt")
    return txt_file

def prefix_filter(ents: list) -> list:
    filtered_ents = ents
    # remove all string in ents start with prefix
    prefixes = ["Category:"]
    for prefix in prefixes:
        filtered_ents = list(filter(lambda x: not x.startswith(prefix), filtered_ents))

    return filtered_ents

def keywords_filter(ents: list, keywords=None) -> list:
    keys = ['Provincial']
    if keywords is not None:
        keys = keywords
    
    filtered_ents = ents
    for keyword in keys:
        filtered_ents = list(filter(lambda x: keyword not in x, filtered_ents))
    return filtered_ents

if __name__ == "__main__":
    #TODO

    tgt_files = get_files()
    for tgt_file in tqdm(tgt_files):
        output_file = tgt_file.replace(".txt", ".filtered.txt")
        ent_type = tgt_file.split(".")[0]
        with open(tgt_file, "r", encoding='utf-8') as fr:
            lines = fr.readlines()
        
        ents = [line.replace("Category:", '').strip() + '\n' for line in lines]
        if ent_type == "STATE_OR_PROVINCE":
            ents = keywords_filter(ents, keywords=['Provincial'])

        with open(output_file, 'w', encoding='utf-8') as fw:
            fw.writelines(ents)
     