

# Получаем текущую дату и время
import pickle
import os

def forecast(df,sku_,fold):
    """
    Загрузка моделей для конкретного магазина.
    :param df: DF
    :param sku_: название модели
    :param fold: путь магазина
    :return: Массив предсказаний
    """

    with open(os.path.join(fold, f'{sku_}.pkl'), 'rb') as file:
        sku_n_model = pickle.load(file)
    predictions = sku_n_model.predict(df)
    return predictions
