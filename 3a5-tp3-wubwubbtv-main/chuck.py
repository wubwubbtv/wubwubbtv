###############################################################################
#  Cours:        420-3A5-EM
#  Session:      Automne 2021
#  Nom:          Gendron-Larsen Louis
#  Groupe:       1020
#  Description:  Travail pratique #3
###############################################################################
#TODO: Écrivez votre script ici.


import requests
import json


def chuck(Jokeid = 0):
        
    data = requests.get("https://api.chucknorris.io/jokes/random")
    tt = json.loads(data.text)
    print(tt["value"])

chuck()

