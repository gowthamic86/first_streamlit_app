import pandas

fruit_listed = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(fruit_listed)
streamlit.header(':grapes: Breakfast Menu')
streamlit.text(':watermelon: Omega 3 & Blueberry Oatmeal')
streamlit.text(':blueberries: Kale, Spinach & Rocket Smoothie')
streamlit.text(':baguette_bread: Hard-Boiled Free-Range Egg')
