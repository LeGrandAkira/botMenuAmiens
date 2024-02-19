import requests
from bs4 import BeautifulSoup

def menu():
    url = "https://quejd.fr/menu/menu.php"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        section_tag = soup.find('section', id='section')

        if section_tag:
            cleaned_text = ""
            
            for item in section_tag.children:
                if item and item.string:
                    cleaned_text += item.string.strip() + "\n"  
            
        else:
            print("Balise <section> introuvable sur la page.")
    else:
        print("La requête a échoué avec le code :", response.status_code)

    return cleaned_text.strip()

def menuToDict(menu):
    menu = menu.split("__________")
    entree = menu[0].replace("\n"," | ")[:-2]
    plat = menu[1].replace("\n"," | ")[:-2][3:].split("+")
    condiment = plat[1][3:]
    plat = plat[0][:-2]
    dessert = menu[3].replace("\n", " | ")[3:]
    menuDict = {"entree" : entree, "plat" : plat, "condiment" : condiment, "dessert" : dessert}

    return (menuDict)
