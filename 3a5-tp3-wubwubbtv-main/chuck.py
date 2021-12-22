###############################################################################
#  Cours:        420-3A5-EM
#  Session:      Automne 2021
#  Nom:          Gendron-Larsen Louis
#  Groupe:       1020
#  Description:  Travail pratique #3
###############################################################################
#TODO: Écrivez votre script ici.
#Import requests install  :
#### python -m pip install requests

import requests, json, sys, argparse

from requests.models import HTTPError

parser = argparse.ArgumentParser()
parser.add_argument("jokeID",type=str, nargs="?")
parser.add_argument("--category","-c",type=str, help= "catégories disponibles")
parser.add_argument("--list-category","-l",action="store_true",help="Liste des catégories disponibles")
parser.add_argument("--search","-s",type=str, help= "on cherche des blagues contenant le mot passé en argument")
args = parser.parse_args()
tableauCategorie = requests.get("https://api.chucknorris.io/jokes/categories")
listtableuacategorie = tableauCategorie.json()

def chuck():

    if args.category is not None:
        data = requests.get(f"https://api.chucknorris.io/jokes/random?category={args.category}")
        tt = json.loads(data.text)
        print(tt["value"],str("["+tt["id"]+"]"))
    
    elif args.list_category:
        print("Catégories disponibles:")
        for i in range(len(listtableuacategorie)):
            print("- " + listtableuacategorie[i])
    
    elif args.search is not None:
        data = requests.get(f"https://api.chucknorris.io/jokes/search?query={args.search}")
        tt =  json.loads(data.text)
        print(str(tt["total"]) + " résultats: ")
        for i in range(len(tt)):
            print("- ",tt["result"][i]["value"],str("["+tt["result"][i]["id"]+"]"))


            
    else:
        data = requests.get("https://api.chucknorris.io/jokes/random")
        tt = json.loads(data.text)
        print(tt["value"],str("["+tt["id"]+"]"))

    

def chuckAvecJoke():
    
    data = requests.get(f"https://api.chucknorris.io/jokes/{args.jokeID}")
    tt = json.loads(data.text)
    print(tt["value"])
try:
    if args.jokeID is not None:
        chuckAvecJoke()
    else:
        chuck()
except HTTPError as e:
    print("e")

