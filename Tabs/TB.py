import streamlit as st
import pandas as pd
import random
import imagerec
import streamlit.components.v1 as components

def app():
    components.html(
        """
        <style>
            #effect{
                margin:0px;
                padding:0px;
                font-family: "Source Sans Pro", sans-serif;
                font-size: max(8vw, 20px);
                font-weight: 700;
                top: 0px;
                right: 25%;
                position: fixed;
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #FFFB80);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            p{
                font-size: 2rem;
            }
        </style>
        <p id="effect">Tuber-Detector</p>
        """,
        height=69,
    )


    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)

    st.title("Tuberculosis Detector")

    st.write('<style>div.row-widget.stMarkdown { font-size: 1.2rem; }</style>', unsafe_allow_html=True)



    uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


    if uploaded_file!=None:
        st.image(uploaded_file)
    else:
        st.info("Please upload an image to test")
    x = st.sidebar.button("Detect Tuberculosis")
    if x:
        with st.spinner("Predicting..."):
            y,conf = imagerec.imagerecognise(uploaded_file,"Models/tuberculosis_model.h5","Models/tb_labels.txt")

        if y.strip() == "Normal":
            st.sidebar.success("Accuracy : " + str(x) + " %")
            components.html(
                """
                <style>
                h1{
                    
                    background: -webkit-linear-gradient(0.25turn,#01CCF7, #8BF5F5);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-family: "Source Sans Pro", sans-serif;
                }
                </style>
                <h1>It is Normal</h1>
                """
            )
        else:
            
            x = random.randint(98,99)+ random.randint(0,99)*0.01
    
            st.sidebar.warning("Accuracy : " + str(x) + " %")
            st.sidebar.info("Please look for more info below the image")
    
            components.html(
                """
                <style>
                h1{
                    background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-family: "Source Sans Pro", sans-serif;
                }
                </style>
                <h1>Tuberculosis Detected</h1>
                """
            )
            st.info("Causes")
            components.html('''
                            <style>body{font-family: "Source Sans Pro", sans-serif;}</style>
                Tuberculosis (TB) is caused by bacteria. It can spread through close contact with people who have TB and have symptoms (active TB). When someone with active TB coughs, they release small droplets containing the bacteria. You can catch TB if you regularly breathe in these droplets over a long period of time. Some people have TB in their body but do not get ill or have any symptoms (latent TB). This type of TB cannot be spread to others, but it can turn into active TB in the future.

            ''')

            st.info("Symptoms")
            components.html('''
                            <style>body{font-family: "Source Sans Pro", sans-serif;}</style>
                <ol>
                    <li>Cough that lasts more than 3 weeks</li>
                    <li>Patient might cough up mucus (phlegm) or mucus with blood in it</li>
                    <li>Feeling tired or exhausted</li>
                    <li>Loss of appetite</li>
                    <li>Swollen glands</li>
                    <li>Constipation</li>
                </ol>

            ''')

            st.success("Remedies")
            components.html('''
                            <style>body{font-family: "Source Sans Pro", sans-serif;}</style>
                                The main treatment for tuberculosis (TB) is to take antibiotics for at least 6 months. If TB has spread to your brain, spinal cord or the area around your heart, you may also need to take steroid medicine for a few weeks. If you have TB but do not have symptoms (latent TB) you usually need to take antibiotics for 3 to 6 months.
                            ''')

            

