import streamlit as st
import pandas as pd
import pickle

st.header('CAR PREDICTION APP :car:',)
col1, col2 = st.columns(2)

with col1:
    seats=st.selectbox('Enter the no of seats',
                        [4,5,7,9,11]
                        )
with col2:
    fuel_type_input=st.selectbox(
        'Enter the Fuel type:',
        ('Diesel', 'Petrol', 'CNG', 'LPG', 'Electric')
    )
col1, col2 = st.columns(2)
with col1:
    transmission=st.selectbox(
        'Enter the transmission type:',
        ('Manual','Automatic')
    )
with col2:
    Engine_CC=st.slider(
        'Engine CC', 500,5000,100
        )

encode_dict={
    'fuel_type':{'Diesel':1,'Petrol':2,'CNG':3,'LPG':4,'Electric':5},
    #'seller_type'={'Dealer':1,'Individual':2,'Trustmark Dealer':3},
    'transmission_type':{'Manual':1,'Automatic':2}
}
def car_pred(fuel_type_encode, transmission_type_encode,Engine_CC,seats):
    with open('car_pred','rb') as file:
        model=pickle.load(file)
        input_features=[[2014,2,130000,fuel_type_encode,transmission_type_encode,19.7,Engine_CC,46.3,seats]]
        return model.predict(input_features)

if st.button('Predict'):
    fuel_type_encode=encode_dict['fuel_type'][fuel_type_input]
    transmission_type_encode=encode_dict['transmission_type'][transmission]

    second_hand_price=car_pred(fuel_type_encode, transmission_type_encode,Engine_CC,seats)
    st.write('Predicted price is:',str(second_hand_price))