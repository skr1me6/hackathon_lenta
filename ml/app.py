#Импорты. Проверить, что все библиотеки поставлены.
import numpy as np
import pandas as pd
import pickle
from catboost import CatboostRegressor

# Загрузка датафрейма теста.
# Поменять путь на свой.
with open(
    '/home/kubanez/Dev/hackathon_lenta/app/'
    'df_test.pkl', 'rb'
) as df:
    df_test = pickle.load(df)

# Загрузка признаков теста.
# Поменять путь на свой.
with open(
    '/home/kubanez/Dev/hackathon_lenta/app/'
    'features_test', 'rb'
) as f:
    features_test = pickle.load(f)

# Загрузка таргета теста.
# Поменять путь на свой.
with open(
    '/home/kubanez/Dev/hackathon_lenta/app/'
    'target_test.pkl', 'rb'
) as t:
    target_test = pickle.load(t)

# Загрузка модели.
# Поменять путь на свой.
with open(
    '/home/kubanez/Dev/hackathon_lenta/app/'
    'catboost_model_40.0.pkl', 'rb'
) as m:
    model = pickle.load(m)

# Предсказания модели.
predictions = model.predict(features_test)

df_to_endpoint = pd.DataFrame()

df_to_endpoint[['st_id', 'date', 'pr_sku_id']] = df_test[['st_id', 'date', 'pr_sku_id']]
df_to_endpoint['sales_units'] = predictions

# День прогноза
today='07/05/2023'

# Создания словаря result_main
def result_gen(row, today):
    
    result = []
    store = row['st_id']
    product = row['pr_sku_id']
    forecast_date = pd.to_datetime(row['date']).strftime('%m/%d/%Y')
    prediction_sales = row['sales_units']

    result.append({'store': store,
                   'forecast_date': today,
                   'forecast': {'sku': product,
                                'sales_units': (forecast_date, prediction_sales)}})
    
    return result

result_main = df_to_endpoint.apply(result_gen, today=today, axis = 1)

# main
def main(result_main):

    for value in result_main:
        requests.post(get_address(URL_FORECAST), json={"data": value}) 
