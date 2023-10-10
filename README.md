<p class="text-center">Hackathon_lenta_2023</p>

![Иллюстрация к проекту](https://www.tadviser.ru/images/c/ce/%D0%9B%D0%B5%D0%BD%D1%82%D0%B0_%D0%BB%D0%BE%D0%B3%D0%BE.png)

# Хакатон "Предсказание временных рядов"

В этом репозитории представленно решение задачи прогнозирования продаж времееного ряда товаров собственного производства магазинов "Лента".

Команды Мастерских Яндекс Практикума и команда Ленты подготовила хакатон, в рамках которого команды создают интерфейс и предсказательную модель по прогнозированию спроса на товары заказчика собственного производства.
## Общее о задаче:

- [Техническое задание заказчика](https://disk.yandex.ru/i/XcbZVaLP48xMZA)
- [Дата-сет заказчика](https://disk.yandex.ru/d/1Q7sWF5LLweoTw)
    - [Описание данных](https://disk.yandex.ru/i/xvXsz0Qgy0d3JA)
    - [Описание задачи](https://disk.yandex.ru/i/flSViZOzj-SeYQ)
    - [Мокап](https://github.com/dataMasterskaya/LentaTimeSeries/tree/main)
- [Брендбук заказчика](https://disk.yandex.ru/i/J_Ieb_CgJ1ibnw)
    - [Описание работы пользователя с системой](https://disk.yandex.ru/i/69TpNiaDQGfx2Q)

## Структура репозитория
/drafts, /prefinal_models, Тест модели 2 сезон, /ml - Черновики и файлы.

Итоговые файлы:
* [eda_final.ipynb](eda_final.ipynb) - Итоговый файл с EDA;
* [preprocess.ipynb](preprocess.ipynb) - Итоговая обработка данных перед обучением;
* [model_final.ipynb](model_final.ipynb) - Итоговая модель машинного обучения с важностьб признаков;
* [sales_submission_csv_fill.ipynb](sales_submission_csv_fill.ipynb) - Заполнения файла sales_submission;
* [sales_submission_filled.csv](sales_submission_filled.csv) - Заполненный файл sales_submission;
* [solution_description.docx](solution_description.docx) - Описание решения. Приведены признаки, алгоритм обучения и важность признаков.

## Чек-лист по работе 
1. Файл в зафиксированном формате с результатом прогноза спроса (sales_submission.csv) ✔️.
2. Воспроизводимый код на Python ✔️
3. Описание решения✔️:
    
    a. Описание обученной модели прогноза спроса✔️
    
    i. Признаки
    ii. интерпретация (shapley values),
    iii. кросс-валидация
    iv. алгоритмы
    
    b. Описание вашего алгоритма оптимизации✔️:
    
    i. методология расчетов
    ii. скорость оптимизации
