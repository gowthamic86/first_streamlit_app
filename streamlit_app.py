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

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit_load list contains")
streamlit.dataframe(my_data_rows)


