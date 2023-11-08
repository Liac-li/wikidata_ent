import os
import glob
import random
import re

class Wiki_Entities:
    def __init__(self, policy='uniform'):
        self.data_dir = 'data'
        self.saved_files = self._get_saved_ents_list(self.data_dir)

        # prepare for saved ents
        self.policy = policy

    @staticmethod
    def _get_saved_ents_list(data_dir:str) -> dict:
        suffix = '.filtered.txt'
        ent_type2file = {}
        txt_files = glob.glob(f"{data_dir}/*{suffix}")
        for ent_file in txt_files:
            ent_type = ent_file.replace(suffix, '')
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
    
    def _ent_filter(ents: list) -> list:
        #TODO: add ent filter rules
        pass
    
    def get_ents_with_type(self, ent_type:str) -> list:
        if ent_type not in self.saved_files:
            raise ValueError(f"{ent_type} not found in saved entities")
            # return None
        
        ent_file = self.saved_files[ent_type]
        ents = self._get_ents(ent_file)

        if self.policy == 'uniform':
            return ents 
    

class EntGenByRules:
    def __init__(self) -> None:
        self.ent_types = [
            "URL", "DATE", "DURATION"
        ]
    
    @staticmethod
    def _gen_urls():
        return NotImplementedError
    