from parser import format_menu, fetch_page
from ui import display_menu 

def main():
    debug_mode = True
    soup = fetch_page(debug_mode)
    dict_plates = format_menu(soup)
    display_menu(dict_plates)


if __name__ == "__main__":
    main()
