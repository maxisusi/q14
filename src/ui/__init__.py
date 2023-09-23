from termcolor import colored

from lib import cleanup_terminal

def display_menu(dict_plates: dict[str, list[str]]):
    cleanup_terminal()
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
    exit()

def display_close():
    cleanup_terminal()
    warning_text= colored("😎 Profitez du weekend, les plats arrivent!", 'red')
    print(warning_text)
    exit()

def display_loading():
    cleanup_terminal()
    print("🍽️ Menu de la semaine...")

