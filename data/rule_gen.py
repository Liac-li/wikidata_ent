"""
    Generate entities dict data from data dir into 'entity-dict.json'
    {
        "PERSON": ["per-1", "per-2"],
        ...
    } 
"""

import json
import os
import random

from typing import List

# TODO

def gen_number_type_entities(n:int) -> List[str]:
    """
        generate entities for tacRED
    """
    def gen_num() -> str:
        num_type = random.choice(["digital", "str", "fraction", "float"])
        res = ""
        length = random.randint(0, 3)                  
        if num_type == 'digital':
            i = 0
            while i < length:
                res = "," + "".join([random.choice("0123456789") for j in range(3)]) + res
                i += 1
            res = "".join([random.choice("0123456789") for j in range(random.randint(1, 3))]) + res
            return res

        elif num_type == 'str':
            nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            one_nums = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
            two_nums = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
            l2names = {
                2: "hundred and ",
                3: "thousand ",
                4: "million ",
                5: "billion ",
            }  
            for i in range(length, 0, -1):
                if i > 1:
                    res += random.choice(nums) + " " + l2names[i]
                else:
                    tmp1 = random.choice(one_nums)
                    tmp2 = random.choice(two_nums) + " " +random.choice(nums)
                    res += random.choice([tmp1, tmp2])
                    break
            return res

        elif num_type == 'fraction':
            res = random.choice("0123456789") + '/' + random.choice("0123456789")
            return res

        elif num_type == 'float':
            res = random.choice("0123456789") + '.' + random.choice("0123456789")
            return res

    nums = [gen_num() for i in range(n)]
    return nums


def gen_url_type_entities(n):
        import string
        def generate_random_url():
            protocols = ["http", "https"]
            domains = [
                "Microsoft.NET",
                "www.adb.org",
                "wikipedia.org",
                "www.google.com",
                "www.hki.org",
                "www.usnow.org",
                "www.scienceblog.org"
            ]
            paths = ["/page", "/blog", "/product", "/psia", "/location"]
        
            protocol = random.choice(protocols)
            domain = random.choice(domains)
            path = random.choice(paths)
        
            # Generate a random query string with random parameters
            query_params = {
                "param1": ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10))),
                "param2": ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10)))
            }
        
            # Combine components to form the URL
            url = f"{protocol}://{domain}{path}?{'&'.join([f'{key}={value}' for key, value in query_params.items()])}"
        
            return url

        res = [generate_random_url() for i in range(n)]
        return res

if __name__ == '__main__':
    GEN_NUM = 5000 

    # gen_numbers
    numbers = gen_number_type_entities(10000)
    numbers = list(filter(lambda x: len(x) > 0, numbers))
    with open('data/NUMBER.filtered.txt', 'w') as fw:
        fw.write('\n'.join(numbers))
        
    urls = gen_url_type_entities(GEN_NUM)
    with open('data/URL.filtered.txt', 'w') as fw:
        fw.write('\n'.join(urls))
     
    