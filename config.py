import re


DEBUG = False
POSTS_PER_GROUP = 10
URL = 'https://api.vk.com/method/'
ID = '204811373'
V = '5.102'
TITLE_FORMAT = re.compile(r'(\n|^)+(.)+\s+\(\d\d\d\d\)')
with open('TOKEN.txt') as f:
    TOKEN = f.readline().strip('\n')
GROUPS = [
    'kino_mania',
    'x.movie',
    'kinomania'
]
