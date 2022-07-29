"""
    Streamlit webserver-based Recommender Engine.
    Author: Explore Data Science Academy.
    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.
    NB: !! Do not remove/modify the code delimited by dashes !!
    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------
    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.
	For further help with the Streamlit framework, see:
	https://docs.streamlit.io/en/latest/
"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

#getting images from imdb database

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

#Code to ensure the app will cover the whole width of website page
#and scale dynamically.
#must always be at the start of the code
st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3, gap = "small")
with col1:
    link = 'resources/imgs/site/logo/StarPRO_w_bg.png'
    st.image(link,use_column_width="always")


## adding page background

# def add_bg_from_url():
#     st.markdown(
#             f"""
#             <style>
#             .stApp {{
#                 background-image: url("https://besthqwallpapers.com/Uploads/13-12-2021/187550/4k-black-3d-shards-blue-neon-light-geometric-shapes-creative.jpg");
#                 background-size: cover
#                 background-position: centre
#                 background-repeat: no-repeat
#             }}
#             </style>
#             """,
#             unsafe_allow_html=True
#         )

# add_bg_from_url()

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# Creates a main title and subheader on your page -
# these are static across all pages

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.

    sbar = st.sidebar
    link = 'resources/imgs/site/logo/StarPRO_w_bg.png'
    sbar.image(link,use_column_width="always")
    chk1 = sbar.button("Discover")
    chk2 = sbar.button("Browse")
    chk4 = sbar.button("About the App")
    chk6 = sbar.button("The Team")
    page_options = ["Recommender System","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------

    
    


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    if chk2:
        page_selection = st.radio("",page_options)
        if page_selection == "Recommender System":
            # Header contents
            # Recommender System algorithm selection
            sys = st.radio("Select an algorithm",
                            ('Content Based Filtering',
                            'Collaborative Based Filtering'))

            # User-based preferences
            st.write('### Enter Your Three Favorite Movies')
            movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
            movie_2 = st.selectbox('Second Option',title_list[25055:25255])
            movie_3 = st.selectbox('Third Option',title_list[21100:21200])
            fav_movies = [movie_1,movie_2,movie_3]

            # Perform top-10 movie recommendation generation
            if sys == 'Content Based Filtering':
                if st.button("Recommend"):
                    try:
                        with st.spinner('Crunching the numbers...'):
                            top_recommendations = content_model(movie_list=fav_movies,
                                                                top_n=10)
                        st.title("We think you'll like:")
                        titles = []
                        for i,j in enumerate(top_recommendations):
                            titles.append(str(i+1)+'. '+j)
                        
                        col1, col2, col3, col4, col5 = st.columns(5, gap = "small")
                        with col1:
                            st.write(titles[0])
                        with col2:
                            st.write(titles[1])
                        with col3:
                            st.write(titles[2])
                        with col4:
                            st.write(titles[3])
                        with col5:
                            st.write(titles[4])
                        col6, col7, col8, col9, col10 = st.columns(5, gap = "small")
                        with col6:
                            st.write(titles[5])
                        with col7:
                            st.write(titles[6])
                        with col8:
                            st.write(titles[7])
                        with col9:
                            st.write(titles[8])
                        with col10:
                            st.write(titles[9])
                    except:
                        st.error("Oops! Looks like this algorithm does't work.\
                                    We'll need to fix it!")


            if sys == 'Collaborative Based Filtering':
                if st.button("Recommend"):
                    try:
                        with st.spinner('Crunching the numbers...'):
                            top_recommendations = collab_model(movie_list=fav_movies,
                                                                top_n=10)
                        st.title("We think you'll like:")
                        titles = []
                        for i,j in enumerate(top_recommendations):
                            titles.append(str(i+1)+'. '+j)
                        col1, col2, col3, col4, col5 = st.columns(5, gap = "small")
                        with col1:
                            st.write(titles[0])
                        with col2:
                            st.write(titles[1])
                        with col3:
                            st.write(titles[2])
                        with col4:
                            st.write(titles[3])
                        with col5:
                            st.write(titles[4])
                        col6, col7, col8, col9, col10 = st.columns(5, gap = "small")
                        with col6:
                            st.write(titles[5])
                        with col7:
                            st.write(titles[6])
                        with col8:
                            st.write(titles[7])
                        with col9:
                            st.write(titles[8])
                        with col10:
                            st.write(titles[9])
                        

                    except:
                        st.error("Oops! Looks like this algorithm does't work.\
                                    We'll need to fix it!")
        
        if page_selection == "Solution Overview":
            page_selection = st.radio("",page_options)
            st.title("Solution Overview")
            st.write("Describe your winning approach on this page")


    if chk4:
        st.write('## HOW DOES IT WORK?')
        st.write('Automatic recommendation systems work by following the following general procedure:')
        st.write('1. Identification of similar users or items')
        st.write('2. Prediction of ratings of the items that are not yet rated by a user.')

        st.write('As such, the following questions arise:')
        st.write('* How to determine which users or items are similar to each other,')
        st.write('* How to determine the rating that a user would give to an item based on the rating of similar users (user-based collaborative filtering, or rating given by the user to other items (item-based collaborative filtering),')
        st.write('* How to measure the accuracy of the calculated ratings')
        st.write('## Technics')
        st.write('### 1. Collaborative Filtering')
        st.write('Collaborative filtering works around the interactions that users have with items. To decide usability of collaborative filtering, consider:')
        st.write("1. It doesn't require features about the items or users to be known. Best where item features do not influence choice. Not applicable to items such as books, music or movies.")
        st.write("2. It helps recommenders not overspecialize in a user's profile, and therefore able to recommend items that are completely different from what they have seen before.")
        st.write("3. It suffers from 'cold starts'. Items cannot be recommended to a user unless they are rated.")
        st.write('4. It is affected by data sparsity.')
        st.write('5. Scaling can be a challenge for growing datasets')

        st.write('### 2. Content-based Approach')

        st.write('Focus is on the data provided about the items. The algorithm recommends products that are similar to the ones that a user has liked in the past.')
        st.write('It has the following features:')
        st.write('1. No need for data on other users, and therefore no cold-starts or sparsity problems')
        st.write('2. Ability to recommend to users with unique tasts')
        st.write('3. Ability to recommend new and unpopular items')
        st.write('4. Ability to provide explanations')
        st.write('5. It is hard to find appropriate features')
        st.write("6. Never recommends items outside user's content profile, and unable to exploit quality judgements of other user")

        st.write('### 3. Hybrid Approach')

        st.write('Two or more different recommenders are implemented and the predictions combined.')

    if chk6:
        team_mates = ["Rogers Mugambi", "Denis Titus", "Frank Ayensu","Cosmus Mutuku","Peter Sumani","Emmanuel"]
        roles = ["Project Lead","CFO","Data Lead","Management Lead","Technical Lead","Member"]
        bio = [" ", " ", " ", " ", " "," "]
        image_link = ['resources/imgs/team_pics/Rogers.jpg',
                        'resources/imgs/team_pics/Denis.png',
                        'resources/imgs/team_pics/Frank.png',
                        'resources/imgs/team_pics/Cosmus.png',
                        'resources/imgs/team_pics/Peter.png',
                        'resources/imgs/team_pics/placeHolder.png']
        theTeam = {'people':team_mates,
                    'role':roles,
                    'bio':bio,
                    'imageLink':image_link}
        col1, col2 = st.columns([1,3], gap = "large")
        with col1:
            link1 = theTeam['imageLink'][0]
            st.image(link1,use_column_width="always")
        with col2:
            st.write(f"{theTeam['people'][0]} -- {theTeam['role'][0]}{chr(10)}")
            st.write(theTeam['bio'][0])

        col1, col2 = st.columns([1,3], gap = "large")
        with col1:
            link1 = theTeam['imageLink'][1]
            st.image(link1,use_column_width="always")
        with col2:
            st.write(f"{theTeam['people'][1]} -- {theTeam['role'][1]}{chr(10)}")
            st.write(theTeam['bio'][1])
        
        col1, col2 = st.columns([1,3], gap = "large")
        with col1:
            link1 = theTeam['imageLink'][2]
            st.image(link1,use_column_width="always")
        with col2:
            st.write(f"{theTeam['people'][2]} -- {theTeam['role'][2]}{chr(10)}")
            st.write(theTeam['bio'][2])

        col1, col2 = st.columns([1,3], gap = "large")
        with col1:
            link1 = theTeam['imageLink'][3]
            st.image(link1,use_column_width="always")
        with col2:
            st.write(f"{theTeam['people'][3]} -- {theTeam['role'][3]}{chr(10)}")
            st.write(theTeam['bio'][3])

        col1, col2 = st.columns([1,3], gap = "large")
        with col1:
            link1 = theTeam['imageLink'][4]
            st.image(link1,use_column_width="always")
        with col2:
            st.write(f"{theTeam['people'][4]} -- {theTeam['role'][4]}{chr(10)}")
            st.write(theTeam['bio'][4])

        # col1, col2 = st.columns([1,3], gap = "large")
        # with col1:
        #     link1 = theTeam['imageLink'][5]
        #     st.image(link1,use_column_width="always")
        # with col2:
        #     st.write(f"{theTeam['people'][5]} -- {theTeam['role'][5]}{chr(10)}")
        #     st.write(theTeam['bio'][5])
    #if chk7:

    #if chk8:

    elif chk1:
        # creating columns that will enable 
        # orderly arrangement of movie images
        st.write('## Top Trending')
        col1, col2, col3, col4, col5 = st.columns(5, gap = "small")
        # assigning content to a column
        with col1:
            link = 'resources/imgs/movies/Anythings_Possible.jpg'
            movie_name = "Anythings' Possible"
            release_year = "(2022)"
            avg_rating = "4.5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")

        with col2:
            link = 'resources/imgs/movies/Black Crab.jpg'
            movie_name = "Black Crab"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")

        with col3:
            link = 'resources/imgs/movies/Deep_Water.jpg'
            movie_name = "Deep Water"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")

        with col4:
            link = 'resources/imgs/movies/Halftime.jpg'
            movie_name = "Halftime"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")

        with col5:
            link = 'resources/imgs/movies/Sans_repit.jpg'
            movie_name = "Sans Repit"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")

        col6, col7, col8, col9, col10 = st.columns(5, gap = "small")
        with col6:
            link = 'resources/imgs/movies/Spiderhead.jpg'
            movie_name = "Spiderhead"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")
        with col7:
            link = 'resources/imgs/movies/The_Man_from_Toronto.jpg'
            movie_name = "The Man from Toronto"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")
        with col8:
            link = 'resources/imgs/movies/The_Sea_Beast.png'
            movie_name = "The Sea Beast"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")
        with col9:
            link = 'resources/imgs/movies/Tinder_swindler.jpg'
            movie_name = "Tinder Swindler"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")
        with col10:
            link = 'resources/imgs/movies/Interceptor.jpg'
            movie_name = "Interceptor"
            release_year = "(2022)"
            avg_rating = "5"
            #st.header("Movie 1")
            new_line = '\n'
            caption = f"{movie_name} {release_year} {chr(10)} Rating: {avg_rating}"
            st.image(link,caption,use_column_width="always")


    page_options = ["None","Recommender System","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox(" ",page_options)
    if page_selection == "None":
        st.write(" ")

    if page_selection == "Recommender System":
        # Header contents
        # Recommender System algorithm selection
        st.write('Want to see a great movie?')
        sys = st.radio("Select an algorithm",
                    ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write(' Enter Your Favorite Movie')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        fav_movies = movie_1

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    titles = []
                    for i,j in enumerate(top_recommendations):
                        titles.append(str(i+1)+'. '+j)
                    
                    col1, col2, col3, col4, col5 = st.columns(5, gap = "small")
                    with col1:
                        st.write(titles[0])
                    with col2:
                        st.write(titles[1])
                    with col3:
                        st.write(titles[2])
                    with col4:
                        st.write(titles[3])
                    with col5:
                        st.write(titles[4])
                    col6, col7, col8, col9, col10 = st.columns(5, gap = "small")
                    with col6:
                        st.write(titles[5])
                    with col7:
                        st.write(titles[6])
                    with col8:
                        st.write(titles[7])
                    with col9:
                        st.write(titles[8])
                    with col10:
                        st.write(titles[9])
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                            We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                            We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")


if __name__ == '__main__':
    main()
