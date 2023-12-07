import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My Parents New Healthy Diner')


streamlit.header('Breakfast Menu')

# streamlit.text('Omega 3 and Blueberry Oatmeal')
# streamlit.text('Kale, Spinach and Rocket Smoothie')
# streamlit.text('Hard-Boiled Free-Range Egg')


streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple', 'Grapefruit'])
fruits_to_show = my_fruit_list.loc[fruits_selected] # only show the filtered entries


# Display the table on the page.
streamlit.dataframe(fruits_to_show)


# New Section to display fruityvice API response (fruityvice does not require an API key)
streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()
  
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) #just displayed the output to the screen

# normalize the json version of the response
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display on the screen as a table
#streamlit.dataframe(fruityvice_normalized)



# DO NOT RUN ANYTHING POST HERE WHILE TROUBLESHOOTING IS GOING ON
streamlit.stop()

# import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)


my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
#my_data_row = my_cur.fetchone() #fetches only one row
# streamlit.text("FRUIT LOAD LIST CONTAINS:")
# streamlit.text(my_data_row)

my_data_rows = my_cur.fetchall()
streamlit.header("THE FRUIT LOAD LIST CONTAINS:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)



# just to test the flow control, will NOT work correctly, but got with it for now

my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")
