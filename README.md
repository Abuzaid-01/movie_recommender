# 🎬 Movie Recommendation System

A modern, user-friendly movie recommendation system built with **Streamlit** and **Machine Learning**. Get personalized movie recommendations based on content similarity using advanced algorithms.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39.0-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ Features

- **🎯 Intelligent Recommendations**: Content-based filtering algorithm
- **🔍 Smart Search**: Type to search through thousands of movies
- **📱 Responsive Design**: Works on desktop and mobile devices
- **⚡ Fast Performance**: Optimized for quick recommendations
- **🎨 Beautiful UI**: Modern, intuitive interface
- **☁️ Cloud Ready**: Optimized for Streamlit Cloud deployment

## 🚀 Quick Start

### Option 1: Streamlit Cloud (Recommended)

1. **Fork this repository** on GitHub
2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**
3. **Connect your GitHub account** and select this repository
4. **Deploy with one click** - Streamlit Cloud will handle everything!

### Option 2: Local Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd movie_recommend
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 🏗️ Project Structure

```
movie_recommend/
├── app.py                    # Main Streamlit application (root level for cloud)
├── movie_recommend/          # Application modules
│   ├── app.py               # Original app (for local development)
│   ├── src/                 # Source code modules
│   │   ├── __init__.py
│   │   ├── model.py         # ML model and recommendation logic
│   │   └── utils.py         # Utility functions
│   └── data/                # Data files
│       ├── movie_list.pkl   # Movie dataset
│       └── similarity.pkl   # Precomputed similarity matrix
├── .streamlit/              # Streamlit configuration
│   ├── config.toml         # App configuration
│   └── secrets.toml        # Secrets template
├── requirements.txt         # Python dependencies (minimal)
├── .gitignore              # Git ignore patterns
└── README.md               # This file
```

## 🛠️ How It Works

The recommendation system uses **Content-Based Filtering**:

1. **Feature Extraction**: Movies are analyzed based on:
   - Genre information
   - Plot keywords and descriptions
   - Cast and crew details
   - User ratings and metadata

2. **Similarity Calculation**: Uses cosine similarity to measure how similar movies are to each other

3. **Recommendation Generation**: When you select a movie, the system finds the top 5 most similar movies

4. **Real-time Results**: Recommendations are generated instantly using precomputed similarity matrices

## 📊 Dataset Information

- **Total Movies**: 4,800+ movies
- **Features**: Genre, keywords, cast, crew, ratings
- **Similarity Matrix**: Precomputed for optimal performance
- **Data Sources**: Processed and cleaned movie metadata

## ☁️ Streamlit Cloud Deployment

### Step-by-Step Guide:

1. **Fork this repository** to your GitHub account

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Click "New app"**

4. **Connect your GitHub** and select this repository

5. **Configure deployment:**
   - **Repository**: `your-username/movie_recommend`
   - **Branch**: `main` (or `master`)
   - **Main file path**: `app.py`

6. **Click "Deploy"** - Your app will be live in minutes!

### Configuration Files:

- **`.streamlit/config.toml`**: App theme and server settings
- **`requirements.txt`**: Only 3 essential dependencies
- **`app.py`**: Main application file at root level

## 🔧 Local Development

### Environment Setup:
```bash
# Clone and setup
git clone <your-repo-url>
cd movie_recommend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

### Testing:
```bash
# Test the recommendation function
python -c "from movie_recommend.src.model import recommend; print(recommend('The Dark Knight'))"

# Run the app
streamlit run app.py --server.port 8502  # Use different port if needed
```

## 🐛 Troubleshooting

### Common Issues:

1. **"Module not found" error**
   - Ensure you're in the correct directory
   - Activate your virtual environment

2. **Data files not found**
   - Check that `movie_list.pkl` and `similarity.pkl` exist in `movie_recommend/data/`

3. **Streamlit Cloud deployment fails**
   - Check `requirements.txt` for correct package versions
   - Ensure `app.py` is at the root level
   - Verify all data files are committed to GitHub

4. **Performance issues**
   - Large pickle files may take time to load initially
   - Consider using Git LFS for large data files

5. **Similarity matrix missing**
   - The `similarity.pkl` file (176MB) is not included in the repository due to GitHub size limits
   - Run `python generate_similarity.py` to create it locally
   - For Streamlit Cloud: the app will auto-generate this file on first run

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📈 Future Enhancements

- [ ] **Collaborative Filtering**: Add user-based recommendations
- [ ] **Movie Posters**: Integrate with TMDB API for poster images
- [ ] **User Ratings**: Allow users to rate movies
- [ ] **Search Filters**: Add genre, year, and rating filters
- [ ] **Recommendation History**: Track user's previous searches
- [ ] **Similar Users**: Find users with similar tastes
- [ ] **Advanced ML**: Implement deep learning models

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit** - For the amazing web framework
- **Scikit-learn** - For machine learning algorithms
- **Pandas** - For data manipulation
- **TMDB** - For movie dataset inspiration

---

**🎬 Made with ❤️ for movie lovers**

**🌟 [Live Demo on Streamlit Cloud](your-app-url-here)**

If you found this project helpful, please ⭐ star the repository!
