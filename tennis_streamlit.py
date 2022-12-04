import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import requests
import supporto


# Componenti di base
giocatori = pd.read_csv('link_giocatori.csv')
vc = supporto.vc

europa =  supporto.europa
sud_america = supporto.sud_america
nord_america = supporto.nord_america
africa = supporto.africa
asia = supporto.asia
oceania = supporto.oceania

# Struttura pagina
st.header('Giocatori')
col1, col2 = st.columns(2)
with col1:
    g1 = st.selectbox(label='Giocatore A', options=giocatori.giocatore.values)
    a_b365 = st.number_input(label='Quota A (Bet365)')
    
    url_a = giocatori.link[giocatori.giocatore == g1].values[0]
    r_a = requests.get(url_a, headers={'User-Agent': ''})
    soup_a = BeautifulSoup(r_a.content, 'html.parser')
    
    a_pts = int(soup_a.find_all('td')[9].text.strip().replace(',', ''))
    a_rank = int(soup_a.find('td', {'class': 'rank-cell'}).text.strip().replace('T', ''))
    try:
        a_dob = int(soup_a.find('div', {'class': 'table-big-value'}).text.strip()[:2])
    except:
        a_dob = 27  # mediana
    try:
        a_height = int(soup_a.find('span', {'class': 'table-height-cm-wrapper'}).text.strip()[1:-3])
    except:
        a_height = 185  # mediana
    try:
        braccio = soup_a.find_all('div', {'class': 'table-value'})[1].text.strip()[0]
    except:
        braccio = 'R'  # moda
    try:
        naz = soup_a.find('div', {'class': 'player-flag-code'}).text.strip()
    except:
        naz = ''
    
    a_hand_R = 1 if braccio == 'R' else 0
    a_ioc_asia = 1 if naz in asia else 0
    a_ioc_europa = 1 if naz in europa else 0
    a_ioc_nord_america = 1 if naz in nord_america else 0
    a_ioc_sud_america = 1 if naz in sud_america else 0
    a_ioc_oceania = 1 if naz in oceania else 0
    
    st.text(f'Punti ATP: {a_pts}')
    st.text(f'Rank: {a_rank}')
    st.text(f'Età: {a_dob}')
    st.text(f'Altezza: {a_height}')
    st.text(f'''Braccio: {'Destro' if braccio == 'R' else 'Sinistro'}''')
    st.text(f'''Continente appartenenza: {'Europa' if naz in europa else 'Asia' if naz in asia else 'Nord America' if naz in nord_america
            else 'Sud America' if naz in sud_america else 'Oceania' if naz in oceania else 'Africa'}''')

with col2:
    g2 = st.selectbox(label='Giocatore B', options=giocatori.giocatore.values)
    b_b365 = st.number_input(label='Quota B (Bet365)')
    
    url_b = giocatori.link[giocatori.giocatore == g2].values[0]
    r_b = requests.get(url_b, headers={'User-Agent': ''})
    soup_b = BeautifulSoup(r_b.content, 'html.parser')
    
    b_pts = int(soup_b.find_all('td')[9].text.strip().replace(',', ''))
    b_rank = int(soup_b.find('td', {'class': 'rank-cell'}).text.strip().replace('T', ''))
    
    try:
        b_dob = int(soup_b.find('div', {'class': 'table-big-value'}).text.strip()[:2])
    except:
        b_dob = 27  # mediana
    try:
        b_height = int(soup_b.find('span', {'class': 'table-height-cm-wrapper'}).text.strip()[1:-3])
    except:
        b_height = 185  # mediana
    try:
        braccio_2 = soup_b.find_all('div', {'class': 'table-value'})[1].text.strip()[0]
    except:
        braccio_2 = 'R'  # moda
    try:
        naz_2 = soup_a.find('div', {'class': 'player-flag-code'}).text.strip()
    except:
        naz_2 = ''
    
    b_hand_R = 1 if braccio_2 == 'R' else 0
    b_ioc_asia = 1 if naz_2 in asia else 0
    b_ioc_europa = 1 if naz_2 in europa else 0
    b_ioc_nord_america = 1 if naz_2 in nord_america else 0
    b_ioc_sud_america = 1 if naz_2 in sud_america else 0
    b_ioc_oceania = 1 if naz_2 in oceania else 0
    
    st.text(f'Punti ATP: {b_pts}')
    st.text(f'Rank: {b_rank}')
    st.text(f'Età: {b_dob}')
    st.text(f'Altezza: {b_height}')
    st.text(f'''Braccio: {'Destro' if braccio_2 == 'R' else 'Sinistro'}''')
    st.text(f'''Continente appartenenza: {'Europa' if naz_2 in europa else 'Asia' if naz_2 in asia else 'Nord America' if naz_2 in nord_america
            else 'Sud America' if naz_2 in sud_america else 'Oceania' if naz_2 in oceania else 'Africa'}''')
    
