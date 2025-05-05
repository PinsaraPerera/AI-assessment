# Behavioral Image Captioning

This project generates behavioral descriptions from images by combining computer vision and natural language processing. It goes beyond basic scene descriptions to infer human behaviors, intentions, and social contexts.

## Features

- Upload images through an intuitive Streamlit interface
- Generate basic image captions using BLIP (Bootstrapping Language-Image Pre-training)
- Enhance captions with behavioral analysis using OpenAI's GPT-3.5
- View both the basic caption and the behavioral analysis side by side

## Architecture

The application uses a two-stage pipeline:
1. **BLIP Model**: Generates accurate initial image captions
2. **GPT-3.5**: Enhances the captions with behavioral analysis

## Installation

1. Clone this repository:
```
git clone https://github.com/PinsaraPerera/AI-assessment.git
cd AI-assessment
```

2. Create a virtual environment and install dependencies:
```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the Streamlit application:
```
streamlit run app.py
```

Then:
1. Upload an image through the interface
2. Click "Generate Analysis"
3. View the basic caption and behavioral analysis

## Project Structure

- `app.py`: Streamlit frontend interface
- `caption_generator.py`: Backend logic for image processing and caption generation
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (API keys)

## Models Used

### BLIP (Bootstrapping Language-Image Pre-training)

BLIP is a state-of-the-art vision-language model that excels at both understanding and generation tasks. It uses a multimodal mixture of encoder-decoder architecture and implements a caption bootstrapping method to improve learning from noisy web data.

Key advantages:
- Unified framework for vision-language tasks
- Effective utilization of noisy web data
- Strong generalization ability to unseen tasks

### GPT-3.5 Turbo

OpenAI's GPT-3.5 Turbo is used to transform basic image captions into nuanced behavioral descriptions by inferring intentions, emotions, and social contexts from the scene description.

## Example Outputs

Basic Caption: "a woman sitting on the beach with her dog"

Behavioral Analysis: "The woman appears to be taking a moment of relaxation at the beach with her canine companion. The setting suggests she values outdoor leisure time and has a close bond with her pet. The beach environment indicates she's seeking a peaceful, natural setting, possibly to unwind from daily stresses. Her posture of sitting rather than more active engagement suggests a contemplative mood, perhaps taking time for mindfulness or simply enjoying the sensory experience of the beach. The presence of her dog shows she prioritizes companionship even during personal relaxation time."

## Requirements

- Python 3.10+
- PyTorch
- Transformers
- OpenAI API key
- Streamlit
- python-dotenv