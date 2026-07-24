# ==============================================
# recommend.py - Movie Recommender System
# ==============================================

import requests
import pickle
import streamlit as st

# ==========================================
# TMDB API Configuration
# ==========================================

TMDB_API_KEY = "c0024873141c552f8126334ab5b6e0c9"
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# ==========================================
# 1. Load Data Function
# ==========================================

@st.cache_data
def load_data():
    """
    Load movies and similarity data from processed_data folder.

    Returns:
        tuple: (movies_data, similarity_matrix)
    """
    try:
        movies = pickle.load(open('processed_data/movies_list.pkl', 'rb'))
        similarity = pickle.load(open('processed_data/similarity.pkl', 'rb'))
        return movies, similarity
    except FileNotFoundError:
        return None, None


# ==========================================
# 2. Poster Fetching Function
# ==========================================

@st.cache_data
def fetch_poster(movie_id):
    """
    Fetch movie poster from TMDB API.

    Args:
        movie_id: TMDB movie ID

    Returns:
        Poster URL or placeholder URL
    """
    url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return TMDB_IMAGE_URL + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    except Exception as e:
        print(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"


# ==========================================
# 3. Recommendation Function
# ==========================================

def get_recommendations(movie, movies_data, similarity_matrix):
    """
    Get movie recommendations based on similarity.

    Args:
        movie: Selected movie title
        movies_data: DataFrame with movie data
        similarity_matrix: Similarity matrix

    Returns:
        tuple: (recommended_movie_names, recommended_movie_posters)
    """
    try:
        movie_index = movies_data[movies_data['title'] == movie].index[0]

        distances = sorted(
            list(enumerate(similarity_matrix[movie_index])),
            reverse=True,
            key=lambda x: x[1]
        )

        recommended_movie_names = []
        recommended_movie_posters = []

        # Get top 5 similar movies
        for i in distances[1:6]:
            movie_id = movies_data.iloc[i[0]].movie_id
            poster_url = fetch_poster(movie_id)  # ← Calls fetch_poster

            recommended_movie_posters.append(poster_url)
            recommended_movie_names.append(movies_data.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters

    except Exception as e:
        print(f"Error getting recommendations: {e}")
        return [], []