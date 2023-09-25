from termcolor import colored
import click
from lib import cleanup_terminal

def display_menu(dict_plates: dict[str, list[str]]):
    click.clear()
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
    click.clear()
    warning_text= colored("😎 Il faut être patient, les plats arrivent!", 'red')
    click.echo(warning_text)

def display_loading():
    click.clear()
    click.echo("🍽️ Menu de la semaine...")

