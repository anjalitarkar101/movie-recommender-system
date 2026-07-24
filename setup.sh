#!/bin/bash
# setup.sh - Movie Recommender System Setup

echo "=========================================="
echo "🎬 Movie Recommender System Setup"
echo "=========================================="

# Create directories
echo "📁 Creating directories..."
mkdir -p data processed_data

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Download NLTK data
echo "📥 Downloading NLTK data..."
python -c "import nltk; nltk.download('punkt')"

echo ""
echo "=========================================="
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Place CSV files in 'data' folder:"
echo "   - tmdb_5000_movies.csv"
echo "   - tmdb_5000_credits.csv"
echo ""
echo "2. Preprocess data: python data_preprocessing.py"
echo ""
echo "3. Run the app: streamlit run app.py"
echo "=========================================="