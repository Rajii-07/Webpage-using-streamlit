import streamlit as st
st.title("Webpage Using Streamlit")
Name=st.text_input("Enter your Name")
Gender=st.radio("Select Gender: ",('Male', 'Female',))
Age=st.number_input("Enter your Age")
Address=st.text_input("Enter your Full Address")
st.write("Hobbies")
st.checkbox("Watching Movies")
st.checkbox("Reading Books")
st.checkbox("Playing Games")
st.checkbox("Listening Music")
st.checkbox("Surfing Quora")
height = st.number_input('Please Enter Your Height in Cms : ',100,300 )
weight = st.number_input('Please Enter Your Weight in Kgs : ',1 )
check = st.button('Find BMI')
if(check):
    bmi = round(weight/height/height*10000,2)
    st.title(f'Your BMI : {bmi}')
    if(bmi>30):
        st.title('You are Obese.')
    elif(bmi>25):
        st.title('You are Overweight.')
    elif(bmi>18.5):
        st.title('You are Normal Weight.')
    else:
        st.title('You are Underweight.')

