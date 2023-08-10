import  streamlit as st
import pickle as pkl

model  =pkl.load(open('model.pkl' ,'rb'))

st.title("Car Pricing")

year = st.number_input("how many years old is car")
present_price = st.text_input("Present price")
kms = st.text_input("kms driven")

fuel = st.selectbox("fuel type", ['deisel' ,'patrol' ,  'CNG'])
if  fuel == 'patrol' :
    fuel = 2
elif fuel == 'deisel':
    fuel = 1
else :
    fuel = 0

seller = st.selectbox("select seller type",['individual','Dealer'])
if seller == 'individual':
    seller = 1
else :
    seller = 0


transmission = st.selectbox("transmission",['Manual' , 'Automatic'])
if transmission == 'Manual':
    transmission=1
else :
    transmission = 0

owner = st.selectbox("owners",[0,1,3])


if st.button("predict"):
    predicted = model.predict([[year, present_price, kms, fuel, seller, transmission, owner]])
    st.write("expected price = " ,predicted[0])
