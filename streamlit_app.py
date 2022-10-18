import streamlit

streamlit.title('My parents healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('omega 3 & Blueberry Oatmeal')
streamlit.text('Kale ,Spinach and Rocket Smoothie')
streamlit.text('Hard Boiled Free Range Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

#Lets put a pick list here so taht they can pick the fruit where they want to include
streamlit.multiselect("pick some fruits", list(my_fruit_list.index), ['Avacado','Strawberries'])

#display the table on the page
streamlit.dataframe(my_fruit_list)

