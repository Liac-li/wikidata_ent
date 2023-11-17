import json


if __name__ == "__main__":
    tgt_file = 'origin/test.json'
    with open(tgt_file, 'r') as fr:
        data = json.load(fr)

    for i in range(len(data)):
        item = data[i]
        sub_s, sub_e = item.get('subj_start'), item.get('subj_end')
        obj_s, obj_e = item.get('obj_start'), item.get('obj_end')
        
        item['stanford_ner'][sub_s:sub_e] = [item['subj_type'] for i in range(sub_e - sub_s + 1)]
        item['stanford_ner'][obj_s:obj_e] = [item['obj_type'] for i in range(obj_e - obj_s + 1)]

    tgt_type = {
        "NUMBER": [], 
        "URL": [],
    }
    for item in data:
        tokens = item.get('token')
        ner_t = item.get('stanford_ner')
        
        is_start = False
        last_type = ''
        token_cache = []
        for idx, token in enumerate(tokens):
            if ner_t[idx] in tgt_type:
                if not is_start:
                    is_start = True
                    last_type = ner_t[idx]
                    token_cache.append(token)
                elif last_type != ner_t[idx]:
                    if last_type in tgt_type:
                        tgt_type[last_type].append(' '.join(token_cache))
                    token_cache = [token]
                    last_type = ner_t[idx]
                else:
                    token_cache.append(token)
            else:
                if is_start and last_type in tgt_type:
                    tgt_type[last_type].append(" ".join(token_cache))
                    token_cache = []
                    is_start = False
                    last_type = ''
                
        if is_start and last_type in tgt_type:
            tgt_type[last_type].append(" ".join(token_cache))

    with open('output.json', 'w')  as fw:
        json.dump(tgt_type, fw, indent=4)