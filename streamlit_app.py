# Import python packages.
import streamlit as st
from snowflake.snowpark.functions import col
import requests
import pandas as pd

# Write directly to the app.
st.title(f"Zena's Amazing Athleisure Catalog")
#st.write(
#  """Pick a sweatsuit color or style:
#  """)

#name_on_order = st.text_input("Name on Smoothie:")
#st.write("The name on your Smoothie will be: ", name_on_order)

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("zenas_athleisure_db.products.catalog_for_website").select(col('COLOR_OR_STYLE'),col('FILE_URL'))
#st.dataframe(data=my_dataframe, use_container_width=True)
#st.stop()

pd_df=my_dataframe.to_pandas()
#st.dataframe(pd_df)
#st.stop()

sweatsuit_list = st.selectbox(
    'Pick a sweatsuit color or style:'
    , my_dataframe
)

if sweatsuit_list:
   
    sweatsuit_string = ''

    for color_chosen in sweatsuit_list:
        sweatsuit_string += color_chosen 

        search_on=pd_df.loc[pd_df['COLOR_OR_STYLE'] == color_chosen].iloc[0]
        st.write('The search value for ', color_chosen,' is ', color_chosen, '.')
        
        #st.subheader(color_chosen + ' Nutrition Information')
        image_response = requests.get(f"{FILE_URL}")
        st.image_response     
  #      sf_df = st.dataframe(data=image_response.json(),use_container_width=True)
    #st.write(ingredients_string)

    #my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
                    #values ('""" + ingredients_string + """','""" + name_on_order + """')"""

   # st.write(my_insert_stmt)
    #st.stop()
   # time_to_insert = st.button('Submit Order')

   # if time_to_insert:
     #   session.sql(my_insert_stmt).collect()
    #    st.success('Your Smoothie is ordered, ' + name_on_order + '!', icon="✅")
