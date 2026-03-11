import streamlit as st
from joblib import dump, load
import numpy as np

# Load Model
model = load("model.pkl")
dump(model, "model.pkl", compress=3)


st.title("Movie Blockbuster Prediction")

runtime = st.number_input("Runtime (90 – 180 minutes)")
popularity = st.number_input("Popularity (1 – 100)")
vote_count = st.number_input("Vote Count (100 – 10000)")
vote_average = st.number_input("Vote Average (1 – 10)")

if st.button("Predict"):

    data = np.array([[runtime,popularity,vote_count,vote_average]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("This Movie Will Be Blockbuster")
    else:
        st.error("This Movie Will NOT Be Blockbuster")