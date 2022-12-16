import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl','rb'))

st.header('Quora Question Pair Similarity')

q1 = st.text_input('Enter First Question')
q2 = st.text_input('Enter Second Question')

if st.button('Find'):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        st.header("Duplicate Question")
    else:
        st.header("Not Duplicate")