import json

import requests

URL = 'http://192.168.43.102:8080/api/ranking/'

AUTH = requests.auth.HTTPBasicAuth('debug', 'secret')

PLAYERS_COUNT = 4
new_statistics = {
    'ela': {
        'place': 1,
        'bomb_set': 10,
        'players_count': PLAYERS_COUNT,
        'kills': 2
    }
}

response = requests.post(URL, json=new_statistics, auth=AUTH)
if response.ok:
    print('statistics added for players: {}'.format(', '.join(new_statistics.keys())))
    print()

"""  
# Get all players
URL = 'http://localhost:8080/api/users/'

response = requests.get(URL)
if response.ok:
    all_players = json.loads(response.content.decode())
    # print(json.dumps(all_players, indent=4))
    # print()


# Add new player(s)
new_player = {
    'nickname': 'Alice',
    'email': 'alice@example.com',
    'password': 'secret',
}
# new_player put into list, because POST accepts list of players
response = requests.post(URL, json=[new_player])
if response.ok:
    print("player added: {}".format(new_player['nickname']))
    print()

new_two_players = [
    {
        'nickname': 'Bob',
        'email': 'bob@example.com',
        'password': 'secret',
    },
    {
        'nickname': 'Charlie',
        'email': 'charlie@example.com',
        'password': 'secret',
    }
]
response = requests.post(URL, json=new_two_players)
if response.ok:
    # print('players added: {}'.format(', '.join([p['nickname'] for p in new_two_players])))
    # print()


# Get specific player, identified by username/nickname
PLAYER = 'Alice'
response = requests.get(URL, params={'nickname': PLAYER})
# Alternatively, more REST-like style:
# response = requests.get(requests.compat.urljoin(URL, PLAYER))
if response.ok:
    player = json.loads(response.content.decode())
    # print(json.dumps(player, indent=4))
    # print()

"""
# Account activation (PATCH method) can be found in user_activation.py"""