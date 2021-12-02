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

parser = argparse.ArgumentParser()
parser.add_argument("jokeID",type=str, nargs="?")
parser.add_argument("--category","-c",type=str, help= "categories possible")
parser.add_argument("--list-category","-l",action="store_true",help="Liste des category")
args = parser.parse_args()
#tableauCategorie = requests.get("https://api.chucknorris.io/jokes/categories")
#print(tableauCategorie.json())
print(args)
def chuck():
    if args.category is not None:
        data = requests.get(f"https://api.chucknorris.io/jokes/random?category={args.category}")
    #if args.list-category is not None:
    else:
        data = requests.get("https://api.chucknorris.io/jokes/random")
    tt = json.loads(data.text)
    print(tt["value"])

def chuckAvecJoke():
    
    data = requests.get(f"https://api.chucknorris.io/jokes/{args.jokeID}")
    tt = json.loads(data.text)
    print(tt["value"])

if args.jokeID is not None:
    chuckAvecJoke()
else:
    chuck()
