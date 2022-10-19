import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
fruit_selected = streamlit.multiselect("Pick some fruits", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#Create the repeatable code block(called a function)
def get_fruity_vice_data(this_fruit_choice):
    fruityvice_reponse = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruitvice_normalized  = pandas.json_normalize(fruityvice_response.json())
    return fruitvice_normalized
  
#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
       streamlit.error("Please select a fruit to get information.")
  else:
      back_from_function = get_fruityvice_data(fruity_choice)
      streamlit.dataframe(back_from_function)

streamlit.header("The fruit_load list contains")
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.xursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()

#add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)    
