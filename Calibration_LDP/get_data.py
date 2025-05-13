import pandas as pd
import numpy as np
from pyjstat import pyjstat
from ecbdata import ecbdata
import requests
from datetime import datetime
from io import BytesIO
from config import *
from functions import *
import os

if __name__ == "__main__":
    from config import *
    from functions import *
    start_date = '2006-01-01'

    # macroeconomic data
    macro_ecb_data = process_ecb_indicators(MAP_CATEGORIES_ECB_INDICADORS_URLS, start_date=start_date) # annual data (number)
    
    df_unemployment = extract_data_from_ecb( # monthly data (start of period)
        MAP_OTHER_ECB_INDICATORS["Unemployment rate"]['url'].split("datasets/")[1].split('/')[1] ,
          start_date).rename(columns={''
          'TIME_PERIOD': 'Date',
          'OBS_VALUE': 'Unemployment rate'}) 
    
    df_labour_prod = extract_data_from_ecb( # quarterly data (start of period)
        MAP_OTHER_ECB_INDICATORS["Labour Productivity (per persons)"]['url'].split("datasets/")[1].split('/')[1],
          start_date).rename(
            columns={'TIME_PERIOD': 'Date',
                     'OBS_VALUE': 'Labour Productivity (per persons)'})  
    
    df_inflation = extract_data_from_bank_pt( # monthly data (end of period)
        MAP_OTHER_BPSTAT_INDICATORS["CPI (Consumer Price Index) MA12"]['url'], None) 
     
    df_euribors = extract_euribors(start_date) # monthly data (start of period)
    
    # LDPs data (Small companies)  
    df_small_ldp = get_ldp_data(SMALL_ENTREPRISE_MAP_INDICATORS_KEYS)
    
    # LDPs data (Medium companies)
    df_medium_ldp = get_ldp_data(MEDIUM_ENTREPRISE_MAP_INDICATORS_KEYS)
    # LDPs data (Large companies)
    df_large_ldp = get_ldp_data(LARGE_ENTREPRISE_MAP_INDICATORS_KEYS)
    # LDPs data (All companies)
    df_all_ldp = get_ldp_data(ALL_ENTREPRISE_MAP_INDICATORS_KEYS)

    # save data
    folder_path = "Data"
    
    # Verifica se a pasta existe; se não, cria
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Guardar os DataFrames
    macro_ecb_data.to_csv(os.path.join(folder_path, "macro_ecb_data.csv"), index=False)
    df_unemployment.to_csv(os.path.join(folder_path, "unemployment_rate.csv"), index=False)
    df_labour_prod.to_csv(os.path.join(folder_path, "labour_productivity.csv"), index=False)
    df_inflation.to_csv(os.path.join(folder_path, "inflation_cpi_ma12.csv"), index=False)
    df_euribors.to_csv(os.path.join(folder_path, "euribors.csv"), index=False)
    df_small_ldp.to_csv(os.path.join(folder_path, "small_ldp.csv"), index=False)
    df_medium_ldp.to_csv(os.path.join(folder_path, "medium_ldp.csv"), index=False)
    df_large_ldp.to_csv(os.path.join(folder_path, "large_ldp.csv"), index=False)
    df_all_ldp.to_csv(os.path.join(folder_path, "all_ldp.csv"), index=False)

    print("Todos os dados foram atualizados e guardados com sucesso!")
