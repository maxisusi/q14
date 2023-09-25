import requests 
from bs4 import BeautifulSoup as bs
from lib import fill_array
from parser.constants import END_POINT
from ui import display_loading

def fetch_page(debug: bool): 
    if debug:
        return bs(open('assets/index.html'), 'html.parser')
    else:
        display_loading()
        q14_page = requests.get(END_POINT)
        return bs(q14_page.content, 'html.parser')

def format_menu(soup: bs) -> dict[str, list[str]] | None :
    days_list = soup.select("div.accordeon-holder h3")
    plates_list = soup.select('div.plat-du-jour h4 + p')

    if(len(days_list) == 0 or len(plates_list) == 0):
        return None 
    else:
        days = []
        plates = []

        ## Fill up the days of the week
        for day in days_list:
            days.append(day.text.strip())
            
        ## Fill up the plates
        for idx, plate in enumerate(plates_list):
            temp_array = []

            fill_array(temp_array, plate)

            if idx % 2 == 0:
                plates.append(temp_array)
                fill_array(temp_array, plates_list[idx + 1])


        return dict(zip(days, plates))

