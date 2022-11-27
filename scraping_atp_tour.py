import requests
from bs4 import BeautifulSoup
import pandas as pd

numero_giocatori = 2000
url = f'https://www.atptour.com/en/rankings/singles?rankDate=2022-11-21&countryCode=all&rankRange=1-{numero_giocatori}'
r = requests.get(url=url, headers={'User-Agent': ''})
soup = BeautifulSoup(r.content, 'html.parser')

g = []
players = soup.find_all('span', {'class': 'player-cell-wrapper'})
for p in players:
    nome = p.find('a').text.strip()
    l = p.find('a').get('href').strip()
    link = 'https://www.atptour.com' + l[:-8] + 'rankings-breakdown'
    
    g.append({
        'giocatore': nome,
        'link': link
    })

df = pd.DataFrame(g)
df.to_csv('link_giocatori.csv', index=False)