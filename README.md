# 🎬 Movie Blockbuster Prediction

- A Machine Learning based web application that predicts whether a movie will become a Blockbuster or Not using movie features.

# 🚀 Project Overview

- This project uses Data Analysis, Feature Engineering, Machine Learning and NLP techniques to analyze a large movie dataset and build predictive models.

- The model is trained on the TMDB Movies Dataset and deployed using Streamlit for real-time predictions.

# 🛠 Technologies Used

- Python

- Pandas

- NumPy

- Seaborn

- Matplotlib

- Scikit-learn

- Streamlit

- Pickle

- TF-IDF (NLP)

# 🤖 Machine Learning Models Used

- Linear Regression

- Random Forest Regressor

- Random Forest Classifier

- K-Means Clustering

- TF-IDF Vectorizer (NLP)

# 📊 Dataset Details

- **Dataset**: TMDB Movies Dataset

- **Source**: Kaggle

- **Problem Types**:

  **Regression**:
  - Predict Movie Revenue
  - Predict Movie Rating

**Classification** → Predict Blockbuster Movies

**Unsupervised Learning** → Movie Clustering

**NLP** → Text Analysis on Movie Overview

# 🔍 Methodology
## 1️⃣ Data Cleaning

- Removed duplicate movies

- Converted release date to datetime format

- Removed movies with invalid revenue

- Handled missing runtime values

- Dropped unnecessary columns

## 2️⃣ Feature Engineering

### Extracted:

- Year

- Month

- Weekday

- Decade

### Split categorical columns:

- Genres

- Production Companies

- Production Countries

- Spoken Languages

- Keywords

## 3️⃣ Exploratory Data Analysis (EDA)

- Movies released per year

- Revenue growth over time

- Top revenue generating movies

- Revenue distribution

- Genre analysis

- Country production analysis

- Language popularity

- Seasonality trends

# 📸 Project Screenshots
![image alt](https://github.com/Sankesh12/Movie-Blockbuster-Prediction/blob/a11f26b5a880be30e389f57e4a843baa96d531bc/movie1.png)

# 📈 Model Evaluation

## Evaluation Metrics Used:

- R2 Score

- Mean Absolute Error (MAE)

- Root Mean Squared Error (RMSE)

- Accuracy (for classification)

# 🏆 Machine Learning Tasks

## 1. Revenue Prediction

### Predict movie box office revenue using features like:

- Runtime

- Popularity

- Vote Count

- Vote Average

- Release Year

- Release Month

## 2. Blockbuster Classification

- Classify whether a movie will be a Blockbuster.

- A movie is considered blockbuster if its revenue is in the top 20% of the dataset.

## 3. NLP Analysis

- Used TF-IDF Vectorizer to extract text features from movie overview descriptions.

## 4. Movie Clustering

### Used K-Means Clustering to group movies into different types based on:

- Revenue

- Popularity

- Vote Average

- Runtime

# 💡 Key Insights

- Movie popularity strongly influences revenue

- Some genres consistently generate higher revenue

- Movies released in certain months perform better

- Production companies and countries impact success

- Vote count and popularity correlate with revenue

# 🌐 Deployment

- Final model saved using Pickle

- Integrated into a Streamlit Web App

## Users can:

- Enter movie details

- Click Predict

- See if the movie will become a Blockbuster

# ▶️ How to Run the Project
- ##Install dependencies
- pip install -r requirements.txt
- ##Run the Streamlit app
- streamlit run app.py

# 🔮 Future Improvements

- Add more advanced feature engineering

- Use Deep Learning models

- Improve NLP using BERT

- Add recommendation system

- Add interactive dashboard
