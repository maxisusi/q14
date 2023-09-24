from termcolor import colored
import click
from lib import cleanup_terminal

def display_menu(dict_plates: dict[str, list[str]]):
    cleanup_terminal()
    for key, value in dict_plates.items():
        click.echo(f"☀️  {key}")
        click.echo("")
        if value[0] == None:
            close = colored("Restaurant fermé", 'grey')
            click.echo(close)
        else: 
            meat = colored(value[0], 'blue')
            veggie = colored(value[1], 'green')
            click.echo(f"🥩: {meat}")
            click.echo(f"🥬: {veggie}")
        click.echo("-------------------------")

def display_close():
    cleanup_terminal()
    warning_text= colored("😎 Profitez du weekend, les plats arrivent!", 'red')
    click.echo(warning_text)

def display_loading():
    cleanup_terminal()
    click.echo("🍽️ Menu de la semaine...")

