from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from openai import OpenAI
import os

# Load BLIP model
def load_blip_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
    return processor, model

# Generate basic caption using BLIP
def generate_basic_caption(image):
    processor, model = load_blip_model()
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Generate behavioral analysis using OpenAI
def generate_behavioral_analysis(basic_caption):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert at analyzing human behavior from descriptions. Provide a detailed behavioral analysis that goes beyond basic description. Infer intentions, emotions, and social context."},
            {"role": "user", "content": f"Based on this image description: '{basic_caption}', provide a behavioral analysis of what might be happening. Only one paragraph with a maximum of 100 words."}
        ]
    )
    
    return response.choices[0].message.content

# Main function to process image
def analyze_image(image):
    basic_caption = generate_basic_caption(image)
    behavioral_analysis = generate_behavioral_analysis(basic_caption)
    
    return {
        "basic_caption": basic_caption,
        "behavioral_analysis": behavioral_analysis
    }
