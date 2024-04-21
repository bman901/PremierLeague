import urllib.request
import json

infile = urllib.request.urlopen('https://raw.githubusercontent.com/openfootball/football.json/master/2015-16/en.1.clubs.json')
html_page = infile.read().decode()
content_as_python_object = json.loads(html_page)

clubs = content_as_python_object['clubs']

clublist = []
Sclublist = []

for element in clubs:
    clublist.append(element['name'])
    clublist.sort()

print(clublist)

for element in clubs:
    if element['name'][0] == 'S':
        Sclublist.append(element['name'])
    Sclublist.sort()

print(Sclublist)