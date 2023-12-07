import streamlit

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



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple', 'Grapefruit'])
fruits_to_show = my_fruit_list.loc[fruits_selected] # only show the filtered entries


# Display the table on the page.
streamlit.dataframe(fruits_to_show)


# New Section to display fruityvice API response (fruityvice does not require an API key)
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json()) #just displayed the output to the screen

# normalize the json version of the response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display on the screen as a table
streamlit.dataframe(fruityvice_normalized)

