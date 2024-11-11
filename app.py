import streamlit as st
import requests

# Set up the Streamlit app
st.set_page_config(page_title="Academic Research Paper Assistant", layout="centered")
st.title("📚 Academic Research Paper Assistant")

st.markdown(
    """
    This tool assists with summarizing academic content, answering questions, 
    and generating future research directions based on your input. 
    Provide a research topic and relevant content to get started!
    """
)

# Inputs: Topic and Content
topic = st.text_input("🔍 Enter a Research Topic", placeholder="e.g., Machine Learning in Healthcare")
content = st.text_area("📝 Enter Content to Analyze", height=200, placeholder="Paste the text here...")

# Function to handle FastAPI requests
def get_response(endpoint, payload):
    try:
        response = requests.post(f"http://localhost:8000/{endpoint}", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error {response.status_code}: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
        return None

# Buttons to trigger API calls
if st.button("🔄 Summarize"):
    if topic and content:
        with st.spinner("Generating summary..."):
            summary = get_response("summarize", {"topic": topic, "content": content})
            if summary:
                st.subheader("📄 Summary")
                st.write(summary.get("summary", "No summary available."))
    else:
        st.warning("Please provide both a topic and content.")

if st.button("❓ Ask a Question"):
    question = st.text_input("Enter your question:")
    if question and content:
        with st.spinner("Finding an answer..."):
            answer = get_response("ask", {"topic": question, "content": content})
            if answer:
                st.subheader("💡 Answer")
                st.write(answer.get("answer", "No answer found."))
    else:
        st.warning("Please enter a question and content.")

if st.button("🚀 Generate Research Directions"):
    if topic and content:
        with st.spinner("Generating research directions..."):
            directions = get_response("generate_directions", {"topic": topic, "content": content})
            if directions:
                st.subheader("🔍 Future Research Directions")
                st.write(directions.get("directions", "No directions found."))
    else:
        st.warning("Please provide both a topic and content.")
