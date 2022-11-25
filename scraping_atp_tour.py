import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.atptour.com/en/rankings/singles?rankDate=2022-11-21&countryCode=all&rankRange=1-1400'
r = requests.get(url=url, headers={'User-Agent': ''})
soup = BeautifulSoup(r.content, 'html.parser')

stat_giocatori = []
players = soup.find_all('span', {'class': 'player-cell-wrapper'})
for p in players:
    nome = p.find('a').text.strip()
    l = p.find('a').get('href').strip()
    link_a = 'https://www.atptour.com' + l[:-8] + 'rankings-breakdown'
    link_b = 'https://www.atptour.com' + l[:-8] + 'player-stats'
    
    
    stat_giocatori.append({
        'giocatore': nome,
        'link_a': link_a,
        'link_b': link_b
    })
    
    

df_stat_p = pd.DataFrame(stat_giocatori)

df_stat_p.to_csv('link_giocatori.csv', index=False)