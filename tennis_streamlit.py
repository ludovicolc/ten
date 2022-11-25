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
vc = joblib.load('forest_clf_joblib')

def dati(A_Pts, A_Rank, B_Pts, B_Rank,
        Date, A_dob, A_height, B_dob, B_height, st_Serve_x,
        st_Serve_Points_Won_x, nd_Serve_Points_Won_x, Service_Games_Won_x,
        Total_Service_Points_Won_x, st_Serve_Return_Points_Won_x,
        nd_Serve_Return_Points_Won_x, Return_Games_Won_x, Return_Points_Won_x,
        st_Serve_y, st_Serve_Points_Won_y, nd_Serve_Points_Won_y, Service_Games_Won_y,
        Total_Service_Points_Won_y, st_Serve_Return_Points_Won_y,
        nd_Serve_Return_Points_Won_y, Return_Games_Won_y, Return_Points_Won_y,
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
        'A_Pts': A_Pts,
        'A_Rank': A_Rank,
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
        'A_ioc_sud_america': A_ioc_sud_america,
        'B_hand_R': B_hand_R,
        'B_ioc_asia': B_ioc_asia,
        'B_ioc_europa': B_ioc_europa,
        'B_ioc_nord_america': B_ioc_nord_america,
        'B_ioc_sud_america': B_ioc_sud_america,
        '1st Serve_x': st_Serve_x,
        '1st Serve Points Won_x': st_Serve_Points_Won_x,
        '2nd Serve Points Won_x': nd_Serve_Points_Won_x,
       'Service Games Won_x': Service_Games_Won_x,
       'Total Service Points Won_x': Total_Service_Points_Won_x,
       '1st Serve Return Points Won_x': st_Serve_Return_Points_Won_x,
       '2nd Serve Return Points Won_x': nd_Serve_Return_Points_Won_x,
       'Return Games Won_x': Return_Games_Won_x,
       'Return Points Won_x': Return_Points_Won_x,
       '1st Serve_y': st_Serve_y,
       '1st Serve Points Won_y': st_Serve_Points_Won_y,
       '2nd Serve Points Won_y': nd_Serve_Points_Won_y,
       'Service Games Won_y': Service_Games_Won_y,
       'Total Service Points Won_y': Total_Service_Points_Won_y,
       '1st Serve Return Points Won_y': st_Serve_Return_Points_Won_y,
       '2nd Serve Return Points Won_y': nd_Serve_Return_Points_Won_y,
       'Return Games Won_y': Return_Games_Won_y, 
       'Return Points Won_y': Return_Points_Won_y
    })
    
    df = pd.DataFrame(d)
    X = sc.transform(df)
    
    return X

col1, col2, col3 = st.columns(3)

