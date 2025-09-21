import streamlit as st
import pandas as pd
from src.model import recommend, movies

# Configure the page
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="auto"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .movie-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #ff6b6b;
    }
    .movie-title {
        font-size: 1.1rem;
        font-weight: bold;
        color: #2c3e50;
    }
    .recommendation-header {
        text-align: center;
        color: #2c3e50;
        padding: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main title with emoji
st.markdown('<h1 style="text-align: center; color: #2c3e50;">🎬 Movie Recommendation System</h1>', unsafe_allow_html=True)

# Add description
st.markdown("""
<p style="text-align: center; color: #7f8c8d; font-size: 1.1rem;">
    Discover your next favorite movie! Select a movie you like and get personalized recommendations.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Create two columns for better layout
col1, col2 = st.columns([3, 1])

with col1:
    # Movie selection with search functionality
    movie_list = sorted(movies['title'].values)
    selected_movie = st.selectbox(
        "🔍 Choose a movie you like:",
        options=movie_list,
        help="Start typing to search for a movie"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)  # Add spacing
    recommend_button = st.button("🎯 Get Recommendations", type="primary")

# Add some space
st.markdown("<br>", unsafe_allow_html=True)

# Show movie details
if selected_movie:
    movie_info = movies[movies['title'] == selected_movie]
    if not movie_info.empty:
        with st.expander("📋 Selected Movie Details", expanded=False):
            if 'genre' in movie_info.columns:
                st.write(f"**Genre:** {movie_info['genre'].iloc[0]}")
            if 'overview' in movie_info.columns:
                st.write(f"**Overview:** {movie_info['overview'].iloc[0]}")

# Recommendation logic
if recommend_button and selected_movie:
    try:
        with st.spinner("🔄 Finding similar movies..."):
            recommendations = recommend(selected_movie)
        
        st.markdown('<div class="recommendation-header"><h2>🎭 Movies You Might Like</h2></div>', unsafe_allow_html=True)
        
        # Display recommendations in an attractive format
        for i, movie in enumerate(recommendations, 1):
            st.markdown(f"""
            <div class="movie-card">
                <div class="movie-title">{i}. {movie}</div>
            </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"❌ Sorry, we couldn't find recommendations for '{selected_movie}'. Please try another movie.")
        st.error(f"Error details: {str(e)}")

elif recommend_button and not selected_movie:
    st.warning("⚠️ Please select a movie first!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d; padding: 1rem;">
    <p>💡 <strong>How it works:</strong> Our system uses content-based filtering to find movies similar to your selection.</p>
    <p>🎯 The more specific your movie choice, the better your recommendations will be!</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with additional info
with st.sidebar:
    st.markdown("### 📊 Dataset Info")
    st.info(f"**Total Movies:** {len(movies)}")
    
    st.markdown("### 🛠️ About")
    st.markdown("""
    This recommendation system uses machine learning to suggest movies based on:
    - Genre similarity
    - Plot keywords
    - Cast and crew
    - User ratings
    """)
    
    st.markdown("### � Tips")
    st.markdown("""
    - Try different genres for varied recommendations
    - Popular movies tend to have better recommendations
    - Scroll through the list or type to search
    """)
