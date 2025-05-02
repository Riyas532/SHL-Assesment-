# SHL Assessment Recommendation System

## How to Run

1. Install requirements: `pip install -r requirements.txt`
2. Start API: `uvicorn main:app --reload`
3. Open Streamlit UI: `streamlit run streamlit_app.py`

## Deployment

- Streamlit Cloud: for frontend
- Render/Railway: for API hosting

## Notes

- Uses SentenceTransformer for embedding
- Data stored in `catalog_data.json`