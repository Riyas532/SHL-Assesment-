import streamlit as st
from recommendation import get_recommendations
import pandas as pd

st.title("SHL Assessment Recommender")

query = st.text_area("Enter job description or natural language query:")

if st.button("Get Recommendations"):
    if query.strip():
        results = get_recommendations(query)
        if results:
            # Format results into DataFrame
            for item in results:
                item["name"] = f"[{item['name']}]({item['url']})"
                del item["url"]  # We include it as a link in the name
            df = pd.DataFrame(results)
            df.columns = [col.capitalize() for col in df.columns]
            st.markdown("### Top Recommended Assessments")
            st.write(df.to_markdown(index=False), unsafe_allow_html=True)
        else:
            st.warning("No recommendations found.")
    else:
        st.warning("Please enter a query to get recommendations.")