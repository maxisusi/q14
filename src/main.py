from parser import format_menu, fetch_page
from ui import display_menu, display_close
import click

@click.command()
@click.option('--debug','-d', is_flag=True, help='Display all the menus')
def main(debug):
    debug_mode = debug 
    soup = fetch_page(debug_mode)
    dict_plates = format_menu(soup)

    if dict_plates == None:
        display_close()
    else:
        display_menu(dict_plates)


if __name__ == "__main__":
    main()
