import bz2
import re
from tqdm import tqdm
import os
import threading

from config import Config as config

def wikipage_iter(config):
    wikidata_file = config.FILE_PATH

    with bz2.open(wikidata_file, 'rt', encoding='utf-8') as fin:
        for i, line in enumerate(fin):
            yield line


def check_ent(page_lines: list, ent_type: list) -> bool:
    # print(ent_type)
    # for line in page_lines:
    #     matches = [re.search(r'\[\[Category:{}'.format(ent_t), line) for ent_t in ent_type]
    #     print(matches)
    #     if any(matches):
    #         return True
    page_content = ''.join(page_lines)
    matches = [
        re.search(r'\[\[Category:{}'.format(ent_t), page_content) is not None
        for ent_t in ent_type
    ]
    # print(matches)
    if any(matches):
        return True

    return False

def clean_name(input_string):
    return re.sub(r'\([^)]*\)', '', input_string)

def save_res(res: list, output_file: str):
    if not res:
        return

    print(res[0])
    with open(output_file, 'a') as fa:
        fa.writelines(res)


def extract_ent(config, ent_t: str, patterns: list):
    # wikidata_file = config.FILE_PATH

    r_page_begin = r"<page>"
    r_page_end = r"</page>"
    r_title = r"<title>(.*?)</title>"
    save_file = os.path.join(config.save_path, '{}.txt'.format(ent_t))

    in_page = False
    page_lines = []
    ent_name = ''
    res = []
    for line in tqdm(wikipage_iter(config)):
        if re.search(r_page_begin, line):
            in_page = True
        elif re.search(r_page_end, line):
            in_page = False
            if check_ent(page_lines, patterns):
                res.append("{}@@@{}\n".format(clean_name(ent_name), ent_t))
                if len(res) >= 20:
                    save_res(res, save_file)
                    res = []
            page_lines = []

        if not in_page:
            continue

        ent_match = re.search(r_title, line)
        ent_name = ent_match.group(1) if ent_match else ent_name
        page_lines.append(line)

    save_res(res, save_file)


def main(config):
    # out_dir = config.save_path
    tgt_types = config.tgt_types
    tgt_types = [k for k, v in tgt_types.items() if v]
    type2pattern = config.type2pattern

    threads = []
    for ent_t in tgt_types:
        thread = threading.Thread(target=extract_ent,
                                  args=(config, ent_t,
                                        type2pattern.get(ent_t)))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Over")


if __name__ == "__main__":
    main(config)
