# 🎬 Movie Recommender System

## 📖 Overview
A **Content-Based Movie Recommender System** built with Streamlit that suggests movies similar to your selection. The system uses **TF-IDF Vectorization** and **Cosine Similarity** to find the most similar movies from a dataset of 5000+ movies.


---

## ✨ Features
- 🎥 **Movie Selection** - Choose from 5000+ movies
- 🔍 **Smart Recommendations** - Finds top 5 similar movies using content-based filtering
- 🖼️ **Movie Posters** - Displays posters for recommended movies via TMDB API
- 📊 **Similarity Score** - Shows confidence level of each recommendation
- 🎨 **Clean UI** - User-friendly interface with sidebar information


---

## 🛠️ Technologies Used
- **Python 3.10+** - Core programming language
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation
- **NumPy** - Numerical operations
- **Scikit-learn** - TF-IDF Vectorization, Cosine Similarity
- **NLTK** - Text preprocessing (stemming)
- **TMDB API** - Fetching movie posters


---

## 📁 Project Structure
```
movie-recommender/
├── app.py # Main Streamlit application (UI)
├── recommend.py # Recommendation functions
├── data_preprocessing.py # Data preparation script
├── requirements.txt # Python dependencies
├── setup.sh # Setup script
├── .gitignore # Git ignore file
├── data/ # Raw CSV files (gitignored)
│ ├── tmdb_5000_movies.csv
│ └── tmdb_5000_credits.csv
├── processed_data/ # Generated pickle files (gitignored)
│ ├── movies_list.pkl
│ └── similarity.pkl
└── README.md # Project documentation
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/anjalitarkar101/movie-recommender-system.git
cd movie-recommender
```

### Step 2: Run Setup Script

```bash
chmod +x setup.sh
./setup.sh
```

This will:
- Create required directories (data/, processed_data/, uploads/)
- Install all dependencies

### Step 3: Download Dataset
- **Source:** Kaggle
- **Link:** https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
- **Name:** TMDB 5000 Movie Dataset
- **Creator:** The Movie Database (TMDb)
- **Files:** tmdb_5000_movies.csv, tmdb_5000_credits.csv
- **Rows:** 5,000+ movies

After downloading, place the CSV files in the `data/` folder:
```
data/
├── tmdb_5000_movies.csv
└── tmdb_5000_credits.csv
```

### Step 4: Preprocess Data
``` bash
python data_preprocessing.py
```
This will:
- Load both CSV files and merge them on movie ID
- Extract genres, keywords, cast, and crew from JSON
- Create a combined tags column
- Apply stemming using Porter Stemmer
- Generate TF-IDF feature vectors
- Compute Cosine Similarity matrix
- Save processed data to processed_data/ folder


### Step 5: Run the Application
```bash
streamlit run app.py
Open your browser and navigate to http://localhost:8501
```

---

## 📊 How It Works
1. Data Preprocessing
   - Loads movie metadata and credits
   - Extracts genres, keywords, cast, crew, and overview
   - Creates a combined tags column
   - Applies stemming using Porter Stemmer
   - Converts text to feature vectors using TF-IDF

2. Similarity Calculation
   - Calculates Cosine Similarity between all movies
   - Creates a similarity matrix

3. Recommendation
   - User selects a movie
   - System finds the top 5 most similar movies
   - Fetches movie posters using TMDB API
   - Displays recommendations with posters


---

## 🔧 Dependencies

```txt
streamlit==1.28.0
pandas==2.0.3
numpy==1.24.3
requests==2.31.0
nltk==3.8.1
scikit-learn==1.3.0
```


---

## 🎯 API Key Setup
To use your own TMDB API key:
1. Sign up at https://www.themoviedb.org/signup
2. Get your API key from Settings -> API
3. Update TMDB_API_KEY in recommend.py


---

## 📝 Usage Guide
1. Select a movie from the dropdown menu
2. Click Show Recommendations
3. View the top 5 similar movies with posters
4. Explore different movies to discover new recommendations


---

## 📊 Dataset Information

### tmdb_5000_movies.csv

| Column | Type | Description |
|--------|------|-------------|
| budget | Numerical | Movie budget in dollars |
| genres | Categorical | Genre categories (JSON format) |
| homepage | Text | Official movie homepage URL |
| id | Numerical | Unique movie identifier |
| keywords | Text | Movie keywords (JSON format) |
| original_language | Categorical | Original language code |
| original_title | Text | Original movie title |
| overview | Text | Movie plot summary |
| popularity | Numerical | Popularity score |
| production_companies | Text | Production companies (JSON format) |
| production_countries | Text | Production countries (JSON format) |
| release_date | Date | Movie release date |
| revenue | Numerical | Movie revenue in dollars |
| runtime | Numerical | Movie duration in minutes |
| spoken_languages | Text | Languages spoken (JSON format) |
| status | Categorical | Movie status (Released, Post-Production, etc.) |
| tagline | Text | Movie tagline |
| title | Text | Movie title |
| vote_average | Numerical | Average user rating (0-10) |
| vote_count | Numerical | Number of votes |

### tmdb_5000_credits.csv

| Column | Type | Description |
|--------|------|-------------|
| movie_id | Numerical | Unique movie identifier |
| title | Text | Movie title |
| cast | Text | Cast information (JSON format) |
| crew | Text | Crew information (JSON format) |

---


## 📄 License

This project is licensed under the MIT License.

© 2026 Anjali Tarkar. All rights reserved.


---

## 👩‍💻 Author
**Anjali Tarkar**
- GitHub: https://github.com/anjalitarkar101
- Email: anjalitarkar101@gmail.com


---

## ⭐ Show Your Support
If you find this project useful, please give it a star on GitHub!


---

## 🙏 Acknowledgments
- The Movie Database (TMDb) - For providing the API and dataset
- Streamlit - For the awesome web framework

