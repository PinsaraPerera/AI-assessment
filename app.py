import streamlit as st
from PIL import Image
import os
from caption_generator import analyze_image
from dotenv import load_dotenv
import torch

# Fix for torch/streamlit compatibility issue
torch.classes.__path__ = []

# Load environment variables from .env file
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="Behavioral Image Analysis",
    layout="wide"
)

# Main header
st.title("Behavioral Image Captioning")
st.write("Upload an image to generate a behavioral analysis")

# Set the API key from environment variable
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Main content
col1, col2 = st.columns([1, 2])

with col1:
    # Image upload section
    uploaded_file = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Uploaded Image")

# analysis section
with col2:
    if uploaded_file is not None:
        if st.button("Generate Analysis"):
            with st.spinner("Analyzing image..."):
                # Process the image
                results = analyze_image(image)
                
                # Display results
                st.subheader("Basic Caption")
                st.write(results["basic_caption"])
                
                st.subheader("Behavioral Analysis")
                st.write(results["behavioral_analysis"])
