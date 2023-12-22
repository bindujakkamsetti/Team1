"""This module contains necessary function needed"""

# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import streamlit as st


@st.cache_data()
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('lungs.csv')

    # Perform feature and target split
    X = df[["Resp_pm","AGE","PackHistory","MWT1","MWT2","MWT1Best","FEV1","FEV1PRED","FVC","FVCPRED","CAT","HAD","SGRQ","AGEquartiles","copd","gender","smoking","Diabetes","muscular","hypertension","AtrialFib","IHD"]]
    y = df['Stage']

    return df, X, y

@st.cache_data()
def train_model(X, y):
    """This function trains the model and return the model and model score"""
    # Create the model
    model = RandomForestClassifier()
    # Fit the data on model
    model.fit(X, y)
    # Get the model score
    score = model.score(X, y)

    # Return the values
    return model, score

def predict(X, y, features):
    # Get model and model score
    model, score = train_model(X, y)
    # Predict the value
    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction, score
