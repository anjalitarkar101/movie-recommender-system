# ==========================================
# app.py - Movie Recommender System
# ==========================================

import streamlit as st
from recommend import load_data, get_recommendations

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Sidebar
# ==========================================

with st.sidebar:
    st.markdown("### 🎭 About This App")
    st.markdown("""
        This app recommends movies based on content similarity.

        **How it works:**
        1. 🎬 Select a movie you like
        2. 🔍 AI analyzes movie features
        3. 🎯 Finds similar movies
        4. ⭐ Shows top 5 recommendations
    """)

    st.markdown("---")

    st.markdown("### 🧠 Model Info")
    st.markdown("""
        - **Algorithm:** Cosine Similarity
        - **Features:** 5000 (TF-IDF)
        - **Recommendations:** 5 Movies
        - **Data Source:** TMDB 5000
    """)

# ==========================================
# Main Content
# ==========================================

st.title("🎬 Movie Recommender System")
st.markdown("Select a movie to get personalized recommendations!")

# Load data using the function from recommend.py
movies_data, similarity_matrix = load_data()

if movies_data is None or similarity_matrix is None:
    st.error("❌ Data files not found! Please run: python data_preprocessing.py")
    st.stop()

st.success(f"✅ Loaded {len(movies_data)} movies successfully!")

# ==========================================
# Movie Selection
# ==========================================

st.markdown("---")

movie_list = movies_data['title'].values

selected_movie = st.selectbox(
    "🎬 Select a movie you like:",
    movie_list,
    help="Type to search or select from the dropdown"
)

# ==========================================
# Show Recommendations
# ==========================================

if st.button("🔮 Show Recommendations", type="primary"):
    with st.spinner("🔍 Finding similar movies..."):
        recommended_movie_names, recommended_movie_posters = get_recommendations(
            selected_movie,
            movies_data,
            similarity_matrix
        )

    if recommended_movie_names:
        st.subheader("⭐ Movies You Might Also Like")
        st.markdown("---")

        cols = st.columns(5)

        for idx, col in enumerate(cols):
            if idx < len(recommended_movie_names):
                with col:
                    st.image(recommended_movie_posters[idx], width=150)

                    movie_name = recommended_movie_names[idx]
                    if len(movie_name) > 18:
                        movie_name = movie_name[:16] + "..."
                    st.markdown(f"**{movie_name}**")
                    st.caption(f"#{idx + 1}")
            else:
                with col:
                    st.image(
                        "https://via.placeholder.com/150x225?text=No+Movie",
                        width=150
                    )
                    st.caption("No more")
    else:
        st.warning("No recommendations found. Please try another movie.")

# ==========================================
# Footer
# ==========================================

st.markdown("---")
st.caption("🎥 Powered by Content-Based Filtering | Data from TMDB")