import requests

url = 'https://superheroapi.com/api/2619421814940190/search/'
superheroes = [{'name' : 'Hulk'}, {'name' : 'Captain America'}, {'name' : 'Thanos'}]

for hero in superheroes:
  sup_hero = requests.get(url + hero['name'])
  hero['intelligence'] = int(sup_hero.json()['results'][0]['powerstats']['intelligence'])
    
print(sorted(superheroes, key=lambda hero: -hero['intelligence'])[0]['name'])