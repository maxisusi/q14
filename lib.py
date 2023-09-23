import os

def cleanup_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def fill_array(temp_array, plate):
    if plate.text.strip() == '':
        temp_array.append(None)
    else:
        temp_array.append(plate.text.strip())
