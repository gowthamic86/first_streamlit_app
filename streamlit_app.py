import streamlit

streamlit.title('My parents healthy dinner')

import snowflake.connector
import pandas

fruit_listed = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(fruit_listed)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
