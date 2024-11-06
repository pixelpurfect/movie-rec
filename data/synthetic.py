import pandas as pd
import random
import numpy as np

# Set random seed for reproducibility
random.seed(42)

# Movie Data
movie_titles = [
    "The Matrix", "Inception", "The Dark Knight", "Pulp Fiction", "The Shawshank Redemption",
    "Forrest Gump", "The Godfather", "Fight Club", "The Lord of the Rings", "The Avengers",
    "The Lion King", "Titanic", "Star Wars", "Jurassic Park", "The Godfather Part II",
    "Back to the Future", "Gladiator", "The Prestige", "The Departed", "Schindler's List"
]

genres = ['Action', 'Adventure', 'Sci-Fi', 'Drama', 'Comedy', 'Thriller', 'Crime', 'Animation', 'Fantasy']

# Users (user_id, age, gender, location)
user_demographics = [
    {'user_id': 1, 'age': 24, 'gender': 'M', 'location': 'USA'},
    {'user_id': 2, 'age': 35, 'gender': 'F', 'location': 'UK'},
    {'user_id': 3, 'age': 28, 'gender': 'M', 'location': 'India'},
    {'user_id': 4, 'age': 40, 'gender': 'F', 'location': 'Canada'},
    {'user_id': 5, 'age': 18, 'gender': 'M', 'location': 'Australia'},
    # Add more users as needed
]

# Movie Ratings (random ratings between 1 and 5)
ratings = []
for user in user_demographics:
    for i, movie in enumerate(movie_titles):
        rating = random.randint(1, 5)
        ratings.append({'user_id': user['user_id'], 'movie_title': movie, 'rating': rating, 'genre': random.choice(genres)})

# Create a DataFrame for movie ratings
ratings_df = pd.DataFrame(ratings)

# Create movie data DataFrame
movies_df = pd.DataFrame({
    'movie_id': [i+1 for i in range(len(movie_titles))],
    'movie_title': movie_titles,
    'genre': [random.choice(genres) for _ in range(len(movie_titles))]
})

# Merge movie data with ratings
data = pd.merge(ratings_df, movies_df, on='movie_title')

# Save as CSV
data.to_csv('data/synthetic_movie_data.csv', index=False)
