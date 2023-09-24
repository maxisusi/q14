from parser import format_menu, fetch_page
from ui import display_menu, display_close
import click

@click.command()
@click.option('--debug','-d', is_flag=True, help='Display all the menus')
def main(debug):
    debug_mode = debug 
    soup = fetch_page(debug_mode)
    get_menus = format_menu(soup)

    if get_menus == None:
        display_close()
    else:
        display_menu(get_menus)


if __name__ == "__main__":
    main()
