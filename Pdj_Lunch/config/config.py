import json

def config(value):
    with open(fr"./json/data.json", 'r', encoding='utf-8 sig') as file:
        data = json.load(file)
        
        ### SCHOOL INFO ###
        School_Name = data['School_Info']['name']
        School_AE = data['School_Info']['AE']
        School_SE = data['School_Info']['SE']

        ### API KEY ###
        API_KEY = data['School_Info']['KEY']
        
        ### INSTAGRAM ACCOUNT ###
        Instagram_ID = data['Instagram_Account']['ID']
        Instagram_PW = data['Instagram_Account']['PW']


        if value == "School_Name":
            return School_Name
        elif value == "School_AE":
            return School_AE
        elif value == "School_SE":
            return School_SE
        
        elif value == "API_KEY":
            return API_KEY
        
        elif value == "Instagram_ID":
            return Instagram_ID
        elif value == "Instagram_PW":
            return Instagram_PW