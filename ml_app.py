import streamlit as st
import pandas as pd
from catboost import CatBoostRegressor
import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# Set Page Layout
st.set_page_config(layout='wide')


model = CatBoostRegressor()
model.load_model('diamond_catboost', format='cbm')


def predict(carat, cut, color, clarity, depth, table, x, y, z):
    prediction = model.predict(pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]], columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']))
    return prediction



st.title('Прогноз годовой чистой прибыли')
st.warning('Внимание! Модель является прототипом, предсказания ошибочные т.к. нужно по-другому обучить модель!')
# st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
st.header('Введите параметры:')


carat = st.number_input('Количество арендованного оборудования:', min_value=0.0, max_value=100.0, value=1.0)

cut = st.selectbox('Федеральный округ:', ['Центральный', 'Южный', 'СевероЗападный', 'Приволжский', 'Дальневосточный'])

color = st.selectbox('Отрасль производства', ['Легкая', 'Металлургия', 'Швейная', 'Химическая', 'Обувная', 'Лесная', 'Производство машин'])

clarity = st.selectbox('Месяц', ['Декабрь', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль'])

depth = st.number_input('Доля бракованной продукции:', min_value=1.0, max_value=100.0, value=1.0)

table = st.number_input('Среднесписочная численность трудоустроенных:', min_value=0.1, max_value=30000.0, value=1.0)

x = st.number_input('Количество заключенных контрактов на производство:', min_value=0.1, max_value=100000.0, value=1.0)

y = st.number_input('Остатки продукции, тыс. руб', min_value=0.1, max_value=200000.0, value=1.0)

z = st.number_input('Количество затраченных человеко-часов', min_value=0.1, max_value=200000.0, value=1.0)

if st.button('Прогноз прибыли'):
    price = predict(carat, cut, color, clarity, depth, table, x, y, z)
    st.success(f'Годовая чистая прибыль {price[0]:.2f} тыс.руб.')