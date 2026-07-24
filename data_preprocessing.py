# ==================================================
# data_preprocessing.py - Movie Recommender System
# ===================================================

import pandas as pd
import numpy as np
import pickle
import ast
import os
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 1. LOAD AND MERGE DATASETS
# ==========================================

print("=" * 60)
print("🎬 MOVIE RECOMMENDER - DATA PREPROCESSING")
print("=" * 60)

print("\n📥 Loading datasets...")

# Load datasets
movies = pd.read_csv('data/tmdb_5000_movies.csv')
credits = pd.read_csv('data/tmdb_5000_credits.csv')

print(f"📊 Movies dataset shape: {movies.shape}")
print(f"📊 Credits dataset shape: {credits.shape}")

# Merge both dataframes
my_data = movies.merge(credits, on='title')
print(f"📊 Merged dataset shape: {my_data.shape}")

# ==========================================
# 2. DATA PREPROCESSING
# ==========================================

print("\n🔄 Preprocessing data...")

# Keep only required columns
required_data = my_data[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

# Remove rows with missing values in overview column
required_data = required_data.dropna()

print(f"📊 After cleaning - Shape: {required_data.shape}")

# ==========================================
# 3. CONVERT COLUMNS TO LISTS
# ==========================================

print("\n🔄 Converting columns to lists...")

def convert_genres(obj):
    """Convert genres string to list of genre names."""
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

def convert_keywords(obj):
    """Convert keywords string to list of keyword names."""
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

def convert_cast(obj):
    """Convert cast string to list of top 3 cast names."""
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L

def convert_crew(obj):
    """Convert crew string to list of director names."""
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

# Apply conversions
required_data['genres'] = required_data['genres'].apply(convert_genres)
required_data['keywords'] = required_data['keywords'].apply(convert_keywords)
required_data['cast'] = required_data['cast'].apply(convert_cast)
required_data['crew'] = required_data['crew'].apply(convert_crew)

# Convert overview to list of words
required_data['overview'] = required_data['overview'].apply(lambda x: x.split())

print("✅ Column conversions complete!")

# ==========================================
# 4. REMOVE SPACES AND CREATE TAGS
# ==========================================

print("\n🔄 Creating tags...")

# Remove spaces from all columns
required_data['genres'] = required_data['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
required_data['keywords'] = required_data['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
required_data['cast'] = required_data['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
required_data['crew'] = required_data['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

# Create tags column by concatenating all lists
required_data['tags'] = required_data['overview'] + required_data['genres'] + required_data['keywords'] + required_data['cast'] + required_data['crew']

# Keep only required columns
required_data = required_data[['movie_id', 'title', 'tags']]

# Convert tags list to single string
required_data['tags'] = required_data['tags'].apply(lambda x: " ".join(x))

# Convert to lowercase
required_data['tags'] = required_data['tags'].apply(lambda x: x.lower())

print("✅ Tags created!")

# ==========================================
# 5. STEMMING
# ==========================================

print("\n🔄 Applying stemming...")

ps = PorterStemmer()

def stem(text):
    """Apply stemming to text."""
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

required_data['tags'] = required_data['tags'].apply(stem)

print("✅ Stemming complete!")

# ==========================================
# 6. TEXT VECTORIZATION
# ==========================================

print("\n🔄 Creating feature vectors...")

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(required_data['tags']).toarray()

print(f"📊 Feature vectors shape: {vectors.shape}")

# ==========================================
# 7. CALCULATE SIMILARITY
# ==========================================

print("\n🔄 Calculating similarity matrix...")

similarity = cosine_similarity(vectors)

print(f"📊 Similarity matrix shape: {similarity.shape}")

# ==========================================
# 8. SAVE PICKLE FILES
# ==========================================

print("\n💾 Saving pickle files...")


# Save movies list
with open('processed_data/movies_list.pkl', 'wb') as f:
    pickle.dump(required_data, f)
print("💾 Saved: processed_data/movies_list.pkl")

# Save similarity matrix
with open('processed_data/similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)
print("💾 Saved: processed_data/similarity.pkl")

# ==========================================
# 9. SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("✅ DATA PREPROCESSING COMPLETE!")
print("=" * 60)
print(f"📊 Total movies: {len(required_data)}")
print(f"📊 Feature vectors: {vectors.shape}")
print(f"📊 Similarity matrix: {similarity.shape}")
print("\n📌 Next step: Run 'streamlit run app.py'")
print("=" * 60)