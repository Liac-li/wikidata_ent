import os
import json
import glob

from typing import List

def get_all_files(dir_path:str='.') -> List[str]:
    """
    Get all files in a directory
    """
    return glob.glob(os.path.join(dir_path, '*.txt'))

def load_data(file_path:str) -> dict[str, list]:
    with open(file_path, 'r') as fr:
        lines = fr.readlines()

    file_name = os.path.basename(file_path)
    ent_type = file_name.split('.')[0]
    lines = [line.strip().split('@@')[0] for line in lines]

    res = {}
    res[ent_type] = lines
    return res

if __name__ == "__main__":
    files = get_all_files('data')
    res = {}
    for file in files:
        ent_file = load_data(file)
        res.update(ent_file)

    ouput_file = os.path.join('data', 'entity-dict.json')
    with open(ouput_file, 'w') as fw:
        json.dump(res, fw, indent=4)