st.header('Torneo')
col_ca, col_cb, col_cc = st.columns(3)
with col_ca:
    date = st.selectbox(label='Mese', options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
with col_cb:
    continente = st.selectbox(label='Continente', options=['Asia', 'Europa', 'Nord America', 'Sud America', 'Oceania', 'Africa'])
with col_cc:
    round_ = st.selectbox(label='Round', options=['Round 1', 'Round 2', 'Round 3', 'Round 4', 'Quarti di finale', 'Round robin', 'Semifinale', 'Finale'])

st.header('Puntata')
with st.container():
    puntata = st.number_input(label='Puntata', value=0)
    

# Trasformazione location torneo
location_asia = 1 if continente == 'Asia' else 0
location_europa = 1 if continente == 'Europa' else 0
location_nord_america = 1 if continente == 'Nord America' else 0
location_oceania = 1 if continente == 'Sud America' else 0
location_sud_america = 1 if continente == 'Oceania' else 0

# Trasformazione round torneo
round_2nd_round = 1 if round_ == 'Round 2' else 0
round_3rd_round = 1 if round_ == 'Round 3' else 0
round_4th_round = 1 if round_ == 'Round 4' else 0
round_quarterfinals = 1 if round_ == 'Quarti di finale' else 0
round_round_robin = 1 if round_ == 'Round robin' else 0
round_semifinals = 1 if round_ == 'Semifinale' else 0
round_the_final = 1 if round_ == 'Finale' else 0


# Tabella dinamica
if 'giocat' not in st.session_state:
    st.session_state.giocat = []
if 'pr_vit_b365' not in st.session_state:
    st.session_state.pr_vit_b365 = []
if 'pr_vit' not in st.session_state:
    st.session_state.pr_vit = []
if 'kel' not in st.session_state:
    st.session_state.kel = []
if 'punt' not in st.session_state:
    st.session_state.punt = []
if 'quot' not in st.session_state:
    st.session_state.quot = []
if 'val_at' not in st.session_state:
    st.session_state.val_at = []

df = pd.DataFrame({
            'Giocatore': st.session_state.giocat,
            'Probabilità di vittoria Bet365': st.session_state.pr_vit_b365,
            'Probabilità di vittoria calcolata': st.session_state.pr_vit,
            '% Kelly': st.session_state.kel,
            'Quota': st.session_state.quot,
            'Valore atteso': st.session_state.val_at,
            'Puntata': st.session_state.punt,
            })

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)

tabella = st.table(df.sort_values(by='% Kelly', ascending=False))
    

# Elaborazione dati
prevedere = supporto.dati(a_b365=a_b365, b_b365=b_b365,a_pts=a_pts, a_rank=a_rank, b_pts=b_pts, b_rank=b_rank, date=date, 
                a_dob=a_dob, a_height=a_height, b_dob=b_dob, b_height=b_height,
                location_asia=location_asia, location_europa=location_europa, location_nord_america=location_nord_america,
                location_oceania=location_oceania, location_sud_america=location_sud_america, round_2nd_round=round_2nd_round,
                round_3rd_round=round_3rd_round, round_4th_round=round_4th_round, round_quarterfinals=round_quarterfinals,
                round_round_robin=0, round_semifinals=0, round_the_final=round_the_final,
                a_hand_R=a_hand_R, a_ioc_asia=a_ioc_asia, a_ioc_europa=a_ioc_europa, a_ioc_nord_america=a_ioc_nord_america,
                a_ioc_sud_america=a_ioc_sud_america, a_ioc_oceania=a_ioc_oceania, b_hand_R=b_hand_R, b_ioc_asia=b_ioc_asia,
                b_ioc_europa=b_ioc_europa, b_ioc_nord_america=b_ioc_nord_america,
                b_ioc_sud_america=b_ioc_sud_america, b_ioc_oceania=b_ioc_oceania
                )

def previsione():
        outcome = vc.predict_proba(prevedere.reshape(1, -1))
        
        if outcome[0][0] > outcome[0][1]:
            b = a_b365
            p_bet = 1 / a_b365
        else:
            b = b_b365
            p_bet = 1 / b_b365
            
        if outcome[0][0] > outcome[0][1]:
            p = outcome[0][0]
            st.session_state.giocat.append(g1)
        else:
            p = outcome[0][1]
            st.session_state.giocat.append(g2)
        
        q = 1 - p
        kelly = ((b * p) - q) / b
        kel_p = kelly*puntata
        va = (p * b * kel_p) - (kel_p * q)
        
        st.session_state.pr_vit_b365.append(f'{round(p_bet*100, 2)}%')
        st.session_state.pr_vit.append(f'{round(p*100, 2)}%')
        st.session_state.kel.append(f'{round(kelly*100, 2)}%')
        st.session_state.punt.append(f'{round(kel_p, 2)}')
        st.session_state.quot.append(f'{round(b, 2)}')
        st.session_state.val_at.append(f'{round(va, 2)}')

prevedi = st.button('Prevedi', on_click=previsione)