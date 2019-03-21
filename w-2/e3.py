# based on this : https://github.com/hacktiv8/phase-0-activities/blob/master/modules/anchor-menggunakan-if-else.md
# with some editing

name = ''
character = ''


def hero(name, character):
    if(name != '' and character != ''):
        print('Your name '+name+', Your caharacter '+character)
        return
    else:
        if(name == ''):
            name = input('Input your name: ')
        if(character == ''):
            character = input('Input your character: ')
        hero(name, character)
        return


hero(name, character)
