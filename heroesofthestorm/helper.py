import os
import csv
import time
import random

role_dict = {
    't':'Tank',
    'b':'Bruiser',
    'h':'Healer',
    's':'Support',
    'r':'Ranged Assassin',
    'm':'Melee Assassin'}

franchise_dict = {
    'w':'World of Warcraft',
    's':'Starcraft',
    'd':'Diablo',
    'o':'Overwatch',
    'v':'The Lost Vikings',
    'h':'Heroes of the Storm'}

help_msg = '''
Hero Picker will help you select a hero, with some optional filters!

Hero Manager doesnt exist yet because im still learning about databases.
'''

with open('heroes.csv') as heroes_file:
    heroes_csv = csv.DictReader(heroes_file)
    heroes_data_dict = {}
    for row in heroes_csv:
        heroes_data_dict[row['name']] = row

#for hero in heroes_data_dict:
    #print(hero + " " + str(heroes_data_dict[hero]) + "\n")

class Hero:

    def __init__(self, name, role, franchise, level):
        self.name = name
        self.role = role
        self.franchise = franchise
        self.level = int(level)

    def __repr__(self):
        return "{0} is a level {1} {2} from the {3} universe.".format(self.name, self.level, role_dict[self.role].lower(), franchise_dict[self.franchise])

    def levelup(self):
        self.level += 1
        print("{0} leveled up to level {1}.".format(self.name, self.level))

    def leveldown(self):
        self.level -= 1
        print("{0} moved back to level {1}.".format(self.name, self.level))
            
heroes_dict = {}
for hero in heroes_data_dict:
    name = heroes_data_dict[hero]['name'] 
    role = heroes_data_dict[hero]['role']
    franchise = heroes_data_dict[hero]['franchise']
    level = heroes_data_dict[hero]['level']
    heroes_dict[hero] = Hero(name, role, franchise, level)

clear = lambda: os.system('cls')

def choice_list(choices, last=None):
    if len(choices) < 9:
        number = 1
        for choice in choices:
            print('[{0}] - {1}'.format(number, choice))
            number += 1
        if last != None:
            print('[{0}] - {1}'.format(number, last))

    else:
        print('Too long!')

def picker(filters):
   
    heroes_list1 = []
    for value in heroes_dict.values():
        heroes_list1.append(value)

    # role filter
    heroes_list2 = []
    if filters[0] != 'n':
        for hero in heroes_list1:
            if hero.role == filters[0]:
                heroes_list2.append(hero)
    else:
        heroes_list2 = heroes_list1

    # franchise filter
    heroes_list3 = []
    if filters[1] != 'n':
        for hero in heroes_list2:
            if hero.franchise == filters[1]:
                heroes_list3.append(hero)
    else:
        heroes_list3 = heroes_list2

    # level filter
    heroes_list4 = []
    if filters[2] == 1:
        for hero in heroes_list3:
            if hero.level == 1:
                heroes_list4.append(hero)
        
    elif filters[2] == 21:
        for hero in heroes_list3:
            if hero.level > 20:
                heroes_list4.append(hero)

    elif filters[2] == 0:
        heroes_list4 = heroes_list3

    else:
        for hero in heroes_list3:
            if hero.level < filters[2]:
                heroes_list4.append(hero)               

    if heroes_list4 == []:
        return False

    else:
        return random.choice(heroes_list4)


