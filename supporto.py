import pandas as pd
import joblib

sca = joblib.load('standard_scaler_b_joblib')
vc = joblib.load('vc_b_clf_joblib')

europa =  ['ESP', 'FRA', 'GER', 'RUS', 'ITA', 'CZE', 'CRO',
       'SRB', 'SUI', 'GBR', 'BEL', 'AUT', 'SVK', 'NED', 'SWE', 'ROU',
       'FIN', 'POR', 'POL', 'BUL', 'CYP', 'BLR', 'UKR', 'SLO', 'LAT', 'NOR',  'BIH', 'GRE',
       'GEO', 'LUX', 'DEN', 'HUN', 'LTU', 'MDA', 'EST', 'IRL', 'BAR', 'ESA']
sud_america= ['ARG', 'BRA', 'COL', 'URU', 'ECU', 'PER', 'CHI', 'BOL', 'MEX', 'PAR']
nord_america= ['USA', 'CAN']
africa = ['RSA', 'TUN', 'MAR', 'TUR', 'EGY', 'ALG', 'ZIM']
asia = ['JPN', 'KAZ', 'UZB', 'ISR', 'IND', 'THA', 'KOR', 'ARM', 'CHN', 'TPE', 'PHI', 'MON', 'PAK']
oceania = ['NZL', 'AUS']

def dati(a_b365, b_b365, a_pts, a_rank, b_pts, b_rank,
        date, a_dob, a_height, b_dob, b_height, 
        location_asia=0, location_europa=0, location_nord_america=0,
        location_oceania=0, location_sud_america=0, round_2nd_round=0,
        round_3rd_round=0, round_4th_round=0, round_quarterfinals=0,
        round_round_robin=0, round_semifinals=0, round_the_final=0,
        a_hand_R=0, a_ioc_asia=0, a_ioc_europa=0, a_ioc_nord_america=0,
        a_ioc_oceania=0, a_ioc_sud_america=0, b_hand_R=0, b_ioc_asia=0,
        b_ioc_europa=0, b_ioc_nord_america=0, b_ioc_oceania=0,
        b_ioc_sud_america=0):
    
    pron = 0 if a_b365 < b_b365 else 1
    diff_pts = a_pts - b_pts
    diff_rank = a_rank - b_rank
    diff_dob = a_dob - b_dob
    
    d = []
    d.append({
        'a_pts': a_pts,
        'a_rank': a_rank,
        'b_pts': b_pts,
        'b_rank': b_rank,
        'date': date,
        'a_dob': a_dob,
        'a_height': a_height,
        'b_dob': b_dob,
        'b_height': b_height,
        'pronostico': pron,
        'diff_pts': diff_pts,
        'diff_rank': diff_rank,
        'diff_dob': diff_dob,
        'location_asia': location_asia,
        'location_europa': location_europa,
        'location_nord_america': location_nord_america,
        'location_oceania': location_oceania,
        'location_sud_america': location_sud_america,
        'round_2nd round': round_2nd_round,
        'round_3rd round': round_3rd_round,
        'round_4th round': round_4th_round,
        'round_quarterfinals': round_quarterfinals,
        'round_round robin': round_round_robin,
        'round_semifinals': round_semifinals,
        'round_the final': round_the_final,
        'a_hand_R': a_hand_R,
        'a_ioc_asia': a_ioc_asia,
        'a_ioc_europa': a_ioc_europa,
        'a_ioc_nord_america': a_ioc_nord_america,
        'a_ioc_oceania': a_ioc_oceania,
        'a_ioc_sud_america': a_ioc_sud_america,
        'b_hand_R': b_hand_R,
        'b_ioc_asia': b_ioc_asia,
        'b_ioc_europa': b_ioc_europa,
        'b_ioc_nord_america': b_ioc_nord_america,
        'b_ioc_oceania': b_ioc_oceania,
        'b_ioc_sud_america': b_ioc_sud_america,
    })
    
    df = pd.DataFrame(d)
    X = sca.transform(df)
    
    return X