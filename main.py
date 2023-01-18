import json


with open('articles.json', 'r') as f:
    data = json.load(f)

run = True

while run:
    noun = input('Write your word here: ')

    for ending in data['rules']:
        if noun.endswith(ending):
            if data['rules'][ending] == 'mas':
                print(f'your noun appears to be masculine: Der {noun}')
            elif data['rules'][ending] == 'fem':
                print(f'your noun appears to be feminine: Die {noun}')
            elif data['rules'][ending] == 'neut':
                print(f'your noun appears to be neuter: Das {noun}')
                
        if noun == 'exit':
            print('bye :)')
            run = False


