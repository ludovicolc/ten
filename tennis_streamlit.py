import pandas as pd
import joblib
import streamlit as st
from bs4 import BeautifulSoup
import requests

giocatori = pd.read_csv('link_giocatori.csv')

europa =  ['ESP', 'FRA', 'GER', 'RUS', 'ITA', 'AUS', 'CZE', 'CRO',
       'SRB', 'SUI', 'GBR', 'BEL', 'AUT', 'SVK', 'NED', 'SWE', 'ROU',
       'FIN', 'POR', 'POL', 'BUL', 'CYP', 'BLR', 'UKR', 'SLO', 'LAT', 'NOR',  'BIH', 'GRE',
       'GEO', 'LUX', 'DEN', 'HUN', 'LTU', 'MDA', 'EST', 'IRL', 'BAR', 'ESA']
sud_america= ['ARG', 'BRA', 'COL', 'URU', 'ECU', 'PER', 'CHI', 'BOL', 'MEX', 'PAR']
nord_america= ['USA', 'CAN']
africa = ['RSA', 'TUN', 'MAR', 'TUR', 'EGY', 'ALG', 'ZIM']
asia = ['JPN', 'KAZ', 'UZB', 'ISR', 'IND', 'THA', 'KOR', 'ARM', 'CHN', 'TPE', 'PHI', 'MON', 'PAK']
oceania = ['NZL']

prev = st.container()

sc = joblib.load('standard_scaler_joblib')
vc = joblib.load('tennis_clf_joblib')

def dati(A_B365, A_Pts, A_Rank, B_B365, B_Pts, B_Rank,
       Date, A_dob, A_height, B_dob, B_height,
       Location_asia=0, Location_europa=0, Location_nord_america=0,
       Location_oceania=0, Location_sud_america=0, Round_2nd_Round=0,
       Round_3rd_Round=0, Round_4th_Round=0, Round_Quarterfinals=0,
       Round_Round_Robin=0, Round_Semifinals=0, Round_The_Final=0,
       A_hand_R=0, A_ioc_asia=0, A_ioc_europa=0, A_ioc_nord_america=0,
       A_ioc_oceania=0, A_ioc_sud_america=0, B_hand_R=0, B_ioc_asia=0,
       B_ioc_europa=0, B_ioc_nord_america=0, B_ioc_oceania=0,
       B_ioc_sud_america=0):
    
    d = []
    d.append({
        'A_B365': A_B365,
        'A_Pts': A_Pts,
        'A_Rank': A_Rank,
        'B_B365': B_B365,
        'B_Pts': B_Pts,
        'B_Rank': B_Rank,
        'Date': Date,
        'A_dob': A_dob,
        'A_height': A_height,
        'B_dob': B_dob,
        'B_height': B_height,
        'Location_asia': Location_asia,
        'Location_europa': Location_europa,
        'Location_nord_america': Location_nord_america,
        'Location_oceania': Location_oceania,
        'Location_sud_america': Location_sud_america,
        'Round_2nd Round': Round_2nd_Round,
        'Round_3rd Round': Round_3rd_Round,
        'Round_4th Round': Round_4th_Round,
        'Round_Quarterfinals': Round_Quarterfinals,
        'Round_Round Robin': Round_Round_Robin,
        'Round_Semifinals': Round_Semifinals,
        'Round_The Final': Round_The_Final,
        'A_hand_R': A_hand_R,
        'A_ioc_asia': A_ioc_asia,
        'A_ioc_europa': A_ioc_europa,
        'A_ioc_nord_america': A_ioc_nord_america,
        'A_ioc_oceania': A_ioc_oceania,
        'A_ioc_sud_america': A_ioc_sud_america,
        'B_hand_R': B_hand_R,
        'B_ioc_asia': B_ioc_asia,
        'B_ioc_europa': B_ioc_europa,
        'B_ioc_nord_america': B_ioc_nord_america,
        'B_ioc_oceania': B_ioc_oceania,
        'B_ioc_sud_america': B_ioc_sud_america
    })
    
    df = pd.DataFrame(d)
    X = sc.transform(df)
    
    return X

col1, col2, col3 = st.columns(3)

with col1:
    g1 = st.selectbox(label='Giocatore_1', options=giocatori.giocatore.values)
    A_B365 = st.number_input(label='A_Bet365')
    
    url = giocatori.link[giocatori.giocatore == g1].values[0]
    r = requests.get(url, headers={'User-Agent': ''})
    soup = BeautifulSoup(r.content, 'html.parser')
    
    A_Pts = int(soup.find_all('td')[9].text.strip().replace(',', ''))
    A_Rank = int(soup.find('td', {'class': 'rank-cell'}).text.strip())
    A_dob = int(soup.find('div', {'class': 'table-big-value'}).text.strip()[:2])
    A_height = int(soup.find('span', {'class': 'table-height-cm-wrapper'}).text.strip()[1:-3])
    braccio = soup.find_all('div', {'class': 'table-value'})[1].text.strip()[0]
    naz = soup.find('div', {'class': 'player-flag-code'}).text.strip()
    
    A_hand_R = 1 if braccio == 'R' else 0
    A_ioc_asia = 1 if naz in asia else 0
    A_ioc_europa = 1 if naz in europa else 0
    A_ioc_nord_america = 1 if naz in nord_america else 0
    A_ioc_oceania = 1 if naz in oceania else 0
    A_ioc_sud_america = 1 if naz in sud_america else 0
    
    st.text(f'Punti ATP: {A_Pts}')
    st.text(f'Rank: {A_Rank}')
    st.text(f'Età: {A_dob}')
    st.text(f'Altezza: {A_height}')
    st.text(f'''Braccio: {'Destro' if braccio == 'R' else 'Sinistro'}''')
    st.text(f'''Nazionalità: {'Europa' if naz in europa else 'Asia' if naz in asia else 'Nord America' if naz in nord_america else 'Sud America' if naz in sud_america else 'Oceania' if naz in oceania else 'Africa'}''')
    
