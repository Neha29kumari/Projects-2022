# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:11:45 2022

@author: lenovo
"""


import streamlit as st
import pandas as pd


st.title("Welcome to telecom project")


st.sidebar.header('User Input Parameters')



def user_input_features():
    
    ss = st.sidebar.selectbox("SeniorCitizen",(0,1))
    pat = st.sidebar.selectbox("Partner",("Yes","No"))
    dep = st.sidebar.selectbox("Dependents",("Yes","No"))
    ten = st.slider("Tenure",min_value=0,max_value=75,step=1)
    ml = st.sidebar.selectbox("MultipleLines", ("No","Yes","No phone service"))
    isr = st.sidebar.selectbox('InternetService',('DSL', 'Fiber optic' ,'No'))
    osr = st.sidebar.selectbox('OnlineSecurity',('No', 'Yes',"No internet service"))
    ob = st.sidebar.selectbox('OnlineBackup',('No', 'Yes',"No internet service"))
    dp = st.sidebar.selectbox('DeviceProtection',('No', 'Yes',"No internet service"))

    ts = st.sidebar.selectbox('TechSupport',('No', 'Yes',"No internet service"))
    
    cr = st.sidebar.selectbox('Contract',('Month-to-month', 'One year' ,'Two year'))
    
    pb = st.sidebar.selectbox('PaperlessBilling',('Yes','No'))
    pm = st.sidebar.selectbox('PaymentMethod',('Electronic check', 'Mailed check', 'Bank transfer (automatic)',
       'Credit card (automatic)'))
    
    
    mc = st.sidebar.number_input("Insert the MonthlyCharges",min_value=10,max_value=1000,step=1)
    tc = st.sidebar.number_input("Insert TotalCharges",min_value=10,max_value=1000,step=1)
    
    
    new = {
         'SeniorCitizen': ss,
         'Partner':pat,
         'Dependents':dep,
         'tenure': ten,
         'MultipleLines':ml,
         'InternetService': isr,
         'OnlineSecurity': osr,
         'OnlineBackup': ob,
         'DeviceProtection': dp,
         'TechSupport': ts,
         'Contract': cr,
         'PaperlessBilling': pb,
         'PaymentMethod': pm,
         'MonthlyCharges': mc,
         'TotalCharges': tc,
            }
    features = pd.DataFrame(new,index = [0])
    return features 
    
df = user_input_features()
st.write(df)


import pickle

with open(file="final_model.pkl",mode="rb") as f:
    model = pickle.load(f)
    

st.write("Model loaded")



result = model.predict(df)
st.subheader('Predicted Result')

if result[0]=="No":
    st.write("Customer will not Churn")
    
else:
    st.write("Customer will Churn")

