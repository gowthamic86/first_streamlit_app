import streamlit

streamlit.title('My parents healthy dinner')

import snowflake.connector
import pandas

fruit_listed = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(fruit_listed)
