from config import *

import requests

from os import listdir, getcwd
from time import sleep


def main():
    auth()
    for result, group, r in search():
        if result is None:
            print('sorry')
        else:
            print('\n' + result)
            link = 'https://vk.com/' + group + '/' + str(r['date']) + '?w=wall' + str(r['owner_id']) + '_' + str(r['id'])
            print(link)


def auth():
    if 'TOKEN.txt' not in listdir(getcwd()):
        print('Program needs a special access token. Here are some instructions how to get it:')
        sleep(1)
        print("""
1. Go to https://oauth.vk.com/authorize?client_id=7175951&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=offline,wall&response_type=token&v=5.65
2. Click 'Allow' button
3. Now look at the address bar. Here you can find 'access_token='.
4. Copy that token.
5. Give it to the program.
""")
        with open('TOKEN.txt') as f:
            f.write(input('Paste your token here: '))


def search():
    method_name = 'wall.search' + '?'
    q = input('Type your search query: ')
    for group in GROUPS:
        r = requests.get('{}{}domain={}&query={}&count={}&owners_only=1&v={}&access_token={}'.format(URL, method_name, group, q, POSTS_PER_GROUP, V, TOKEN))

        if DEBUG:
            import json
            with open('data.json', 'w') as f:
                json.dump(r.json(), f, ensure_ascii=False, indent=2)

        for i in range(POSTS_PER_GROUP):
            try:
                title = TITLE_FORMAT.search(r.json()['response']['items'][i]['text'])
                if not (title is None):
                    yield title.group().strip('\n'), group, r.json()['response']['items'][i]
            except IndexError:
                break

    return None, None, None


if __name__ == '__main__':
    main()
