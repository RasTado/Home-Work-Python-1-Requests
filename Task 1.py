import requests
name_list = ['Hulk', 'Captain America', 'Thanos']
token = 2619421814940190

def hero_request(token, names):
    for name in name_list:
        url = f'https://superheroapi.com/api/{token}/search/{name}'
        req = requests.get(url).json()['results']
        # print(req)
        heroes = {}
        for id_ in req:
            if id_['name'] == name:
                url_id = f'''https://superheroapi.com/api/{token}/{id_['id']}/powerstats'''
                req_int = requests.get(url_id).json()
                heroes[int(req_int['intelligence'])] = req_int['name']
    print(f'Самый умный супергерой это {heroes[max(heroes.keys())]} с интелектом {max(heroes.keys())}')

if __name__ == '__main__':
    hero_request(token, name_list)
