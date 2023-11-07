class Config:
    FILE_PATH = '/home/leelin/Downloads/enwiki-latest-pages-articles.xml.bz2'
    save_path = 'data'
    tgt_types = {
        "MISC": False, # need to add rules
        "CAUSE_OF_DEATH": False, 
        "CRIMINAL_CHARGE": False,

        "LOCATION": True,
        "TITLE": True,
        "NATIONALITY": False, # use nationality list not wikidata
        "NUMBER": False,  # use rule generated
        "COUNTRY": True,
        "IDEOLOGY": True,
        "CITY": True,
        "ORGANIZATION": True,
        "DATE": False, # use rule generated
        "RELIGION": True,
        "STATE_OR_PROVINCE": True,

        "URL": False, # need to add rules
        "DURATION": False,
        "PERSON": True,
    }

    type2pattern = {
        "MISC": [],
        "CAUSE_OF_DEATH": [],
        "CRIMINAL_CHARGE": [],
        "LOCATION": ["Locations"],
        "TITLE": ["Titles\]", "Titles in "],
        "NATIONALITY": ["Nationality"],
        "NUMBER": ["Numbers"],
        "COUNTRY": ["Countries"],
        "IDEOLOGY": ["Ideology", "Ideologies"],
        "CITY": ["City-states", "City of"],
        "ORGANIZATION": ["Organizations"],
        "DATE": [],
        "RELIGION": ["Religion in"],
        "STATE_OR_PROVINCE": ["States of", "Provinc"],
        "URL": [],
        "DURATION": [],
        "PERSON": ["Persons", "Living_people"],
    }

    tacRED_types = [
        'MISC', 'CAUSE_OF_DEATH', 'CRIMINAL_CHARGE', 'LOCATION', 'TITLE',
        'NATIONALITY', 'NUMBER', 'COUNTRY', 'IDEOLOGY', 'CITY', 'ORGANIZATION',
        'DATE', 'RELIGION', 'STATE_OR_PROVINCE', 'URL', 'DURATION', 'PERSON'
    ]
