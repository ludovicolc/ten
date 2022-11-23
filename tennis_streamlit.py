import pandas as pd
import joblib
import streamlit as st

'''atp tour --> players --> ranking breakdown
bet 365'''


prev = st.container()

sc = joblib.load('standard_scaler_joblib')
vc = joblib.load('tennis_clf_joblib')

def dati(A_B365, A_Pts, A_Rank, B_B365, B_Pts, B_Rank, Best_of,
       Date, A_dob, A_height, B_dob, B_height, Court_Outdoor=0,
       Location_asia=0, Location_europa=0, Location_nord_america=0,
       Location_oceania=0, Location_sud_america=0, Round_2nd_Round=0,
       Round_3rd_Round=0, Round_4th_Round=0, Round_Quarterfinals=0,
       Round_Round_Robin=0, Round_Semifinals=0, Round_The_Final=0,
       Series_ATP500=0, Series_Grand_Slam=0, Series_International=0,
       Series_International_Gold=0, Series_Masters=0, Series_Masters_1000=0,
       Series_Masters_Cup=0, Surface_Clay=0, Surface_Grass=0, Surface_Hard=0,
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
        'Best of': Best_of,
        'Date': Date,
        'A_dob': A_dob,
        'A_height': A_height,
        'B_dob': B_dob,
        'B_height': B_height,
        'Court_Outdoor': Court_Outdoor,
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
        'Series_ATP500': Series_ATP500,
        'Series_Grand Slam': Series_Grand_Slam,
        'Series_International': Series_International,
        'Series_International Gold': Series_International_Gold,
        'Series_Masters': Series_Masters,
        'Series_Masters 1000': Series_Masters_1000,
        'Series_Masters Cup': Series_Masters_Cup,
        'Surface_Clay': Surface_Clay,
        'Surface_Grass': Surface_Grass,
        'Surface_Hard': Surface_Hard,
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


with prev:
    st.header('Previsione')

    A_B365 = st.number_input(label='A_B365')
    A_Pts = st.number_input(label='A_Pts')
    A_Rank = st.number_input(label='A_Rank')
    B_B365 = st.number_input(label='B_B365')
    B_Pts = st.number_input(label='B_Pts')
    B_Rank = st.number_input(label='B_Rank')
    Best_of = st.number_input(label='Al meglio dei')
    Date = st.number_input(label='mese')
    A_dob = st.number_input(label='A_età')
    A_height = st.number_input(label='A_altezza')
    B_dob = st.number_input(label='B_età')
    B_height = st.number_input(label='B_altezza')
    Court_Outdoor = st.number_input(label='outdoor', value=0)
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
    Series_ATP500 = st.number_input(label='atp5000', value=0)
    Series_Grand_Slam = st.number_input(label='grand_slam', value=0)
    Series_International = st.number_input(label='internazionale', value=0)
    Series_International_Gold = st.number_input(label='internazionale_gold', value=0)
    Series_Masters = st.number_input(label='masters', value=0)
    Series_Masters_1000 = st.number_input(label='masters1000', value=0)
    Series_Masters_Cup = st.number_input(label='masters_cup', value=0)
    Surface_Clay = st.number_input(label='clay', value=0)
    Surface_Grass = st.number_input(label='grass', value=0)
    Surface_Hard = st.number_input(label='hard', value=0)
    A_hand_R = st.number_input(label='A_destro', value=0)
    A_ioc_asia = st.number_input(label='A_nazionalità_asia', value=0)
    A_ioc_europa = st.number_input(label='A_nazionalità_europa', value=0)
    A_ioc_nord_america = st.number_input(label='A_nazionalità_nord_america', value=0)
    A_ioc_oceania = st.number_input(label='A_nazionalità_oceania', value=0)
    A_ioc_sud_america = st.number_input(label='A_nazionalità_sud_america', value=0)
    B_hand_R = st.number_input(label='B_destro', value=0)
    B_ioc_asia = st.number_input(label='B_nazionalità_asia', value=0)
    B_ioc_europa = st.number_input(label='B_nazionalità_europa', value=0)
    B_ioc_nord_america = st.number_input(label='B_nazionalità_nord_america', value=0)
    B_ioc_oceania = st.number_input(label='B_nazionalità_oceania', value=0)
    B_ioc_sud_america = st.number_input(label='B_nazionalità_sud_america', value=0)

    prevedere = dati(A_B365=A_B365, A_Pts=A_Pts, A_Rank=A_Rank, B_B365=B_B365, B_Pts=B_Pts, B_Rank=B_Rank, Best_of=Best_of, Date=Date, 
                    A_dob=A_dob, A_height=A_height, B_dob=B_dob, B_height=B_height, Court_Outdoor=Court_Outdoor,
                    Location_asia=Location_asia, Location_europa=Location_europa, Location_nord_america=Location_nord_america,
                    Location_oceania=Location_oceania, Location_sud_america=Location_sud_america, Round_2nd_Round=Round_2nd_Round,
                    Round_3rd_Round=Round_3rd_Round, Round_4th_Round=Round_4th_Round, Round_Quarterfinals=Round_Quarterfinals,
                    Round_Round_Robin=0, Round_Semifinals=0, Round_The_Final=Round_The_Final,
                    Series_ATP500=Series_ATP500, Series_Grand_Slam=Series_Grand_Slam, Series_International=Series_International,
                    Series_International_Gold=Series_International_Gold, Series_Masters=Series_Masters, Series_Masters_1000=Series_Masters_1000,
                    Series_Masters_Cup=Series_Masters_Cup, Surface_Clay=Surface_Clay, Surface_Grass=Surface_Grass, Surface_Hard=Surface_Hard,
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

    st.button('Prevedi', on_click=previsione)



'''atp tour --> players --> ranking breakdown
bet 365'''

# de minaur vince
# punto 700 euro