with col1:
    g1 = st.selectbox(label='Giocatore_1', options=giocatori.giocatore.values)
    A_B365 = st.number_input(label='Quota_A')
    
    url_a = giocatori.link_a[giocatori.giocatore == g1].values[0]
    r_a = requests.get(url_a, headers={'User-Agent': ''})
    soup_a = BeautifulSoup(r_a.content, 'html.parser')
    
    url_b = giocatori.link_b[giocatori.giocatore == g1].values[0]
    r_b = requests.get(url_b, headers={'User-Agent': ''})
    soup_b = BeautifulSoup(r_b.content, 'html.parser')
    stats_1 = soup_b.find_all('table', {'class': 'mega-table'})
    
    tab_1 = stats_1[0].find_all('td')
    tab_2 = stats_1[1].find_all('td')
    
    A_Pts = int(soup_a.find_all('td')[9].text.strip().replace(',', ''))
    A_Rank = int(soup_a.find('td', {'class': 'rank-cell'}).text.strip().replace('T', ''))
    A_dob = int(soup_a.find('div', {'class': 'table-big-value'}).text.strip()[:2])
    
    try:
        A_height = int(soup_a.find('span', {'class': 'table-height-cm-wrapper'}).text.strip()[1:-3])
    except:
        A_height = 180
    try:
        braccio = soup_a.find_all('div', {'class': 'table-value'})[1].text.strip()[0]
    except:
        braccio = 'R'
    
    naz = soup_a.find('div', {'class': 'player-flag-code'}).text.strip()
    
    A_hand_R = 1 if braccio == 'R' else 0
    A_ioc_asia = 1 if naz in asia else 0
    A_ioc_europa = 1 if naz in europa else 0
    A_ioc_nord_america = 1 if naz in nord_america else 0
    A_ioc_sud_america = 1 if naz in sud_america else 0
    
    st_Serve_x = int(tab_1[5].text.strip().replace('%', ''))
    st_Serve_Points_Won_x = int(tab_1[7].text.strip().replace('%', ''))
    nd_Serve_Points_Won_x = int(tab_1[9].text.strip().replace('%', ''))
    Service_Games_Won_x = int(tab_1[17].text.strip().replace('%', ''))
    Total_Service_Points_Won_x = int(tab_1[19].text.strip().replace('%', ''))
    st_Serve_Return_Points_Won_x = int(tab_2[1].text.strip().replace('%', ''))
    nd_Serve_Return_Points_Won_x = int(tab_2[3].text.strip().replace('%', ''))
    Return_Games_Won_x = int(tab_2[11].text.strip().replace('%', ''))
    Return_Points_Won_x = int(tab_2[13].text.strip().replace('%', ''))
    
    st.text(f'Punti ATP: {A_Pts}')
    st.text(f'Rank: {A_Rank}')
    st.text(f'Età: {A_dob}')
    st.text(f'Altezza: {A_height}')
    st.text(f'''Braccio: {'Destro' if braccio == 'R' else 'Sinistro'}''')
    st.text(f'''Nazionalità: {'Europa' if naz in europa else 'Asia' if naz in asia else 'Nord America' if naz in nord_america else 'Sud America' if naz in sud_america else 'Oceania' if naz in oceania else 'Africa'}''')
    
    st.text(f'1 servizio: {st_Serve_x}%')
    st.text(f'Punto vinto al primo servizio: {st_Serve_Points_Won_x}%')
    st.text(f'Punto vinto al secondo servizio: {nd_Serve_Points_Won_x}%')
    st.text(f'Game vinto al servizio: {Service_Games_Won_x}%')
    st.text(f'Punti vinti al servizio: {Total_Service_Points_Won_x}%')
    st.text(f'Punto vinto al ritorno del primo servizio: {st_Serve_Return_Points_Won_x}%')
    st.text(f'Punto vinto al ritorno del secondo servizio: {nd_Serve_Return_Points_Won_x}%')
    st.text(f'Game vinto in ritorno: {Return_Games_Won_x}%')
    st.text(f'Punti vinti al ritorno: {Return_Points_Won_x}%')

with col2:
    g2 = st.selectbox(label='Giocatore_2', options=giocatori.giocatore.values)
    B_B365 = st.number_input(label='Quota_B')
    
    url_a2 = giocatori.link_a[giocatori.giocatore == g2].values[0]
    r_a2 = requests.get(url_a2, headers={'User-Agent': ''})
    soup_a2 = BeautifulSoup(r_a2.content, 'html.parser')
    
    url_b2 = giocatori.link_b[giocatori.giocatore == g2].values[0]
    r_b2 = requests.get(url_b2, headers={'User-Agent': ''})
    soup_b2 = BeautifulSoup(r_b2.content, 'html.parser')
    stats_2 = soup_b2.find_all('table', {'class': 'mega-table'})
    
    tab_12 = stats_2[0].find_all('td')
    tab_22 = stats_2[1].find_all('td')
    
    B_Pts = int(soup_a2.find_all('td')[9].text.strip().replace(',', ''))
    B_Rank = int(soup_a2.find('td', {'class': 'rank-cell'}).text.strip().replace('T', ''))
    B_dob = int(soup_a2.find('div', {'class': 'table-big-value'}).text.strip()[:2])
    
    try:
        B_height = int(soup_a2.find('span', {'class': 'table-height-cm-wrapper'}).text.strip()[1:-3])
    except:
        B_height = 180
    try:
        braccio_2 = soup_a2.find_all('div', {'class': 'table-value'})[1].text.strip()[0]
    except:
        braccio_2 = 'R'
    
    naz_2 = soup_a2.find('div', {'class': 'player-flag-code'}).text.strip()
    
    B_hand_R = 1 if braccio_2 == 'R' else 0
    B_ioc_asia = 1 if naz_2 in asia else 0
    B_ioc_europa = 1 if naz_2 in europa else 0
    B_ioc_nord_america = 1 if naz_2 in nord_america else 0
    B_ioc_sud_america = 1 if naz_2 in sud_america else 0
    
    st_Serve_y = int(tab_12[5].text.strip().replace('%', ''))
    st_Serve_Points_Won_y = int(tab_12[7].text.strip().replace('%', ''))
    nd_Serve_Points_Won_y = int(tab_12[9].text.strip().replace('%', ''))
    Service_Games_Won_y = int(tab_12[17].text.strip().replace('%', ''))
    Total_Service_Points_Won_y = int(tab_12[19].text.strip().replace('%', ''))
    st_Serve_Return_Points_Won_y = int(tab_22[1].text.strip().replace('%', ''))
    nd_Serve_Return_Points_Won_y = int(tab_22[3].text.strip().replace('%', ''))
    Return_Games_Won_y = int(tab_22[11].text.strip().replace('%', ''))
    Return_Points_Won_y = int(tab_22[13].text.strip().replace('%', ''))
    
    st.text(f'Punti ATP: {B_Pts}')
    st.text(f'Rank: {B_Rank}')
    st.text(f'Età: {B_dob}')
    st.text(f'Altezza: {B_height}')
    st.text(f'''Braccio: {'Destro' if braccio_2 == 'R' else 'Sinistro'}''')
    st.text(f'''Nazionalità: {'Europa' if naz_2 in europa else 'Asia' if naz_2 in asia else 'Nord America' if naz_2 in nord_america else 'Sud America' if naz_2 in sud_america else 'Oceania' if naz_2 in oceania else 'Africa'}''')
    
    st.text(f'1 servizio: {st_Serve_y}%')
    st.text(f'Punto vinto al primo servizio: {st_Serve_Points_Won_y}%')
    st.text(f'Punto vinto al secondo servizio: {nd_Serve_Points_Won_y}%')
    st.text(f'Game vinto al servizio: {Service_Games_Won_y}%')
    st.text(f'Punti vinti al servizio: {Total_Service_Points_Won_y}%')
    st.text(f'Punto vinto al ritorno del primo servizio: {st_Serve_Return_Points_Won_y}%')
    st.text(f'Punto vinto al ritorno del secondo servizio: {nd_Serve_Return_Points_Won_y}%')
    st.text(f'Game vinto in ritorno: {Return_Games_Won_y}%')
    st.text(f'Punti vinti al ritorno: {Return_Points_Won_y}%')
    
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

