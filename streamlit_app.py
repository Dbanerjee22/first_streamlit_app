import streamlit
import pandas
import requests
import snowflake.connector
#streamlit.header('Breakfast Menu')
#streamlit.text('Omega 3 & Blueberry Oatmeal')
#streamlit.text('Kale, Spinach & Rocket Smoothie')
#streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#setting index
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
if fruits_selected:
  #filter fruits
  fruits_to_show = my_fruit_list.loc[fruits_selected]
  streamlit.dataframe(fruits_to_show)
else:
  streamlit.dataframe(my_fruit_list)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header("Fruityvice Fruit Advice!")
# converting json data into flat table 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# converting flat table into row-column table
streamlit.dataframe(fruityvice_normalized)
#taking user input
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("Thr Fruit load list contains:")
streamlit.dataframe(my_data_row)
#adding fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write("Thanks for adding:",add_my_fruit)
#my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")


  



