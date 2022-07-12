import JSON
import request as rq
import flask

url = "https://api.atlasacademy.io/export/NA/basic_servant.json"
servantInfo = url.json()

#using this function to get all the JSON data of each servant from the API

def get_NAservants():
    
    for servants in servantInfo:
        print(servantInfo['name']
        print(servantInfo['class']
        print(servantInfo['rarity']
        print(servantInfo['atkMax']
        print(servantInfo['hpMax']
       # print(servantInfo['face']


