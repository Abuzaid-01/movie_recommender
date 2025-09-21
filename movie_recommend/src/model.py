import pickle
import pandas as pd
import os

# Get the current directory and construct paths relative to the script location
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, '..', 'data')

try:
    # Load movie data
    with open(os.path.join(data_dir, "movie_list.pkl"), "rb") as f:
        movies = pickle.load(f)
    
    # Load similarity matrix
    with open(os.path.join(data_dir, "similarity.pkl"), "rb") as f:
        similarity = pickle.load(f)
        
    print(f"✅ Loaded {len(movies)} movies successfully!")
    
except FileNotFoundError as e:
    print(f"❌ Error: Could not find data files. Make sure movie_list.pkl and similarity.pkl exist in the data directory.")
    raise e
except Exception as e:
    print(f"❌ Error loading data: {str(e)}")
    raise e

def recommend(movie_title):
    """
    Recommend similar movies based on content similarity.
    
    Args:
        movie_title (str): The title of the movie to base recommendations on
        
    Returns:
        list: List of 5 recommended movie titles
        
    Raises:
        ValueError: If the movie is not found in the dataset
        Exception: If there's an error in the recommendation process
    """
    try:
        # Check if movie exists in the dataset
        movie_matches = movies[movies['title'] == movie_title]
        if movie_matches.empty:
            raise ValueError(f"Movie '{movie_title}' not found in the database.")
        
        # Find index of the selected movie
        movie_index = movie_matches.index[0]
        
        # Get similarity scores
        distances = similarity[movie_index]
        
        # Get top 5 similar movies (excluding itself)
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        # Fetch movie titles
        recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
        
        return recommended_movies
        
    except ValueError:
        # Re-raise ValueError with the same message
        raise
    except IndexError as e:
        raise Exception(f"Error accessing movie data: {str(e)}")
    except Exception as e:
        raise Exception(f"Unexpected error during recommendation: {str(e)}")

def get_movie_details(movie_title):
    """
    Get additional details about a movie if available.
    
    Args:
        movie_title (str): The title of the movie
        
    Returns:
        dict: Dictionary containing movie details
    """
    try:
        movie_info = movies[movies['title'] == movie_title]
        if movie_info.empty:
            return {}
            
        details = {'title': movie_title}
        
        # Add available columns to details
        for col in ['genre', 'overview', 'release_date', 'vote_average']:
            if col in movie_info.columns:
                details[col] = movie_info[col].iloc[0]
                
        return details
        
    except Exception as e:
        print(f"Error getting movie details: {str(e)}")
        return {'title': movie_title}

def get_random_movies(n=10):
    """
    Get a random sample of movies for suggestions.
    
    Args:
        n (int): Number of random movies to return
        
    Returns:
        list: List of random movie titles
    """
    try:
        return movies['title'].sample(n=min(n, len(movies))).tolist()
    except Exception as e:
        print(f"Error getting random movies: {str(e)}")
        return movies['title'].head(n).tolist()
