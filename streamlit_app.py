import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My parents healthy dinner')
streamlit.header('Breakfast favourites')
streamlit.text('omega 3 & Blueberry Oatmeal')
streamlit.text('Kale ,Spinach and Rocket Smoothie')
streamlit.text('Hard Boiled Free Range Egg')
streamlit.text('Avacado toast')
streamlit.header('Build your own fruit smoothie')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit_load list contains")
streamlit.dataframe(my_data_rows)

streamlit.write('Thanks for adding', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')");

