import streamlit

streamlit.title('My Parents New Health Diner')

streamlit.header(' Breakfast Favorites')

streamlit.text( '🫕 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐓Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
# streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
# streamlit.dataframe(my_fruit_list)
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
import requests
streamlit.header ('Fruityvice Fruit Advice!')
#fruityvice_response = requests.get("http://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("http://fruityvice.com/api/fruit/" + "kiwi")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
fruityvice_response = requests.get("http://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())
fruitvice_normalize = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruitvice_normalize)



