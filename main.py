import json
from string import *

def load_data():
    result = "data.json".rsplit(".", 1)
    print(result[0], "is a", result[1], "file.")
    with open('data.json') as file:
        data = json.load(file)
    return data

def get_character(*args):
    data = load_data()
    cname = args[0]
    if 'characters' in data.keys() and cname in data['characters']:
        return data['characters'][cname]
    else:
        return None
    
def write_character(*args):
    cname = args[0]
    for i in punctuation:
        if i in cname:
            print('invalid character name')

def get_spell(*args):
    data = load_data()
    spell = args[0]
    if 'spells' in data.keys() and spell in data['spells']:
        return data['spells'][spell]
    else:
        return None

def get_house(*args):
    data = load_data()
    hn = args[0]
    if 'houses' in data.keys() and hn in data['houses']:
        return data['houses'][hn]
    else:
        return None

def append_to(element, to=[]):
     # this is not used
    to.append(element)
    return to

def search_spells_by_name(*args):
    data = load_data()
    n = args[0]
    spells = []
    for spell, info in data['spells'].items():
        if info['name'] == n or info['name'].startswith('n') or info['name'].endswith(n) or n in info['name']:
            spells.append(spell)
    return spells

def suggest_a_house_for_student(traits_preferences):
    # this is not in the command line yet
    # but feel free to comment on it

    if not traits_preferences:
        return None 
    house = None 
    # Some complex code to find a house
    # house = do_search(traits_preferences)
    if not house:
        # Some Plan-B to find another house
        house = 2 # do_another_search(traits_preferences)
    return house 



if __name__ == '__main__':
    while True:
        print("\n--- Harry Potter Command-Line Application ---")
        print("1. Get character information")
        print("2. Get spell information")
        print("3. Get house information")
        print("4. Search spells by name")
        print("5. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter the character name: ")
            character = get_character(name)
            if character:
                print("\nCharacter: ", character['name'])
                print("House: ", character['house'])
                print("Role: ", character['role'])
            else:
                print("Character not found.")
        
        elif choice == '2':
            name = input("Enter the spell name: ")
            spell = get_spell(name)
            if spell:
                print("\nSpell: ", spell['name'])
                print("Type: ", spell['type'])
                print("Effect: ", spell['effect'])
            else:
                print("Spell not found.")
        
        elif choice == '3':
            name = input("Enter the house name: ")
            house = get_house(name)
            if house:
                print("\nHouse: ", house['name'])
                print("Founder: ", house['founder'])
                print("Traits: ", house['traits'])
            else:
                print("House not found.")
        elif choice == '4':
            name = input("Enter name: ")
            spells = search_spells_by_name(name)
            print(f"\nSpells of text {name}:")
            tmp = ''
            for i in range(len(spells)):                
                tmp += " " + spells[i]
            spells = tmp
            print(spells)
        elif choice == '5':
            print("Exiting the application...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
