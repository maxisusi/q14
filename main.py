import requests
from bs4 import BeautifulSoup as bs
from termcolor import colored
import os


end_point = 'https://accueil.emploilausanne.ch/menu-de-la-semaine/menu-de-la-semaine/'

## display loading
print("🍽️ Menu de la semaine...")
q14_page = requests.get(end_point)

## parse datas
soup = bs(q14_page.content, 'html.parser')

## Get Day
get_days = soup.select("div.accordeon-holder h3")

## Check if the restaurant is open
if len(get_days) == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    warning_text= colored("😎 Profitez du weekend, les plats arrivent!", 'red')
    print(warning_text)
    exit()
    
## Get the "plat du jour selector"
get_plates = soup.select('div.plat-du-jour h4 + p')

## format days 
list_day = []
list_plates = []

for day in get_days:
    list_day.append(day.text.strip())
    

def fill_array(temp_array, plate):
    if plate.text.strip() == '':
        temp_array.append(None)
    else:
        temp_array.append(plate.text.strip())



for idx, plate in enumerate(get_plates):
    temp_array = []

    fill_array(temp_array, plate)
    # Push it to the list when done
    if idx % 2 == 0:
        list_plates.append(temp_array)
        fill_array(temp_array, get_plates[idx + 1])

## create a dictionnary to stope dates and plates
dict_plates = dict(zip(list_day, list_plates))

os.system('cls' if os.name == 'nt' else 'clear')
## display beautifuly in ascii style like a restaurant the meat menus and the veggie menus for the week
for key, value in dict_plates.items():
    print(f"☀️  {key}")
    print("")
    if value[0] == None:
        close = colored("Restaurant fermé", 'grey')
        print(close)
    else: 
        meat = colored(value[0], 'blue')
        veggie = colored(value[1], 'green')
        print(f"🥩: {meat}")
        print(f"🥬: {veggie}")
    print("-------------------------")