play = 1
menu_code = 1
filters = 'Filters Active - '
filter_list = []
while play == 1:

    while menu_code == 1:

        # main menu
        clear()
        time.sleep(.25)
        print('Welcome to Heroes Helper!\n\n')
        choice_list(['Hero Picker', 'Hero Manager', 'Help', 'Exit'])
        user = input('---{ ')

        if user == '1':
            menu_code = 7

        if user == '2':
            pass

        if user == '3':
            menu_code = 2

        if user == '4':
            play = 0
            menu_code = 0

    # help menu
    while menu_code == 2:
        clear()     
        print(help_msg)
        choice_list(['Back'])
        user = input('---{ ')

        if user == '1':
            menu_code = 1  

    # Hero Picker role filter
    while menu_code == 3:
        clear()
        print('Welcome to the Hero Picker!\n')
        print(filters)
        choice_list(role_dict.values(), 'No Filter')
        user = input('---{ ')

        if user == '7':
            menu_code = 4
            filter_list.append('n')

        if user == '1':
            filters += 'Role: Tank'
            filter_list.append('t')
            
        if user == '2':
            filters += 'Role: Bruiser'
            filter_list.append('b')

        if user == '3':
            filters += 'Role: Healer'
            filter_list.append('h')

        if user == '4':
            filters += 'Role: Support'
            filter_list.append('s')

        if user == '5':
            filters += 'Role: Ranged Assassin'
            filter_list.append('r')

        if user == '6':
            filters += 'Role: Melee Assassin'
            filter_list.append('m')

        menu_code = 4

    # Hero Picker franchise filter
    while menu_code == 4:
        clear()
        print('Welcome to the Hero Picker!\n')
        print(filters)
        choice_list(franchise_dict.values(), 'No Filter')
        user = input('---{ ')

        if user == '7':
            menu_code = 5
            filter_list.append('n')

        if len(filters) > 17:
            filters += ', '

        if user == '1':
            filters += 'Franchise: World of Warcraft'
            filter_list.append('w')
            
        if user == '2':
            filters += 'Franchise: Starcraft'
            filter_list.append('s')

        if user == '3':
            filters += 'Franchise: Diablo'
            filter_list.append('d')

        if user == '4':
            filters += 'Franchise: Overwatch'
            filter_list.append('o')

        if user == '5':
            filters += 'Franchise: The Lost Vikings'
            filter_list.append('v')

        if user == '6':
            filters += 'Franchise: Heroes of the Storm'
            filter_list.append('h')

        menu_code = 5

    # Hero Picker level filter
    while menu_code == 5:
        clear()
        print('Welcome to the Hero Picker!\n')
        print(filters)
        choice_list(['Level 1', '< Level 5', "< Level 10", "< Level 15", '< Level 20', '> Level 20'], 'No Filter')
        user = input('---{ ')

        if user == '7':
            menu_code = 6
            filter_list.append(0)

        if len(filters) > 17:
            filters += ', '        

        if user == '1':
            filters += 'Level: 1'
            filter_list.append(1)
            
        if user == '2':
            filters += 'Level: < 5'
            filter_list.append(5)

        if user == '3':
            filters += 'Level: < 10'
            filter_list.append(10)

        if user == '4':
            filters += 'Level: < 15'
            filter_list.append(15)

        if user == '5':
            filters += 'Level: < 20'
            filter_list.append(20)

        if user == '6':
            filters += 'Level: > 20'
            filter_list.append(21)

        menu_code = 6

    # Hero Picker 
    while menu_code == 6:
        clear()
        print('Welcome to the Hero Picker!\n')
        print(filters + "\n")
        pick = picker(filter_list)

        if pick == False:
            print('No matches for that filter!\n')
        else:
            print('Your selection is: {0}'.format(pick.name))
            print('{0}\n'.format(pick))


        choice_list(['Start over', 'Quit'])
        user = input('---{ ')

        if user == '1':
            filters = 'Filters Active - '
            filter_list = []
            menu_code = 7

        if user == '2':
            filters = 'Filters Active - '
            filter_list = []
            menu_code = 1

    while menu_code == 7:
        clear()
        print('Welcome to the Hero Picker!\n')
        choice_list(['Custom Filters', 'Level 1'])
        user = input('---{ ')

        if user == '1':
            menu_code = 3

        if user == '2':
            filters = 'Filters Active - Level 1'
            filter_list = ['n', 'n', 1]
            menu_code = 6