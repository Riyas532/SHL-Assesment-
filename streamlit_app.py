import streamlit as st
import requests

st.title("SHL Assessment Recommender")
query = st.text_area("Enter job description or query")

if st.button("Get Recommendations"):
    response = requests.post("http://localhost:8000/recommend", json={"query": query})
    if response.status_code == 200:
        results = response.json().get("results", [])
        for res in results:
            st.markdown(f"- [{res['name']}]({res['url']}) - {res['duration']} mins")
    else:
        st.error("API Error")