import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents New Healthy Dinner')

streamlit.text('omega 3 & Blueberry Oatmeal')
streamlit.text('Kale ,Spinach and Rocket Smoothie')
streamlit.text('Hard Boiled Free Range Egg')
streamlit.text('Avocado toast')

streamlit.header('Build your own fruit smoothie')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

#Create the repeatable code block(called function)
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
    
#take the json version of the response and normalise it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)

#dont run anything past here whlewe troubleshoot
streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)

#allow the end user to add a fruit to the list 
add_my_fruit = streamlit.text_input('What fruit would you like to add','Jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)

#This will ot work
my_cur.execute("insert into fruit_load_list values('from streamlit')")
