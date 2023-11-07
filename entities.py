import os
import glob
import random
import re

class Wiki_Entities:
    def __init__(self):
        self.data_dir = 'data'
        self.saved_files = self._get_saved_ents_list(self.data_dir)

        # prepare for saved ents

    @staticmethod
    def _get_saved_ents_list(data_dir:str) -> dict:
        ent_type2file = {}
        txt_files = glob.glob(f"{data_dir}/*.txt")
        for ent_file in txt_files:
            ent_type = ent_file.replace('.txt', '')
            ent_type2file[ent_type] = ent_file
        
        return ent_type2file
    
    def _get_ents(file_path:str) -> list:
        clean_name = lambda x: re.sub(r'\([^)]*\)', '', x)

        with open(file_path, 'r', encoding='utf-8') as fr:
            lines = fr.readlines()

        ents = [ent.split('@@@')[0] for ent in lines]
        clean_ents = [clean_name(ent) for ent in ents]
        random.shuffle(clean_ents)
        return clean_ents
    
    # TODO