prevedere = dati(A_Pts=A_Pts, A_Rank=A_Rank, B_Pts=B_Pts, B_Rank=B_Rank, Date=Date, 
                    A_dob=A_dob, A_height=A_height, B_dob=B_dob, B_height=B_height,
                    Location_asia=Location_asia, Location_europa=Location_europa, Location_nord_america=Location_nord_america,
                    Location_oceania=Location_oceania, Location_sud_america=Location_sud_america, Round_2nd_Round=Round_2nd_Round,
                    Round_3rd_Round=Round_3rd_Round, Round_4th_Round=Round_4th_Round, Round_Quarterfinals=Round_Quarterfinals,
                    Round_Round_Robin=0, Round_Semifinals=0, Round_The_Final=Round_The_Final,
                    A_hand_R=A_hand_R, A_ioc_asia=A_ioc_asia, A_ioc_europa=A_ioc_europa, A_ioc_nord_america=A_ioc_nord_america,
                    A_ioc_sud_america=A_ioc_sud_america, B_hand_R=B_hand_R, B_ioc_asia=B_ioc_asia,
                    B_ioc_europa=B_ioc_europa, B_ioc_nord_america=B_ioc_nord_america,
                    B_ioc_sud_america=B_ioc_sud_america, st_Serve_x=st_Serve_x, st_Serve_Points_Won_x=st_Serve_Points_Won_x,
                    nd_Serve_Points_Won_x=nd_Serve_Points_Won_x, Service_Games_Won_x=Service_Games_Won_x, Total_Service_Points_Won_x=Total_Service_Points_Won_x,
                    st_Serve_Return_Points_Won_x=st_Serve_Return_Points_Won_x, nd_Serve_Return_Points_Won_x=nd_Serve_Return_Points_Won_x,
                    Return_Games_Won_x=Return_Games_Won_x, Return_Points_Won_x=Return_Points_Won_x,
                    st_Serve_y=st_Serve_y, st_Serve_Points_Won_y=st_Serve_Points_Won_y, nd_Serve_Points_Won_y=nd_Serve_Points_Won_y,
                    Service_Games_Won_y=Service_Games_Won_y, Total_Service_Points_Won_y=Total_Service_Points_Won_y,
                    st_Serve_Return_Points_Won_y=st_Serve_Return_Points_Won_y, nd_Serve_Return_Points_Won_y=nd_Serve_Return_Points_Won_y,
                    Return_Games_Won_y=Return_Games_Won_y, Return_Points_Won_y=Return_Points_Won_y)
                    
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
        
        st.text(f'Kelly: {round(kelly*100, 2)}%  |  Quota 1:{b}')
        st.text(f'Puntata_1: {round(kelly*puntata, 2)}')

st.button('Prevedi', on_click=previsione)