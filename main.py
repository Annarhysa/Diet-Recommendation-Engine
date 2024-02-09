from PIL import Image
import requests
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from streamlit_lottie import st_lottie

Pkl_file = 'pickle_model'
with open(Pkl_file, 'rb') as file:
    classifier=pickle.load(file)
df = pd.read_csv("Hackstreet2.csv")
sd = df['Food']


def prediction(BMI, Age, Health_Issue, Food):
    arr = np.zeros((1,8))
    arr[0,0] = sd[sd==Food].index[0]
    arr[0,-1] = Age
    arr[0,-2] = BMI
    if Health_Issue == 'Gastroentritis':
        arr[0,1] = 1
        arr[0,2] = 0
        arr[0,3] = 0
        arr[0,4] = 0
        arr[0,5] = 0
    elif Health_Issue == 'Cholestrol':
        arr[0,1] = 0
        arr[0,2] = 1
        arr[0,3] = 0
        arr[0,4] = 0
        arr[0,5] = 0
    elif Health_Issue == 'Thyroid':
        arr[0,1] = 0
        arr[0,2] = 0
        arr[0,3] = 1
        arr[0,4] = 0
        arr[0,5] = 0
    elif Health_Issue == 'Blood Pressure':
        arr[0,1] = 0
        arr[0,2] = 0
        arr[0,3] = 0
        arr[0,4] = 1
        arr[0,5] = 0
    else:
        arr[0,1] = 0
        arr[0,2] = 0
        arr[0,3] = 0
        arr[0,4] = 0
        arr[0,5] = 1

    input_arr = pd.DataFrame(arr)
    prediction = classifier.predict(input_arr)
    print(prediction)
    return prediction


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_diet = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_kl8ExNwnCB.json")



with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Diet Recommendation")
        st.write("An AI driven model which recommends whether a particular food item is safe for consumption by a person, taking into consideration the factors like health condition, age, BMI, and others")
        st.write("[Click here to calculate your BMI](https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm)")
        st.write("---")
    with right_column:
        st_lottie(lottie_diet, height = 250, key = "diet")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("Style/snowflake")

animation_symbol = "❄"

st.markdown(
    f"""
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
<div class = "snowflake">{animation_symbol}</div>
""", unsafe_allow_html = True)
    

def main():
    with st.container(): 
        html_temp = """<div style = "background-color:white;padding:12px"> <h1 style = "color:black; text-align:center;">Get Your Diet Right!</h1> </div>"""
        st.markdown(html_temp, unsafe_allow_html = True)
        
        st.write("##")

        BMI = st.text_input("BMI")
        Age = st.text_input("Age")
        Health_Issue = st.text_input("Health Issue")
        Food = st.text_input("Food")

    result = ""
    y_s = ""
    if st.button("Predict"):
        result = prediction(BMI, Age, Health_Issue, Food)
        if  result == 1:
            y_s = 'The particular food item is safe/recommended to be consumed by the person having disease.'
        else:
            y_s = 'The particular food item is not safe/not recommended to be consumed by the person having disease.'
    st.success('Result: {}'.format(y_s))

    with st.container():
        st.write("---")
        st.header("Get in Touch With H2Us")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/annarhysa13@gmail.com" method="POST">
             <input type="text" name="name" required placeholder = "Your name" required>
             <input type="email" name="email" placeholder = "Your email" required>
             <textarea name = "messgae" placeholder = "Your message here" required></textarea>
             <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html = True)

        local_css('style/ContactForm.css')

        
                




if __name__ == '__main__':
    main()
        

        