with col2:
    g2 = st.selectbox(label='Giocatore_2', options=giocatori.giocatore.values)
    B_B365 = st.number_input(label='B_Bet365')
    
    url_2 = giocatori.link[giocatori.giocatore == g2].values[0]
    r_2 = requests.get(url_2, headers={'User-Agent': ''})
    soup_2 = BeautifulSoup(r_2.content, 'html.parser')
    
    B_Pts = int(soup_2.find_all('td')[9].text.strip().replace(',', ''))
    B_Rank = int(soup_2.find('td', {'class': 'rank-cell'}).text.strip())
    B_dob = int(soup_2.find('div', {'class': 'table-big-value'}).text.strip()[:2])
    B_height = int(soup_2.find('span', {'class': 'table-height-cm-wrapper'}).text.strip()[1:-3])
    braccio_2 = soup_2.find_all('div', {'class': 'table-value'})[1].text.strip()[0]
    naz_2 = soup_2.find('div', {'class': 'player-flag-code'}).text.strip()
    
    
    B_hand_R = 1 if braccio_2 == 'R' else 0
    B_ioc_asia = 1 if naz_2 in asia else 0
    B_ioc_europa = 1 if naz_2 in europa else 0
    B_ioc_nord_america = 1 if naz_2 in nord_america else 0
    B_ioc_oceania = 1 if naz_2 in oceania else 0
    B_ioc_sud_america = 1 if naz_2 in sud_america else 0
    
    st.text(f'Punti ATP: {B_Pts}')
    st.text(f'Rank: {B_Rank}')
    st.text(f'Età: {B_dob}')
    st.text(f'Altezza: {B_height}')
    st.text(f'''Braccio: {'Destro' if braccio_2 == 'R' else 'Sinistro'}''')
    st.text(f'''Nazionalità: {'Europa' if naz_2 in europa else 'Asia' if naz_2 in asia else 'Nord America' if naz_2 in nord_america else 'Sud America' if naz_2 in sud_america else 'Oceania' if naz_2 in oceania else 'Africa'}''')
    
with col3:
    Date = st.number_input(label='mese', value=0)
    Location_asia = st.number_input(label='luogo_asia', value=0)
    Location_europa = st.number_input(label='luogo_europa', value=0)
    Location_nord_america = st.number_input(label='luogo_nord_america', value=0)
    Location_oceania = st.number_input(label='luogo_oceania', value=0)
    Location_sud_america = st.number_input(label='luogo_sud_america', value=0)
    Round_2nd_Round = st.number_input(label='round_2', value=0)
    Round_3rd_Round = st.number_input(label='round_3', value=0)
    Round_4th_Round = st.number_input(label='round_4', value=0)
    Round_Quarterfinals = st.number_input(label='round_quarti_di_finale', value=0)
    Round_Round_Robin = st.number_input(label='round_robin', value=0)
    Round_Semifinals = st.number_input(label='round_semifinali', value=0)
    Round_The_Final = st.number_input(label='round_finale', value=0)
    
puntata = st.number_input(label='Puntata', value=0)

prevedere = dati(A_B365=A_B365, A_Pts=A_Pts, A_Rank=A_Rank, B_B365=B_B365, B_Pts=B_Pts, B_Rank=B_Rank, Date=Date, 
                    A_dob=A_dob, A_height=A_height, B_dob=B_dob, B_height=B_height,
                    Location_asia=Location_asia, Location_europa=Location_europa, Location_nord_america=Location_nord_america,
                    Location_oceania=Location_oceania, Location_sud_america=Location_sud_america, Round_2nd_Round=Round_2nd_Round,
                    Round_3rd_Round=Round_3rd_Round, Round_4th_Round=Round_4th_Round, Round_Quarterfinals=Round_Quarterfinals,
                    Round_Round_Robin=0, Round_Semifinals=0, Round_The_Final=Round_The_Final,
                    A_hand_R=A_hand_R, A_ioc_asia=A_ioc_asia, A_ioc_europa=A_ioc_europa, A_ioc_nord_america=A_ioc_nord_america,
                    A_ioc_oceania=A_ioc_oceania, A_ioc_sud_america=A_ioc_sud_america, B_hand_R=B_hand_R, B_ioc_asia=B_ioc_asia,
                    B_ioc_europa=B_ioc_europa, B_ioc_nord_america=B_ioc_nord_america, B_ioc_oceania=B_ioc_oceania,
                    B_ioc_sud_america=B_ioc_sud_america)
                    
def previsione():
        outcome = vc.predict_proba(prevedere.reshape(1, -1))
        st.text(f'Giocatore 1: {(round(outcome[0][0]*100, 2))}% | Giocatore 2: {(round(outcome[0][1]*100, 2))}%')
        
        if outcome[0][0] > outcome[0][1]: # probabilità vittoria
            b = A_B365
        else:
            b = B_B365
            
        if outcome[0][0] > outcome[0][1]: # probabilità vittoria
            p = outcome[0][0]
        else:
            p = outcome[0][1]
        
        q = 1 - p # probabilità sconfitta
        
        kelly = (b*p - q) / b
        kelly_2 = ((b*p - q) / b) / 2
        
        st.text(f'Kelly: {round(kelly*100, 2)}% | Kelly_2: {round(kelly_2*100, 2)}%    Quota 1:{b}')
        st.text(f'Puntata_1: {round(kelly*puntata, 2)} | Puntata_2: {round(kelly_2*puntata, 2)}')

st.button('Prevedi', on_click=previsione)