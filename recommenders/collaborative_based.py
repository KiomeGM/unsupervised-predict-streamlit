"""

    Collaborative-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `collab_model` !!

    You must however change its contents (i.e. add your own collaborative
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline collaborative
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import pandas as pd
import numpy as np
import pickle
import copy
from surprise import Reader, Dataset
from surprise import SVD, NormalPredictor, BaselineOnly, KNNBasic, NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Importing data
movies = pd.read_csv('resources/data/movies.csv',sep = ',')
imdb_data = pd.read_csv('resources/data/imdb_data.csv')

# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
#model=pickle.load(open('resources/models/content_based.pkl', 'rb'))

df = imdb_data[['movieId','title_cast', 'plot_keywords']]
df = df.merge(movies[['movieId', 'genres', 'title']], on='movieId', how='inner')

# Convert data types to strings for string handling
df['title_cast'] = df.title_cast.astype(str)
df['plot_keywords'] = df.plot_keywords.astype(str)
df['genres'] = df.genres.astype(str)
#df['director'] = df.director.astype(str)

# Removing spaces between names
#df['director'] = df['director'].apply(lambda x: "".join(x.lower() for x in x.split()))
df['title_cast'] = df['title_cast'].apply(lambda x: "".join(x.lower() for x in x.split()))
# Discarding the pipes between the actors' full names and getting only the first four names
df['title_cast'] = df['title_cast'].map(lambda x: x.split('|')[:4])
# Discarding the pipes between the plot keywords' and getting only the first five words
df['plot_keywords'] = df['plot_keywords'].map(lambda x: x.split('|')[:5])
df['plot_keywords'] = df['plot_keywords'].apply(lambda x: " ".join(x))
# Discarding the pipes between the genres 
df['genres'] = df['genres'].map(lambda x: x.lower().split('|'))
df['genres'] = df['genres'].apply(lambda x: " ".join(x))

df2=df.copy()
df2["title_cast"]= df2["title_cast"].str.join(' ')

"""
creating a corpus
"""
# Creating an empty column and list to store the corpus for each movie
df2['corpus'] = ''
corpus = []
# List of the columns we want to use to create our corpus 
columns = ['title_cast', 'plot_keywords', 'genres']
# For each movie, combine the contents of the selected columns to form it's unique corpus 
for i in range(0, len(df2['movieId'])):
    words = ''
    for col in columns:
        words = words + df2.loc[i][col] + " "        
    corpus.append(words)
# Add the corpus information for each movie to the dataframe 
df2['corpus'] = corpus
df2.set_index('movieId', inplace=True)
# Drop the columns we don't need anymore to preserve memory
df2.drop(columns=['title_cast', 'plot_keywords', 'genres'], inplace=True)

"""
generating similarity values
"""
cv = CountVectorizer()
count_matrix = cv.fit_transform(df2['corpus'])
#cosine similarities
cos_sim = cosine_similarity(count_matrix, count_matrix)

# Get list of prediction


def get_topN_recommendations(title, n=10):
    """
    This function gets the top n recomended movies based on the 
    title of the movie input by the user 
    
    Input: title
           Datatype: str
           
           n (default = 10)
           Datatype: int
    """ 
    # Create a a copy of the input dataframe where the index has been reset
    df1 = df2.reset_index()
    
    # Extract the movie titles
    titles = df1['title']
    indices = pd.Series(df1.index, index=df['title'])
    idx = indices[title]
    
    # Get the similarity scores of the top n movies most similar to the user input
    sim_scores = list(enumerate(cos_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n]
    
    # Exctract the titles of the top n most similar movies  
    movie_indices = [i[0] for i in sim_scores]
    
    return titles.iloc[movie_indices]

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def collab_model(movie_list):
    """Performs Collaborative filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """
    # loaded_model = pickle.load(open(filename, 'rb'))
    # recommended_movies = loaded_model('Ice Age (2002)')

    recommended_movies = get_topN_recommendations(movie_list, n=10)


    return recommended_movies
