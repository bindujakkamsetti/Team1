"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of Stress Level.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    Resp_pm = st.slider("Respiration Per Minute", int(df["Resp_pm"].min()), int(df["Resp_pm"].max()))
    AGE = st.slider("Age", int(df["AGE"].min()), int(df["AGE"].max()))
    PackHistory = st.slider("PackHistory", int(df["PackHistory"].min()), int(df["PackHistory"].max()))
    MWT1 = st.slider("MWT1", float(df["MWT1"].min()), float(df["MWT1"].max()))
    MWT2 = st.slider("MWT2", float(df["MWT2"].min()), float(df["MWT2"].max()))
    MWT1Best = st.slider("MWT1Best", float(df["MWT1Best"].min()), float(df["MWT1Best"].max()))
    FEV1 = st.slider("FEV1", float(df["FEV1"].min()), float(df["FEV1"].max()))
    FEV1PRED = st.slider("FEV1PRED", float(df["FEV1PRED"].min()), float(df["FEV1PRED"].max()))

    FVC = st.slider("FVC", int(df["FVC"].min()), int(df["FVC"].max()))
    FVCPRED = st.slider("FVCPRED", int(df["FVCPRED"].min()), int(df["FVCPRED"].max()))
    CAT = st.slider("CAT", float(df["CAT"].min()), float(df["CAT"].max()))
    HAD = st.slider("HAD", float(df["HAD"].min()), float(df["HAD"].max()))
    SGRQ = st.slider("SGRQ", float(df["SGRQ"].min()), float(df["SGRQ"].max()))
    AGEquartiles = st.slider("AGEquartiles", float(df["AGEquartiles"].min()), float(df["AGEquartiles"].max()))
    copd = st.slider("copd", float(df["copd"].min()), float(df["copd"].max()))

    gender = st.slider("gender", int(df["gender"].min()), int(df["gender"].max()))
    smoking = st.slider("smoking", int(df["smoking"].min()), int(df["smoking"].max()))
    Diabetes = st.slider("Diabetes", int(df["Diabetes"].min()), int(df["Diabetes"].max()))
    muscular = st.slider("muscular", float(df["muscular"].min()), float(df["muscular"].max()))
    hypertension = st.slider("hypertension", float(df["hypertension"].min()), float(df["hypertension"].max()))
    AtrialFib = st.slider("AtrialFib", float(df["AtrialFib"].min()), float(df["AtrialFib"].max()))
    
    IHD = st.slider("IHD", float(df["IHD"].min()), float(df["IHD"].max()))
    

    # Create a list to store all the features
    features = [Resp_pm,AGE,PackHistory,MWT1,MWT2,MWT1Best,FEV1,FEV1PRED,FVC,FVCPRED,CAT,HAD,SGRQ,AGEquartiles,copd,gender,smoking,Diabetes,muscular,hypertension,AtrialFib,IHD]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person has risk of extrapulmonary TB")
            st.info("Smell some Eucalyptus oil")
        elif (prediction == 2):
            st.warning("The person has risk of Pulmonary TB")
            st.info("Requires medical attention and nebulizaton")
        elif (prediction == 3):
            st.error("The person has high risk of Chronic / Drug Resistant Tuberculosis")
            st.info("Admit to ICU and start ventilation")
        elif (prediction == 4):
            st.error("The person has pulomonary Fungucitis!")
            st.info("Require Amycline or similar antibiotics")
        else:
            st.success("The person has no lungs problems 😄")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
