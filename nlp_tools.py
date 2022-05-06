
import re
from unidecode import unidecode
import pickle


def tokennize(texte):
    texte = texte.lower()
    p = "([a-zéèàùîêâûôçïëœ]{1,})"
    texte = ' '.join(re.findall(p, texte))
    # Je renvoi une liste de token
    return texte.split()


with open('lemmatize_fr.pickle', 'rb',) as f:
    dico = pickle.load(f)


def lemmitize(tokens):
    final = []
    for token in tokens:
        try:
            final.append(dico[token])
        except:
            final.append(token)
    return final



## List Cleaner
with open('stop-w_fr.txt', "r") as f:
    stop = f.read().split('\n')


remove_list = ['haut', 'pas', 'ne', 'n', 'ni', 'peu', 'bon', 'très', 'tres', 'même', 'fait', 'début',
               'mais', 'dès', 'premier', 'première', 'plus', 'aussi', 'bien', 'assez', 'retour', 'tout', 'rien']
for element in remove_list:
    try:
        stop.remove(element)
    except Exception as e:
        print(e)


def stopword(liste_token):
    final = []
    for token in liste_token:
        if unidecode(token) in stop:
            continue
        final.append(unidecode(token))
    return final


def cleaner(texte):
    return ' '.join(stopword(lemmitize(tokennize(texte))))
