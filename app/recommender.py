import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
def load_data():
    data = pd.read_csv('data/synthetic_movie_data.csv')
    return data

# Create user-item matrix
def create_user_item_matrix(data):
    user_item_matrix = data.pivot_table(index='user_id', columns='movie_title', values='rating', fill_value=0)
    return user_item_matrix

# Train SVD model for collaborative filtering
def train_svd(user_item_matrix, n_components=5):
    svd = TruncatedSVD(n_components=n_components)
    svd_matrix = svd.fit_transform(user_item_matrix)
    return svd, svd_matrix

# Make movie recommendations for a user
def recommend_movies(user_id, svd, svd_matrix, user_item_matrix):
    user_index = user_id - 1  # user_id starts from 1
    user_svd_vector = svd_matrix[user_index]
    
    # Compute similarity scores for all movies
    movie_similarity = cosine_similarity([user_svd_vector], svd_matrix)
    
    # Get the indices of the most similar movies
    similar_movie_indices = movie_similarity.argsort()[0][::-1]
    
    recommended_movies = []
    for idx in similar_movie_indices[:5]:
        movie = user_item_matrix.columns[idx]
        recommended_movies.append(movie)
    
    return recommended_movies

# Example: Main function
def main(user_id):
    data = load_data()
    user_item_matrix = create_user_item_matrix(data)
    svd, svd_matrix = train_svd(user_item_matrix)
    recommended_movie_titles = recommend_movies(user_id, svd, svd_matrix, user_item_matrix)
    return recommended_movie_titles
