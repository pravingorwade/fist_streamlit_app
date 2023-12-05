import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError
streamlit.title('My Parents New Health Diner')

streamlit.header(' Breakfast Favorites')

streamlit.text( '🫕 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐓Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
# streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
# streamlit.dataframe(my_fruit_list)
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header ('Fruityvice Fruit Advice!')
# import requests
#fruityvice_response = requests.get("http://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("http://fruityvice.com/api/fruit/" + "kiwi")
def get_fruityvale_data(this_fruit_choice):
    fruityvice_response = requests.get("http://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruitvice_normalize = pandas.json_normalize(fruityvice_response.json())
    return fruitvice_normalize  
  
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select fruit to get information")
  else:
    #fruityvice_response = requests.get("http://fruityvice.com/api/fruit/" + fruit_choice)
    #streamlit.text(fruityvice_response.json())
    #fruitvice_normalize = pandas.json_normalize(fruityvice_response.json())
    #streamlit.dataframe(fruitvice_normalize)
    back_from_function = get_fruityvale_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e :
  streamlit.error()
 
#streamlit.stop()
streamlit.text( "The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit load list")
    return my_cur.fetchall()
        
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe (my_data_rows)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchall()
#streamlit.text( "Hello from Snowflake:")
#streamlit.text( "The fruit load list contains:")
#streamlit.text(my_data_row)


#add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
#streamlit.write("Thanks for adding " + add_my_fruit)
#my_cur.execute("insert into fruit_load_list values ('From Streamlit')")
