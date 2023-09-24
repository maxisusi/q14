import requests
from bs4 import BeautifulSoup as bs
from lib import fill_array 
from ui import display_close, display_loading

def fetch_page(debug: bool): 
    end_point = 'https://accueil.emploilausanne.ch/menu-de-la-semaine/menu-de-la-semaine/'
    if debug:
        return bs(open('assets/index.html'), 'html.parser')
    else:
        display_loading()
        q14_page = requests.get(end_point)
        return bs(q14_page.content, 'html.parser')

def format_menu(soup: bs) -> dict[str, list[str]] | None :
    get_days = soup.select("div.accordeon-holder h3")
    get_plates = soup.select('div.plat-du-jour h4 + p')

    if(len(get_days) == 0 or len(get_plates) == 0):
        return None 
    else:
        days = []
        plates = []

        ## Fill up the days of the week
        for day in get_days:
            days.append(day.text.strip())
            
        ## Fill up the plates
        for idx, plate in enumerate(get_plates):
            temp_array = []

            fill_array(temp_array, plate)

            if idx % 2 == 0:
                plates.append(temp_array)
                fill_array(temp_array, get_plates[idx + 1])

        return dict(zip(days, plates))

