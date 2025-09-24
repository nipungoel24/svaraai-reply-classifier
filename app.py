import os
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Define Pydantic models for request and response
class TextInput(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    label: str
    confidence: float

# 2. Initialize FastAPI app
app = FastAPI(
    title="SvaraAI Reply Classification API",
    description="A service to classify email replies as positive, neutral, or negative."
)

# 3. Load the pre-trained model and artifacts
# This section assumes the fine-tuned DistilBERT model is saved in a directory named 'distilbert_model'.
model_pipeline = None
model_type = "Not Loaded"
label_encoder = None

# A) Hardcode the LabelEncoder fitting, as it is not saved to a file by the notebook.
label_encoder = LabelEncoder()
# This order must match the notebook's encoding (negative=0, neutral=1, positive=2)
label_encoder.fit(['negative', 'neutral', 'positive'])

# B) Attempt to load the DistilBERT model
try:
    if os.path.exists("./distilbert_model"):
        tokenizer = AutoTokenizer.from_pretrained("./distilbert_model")
        model = AutoModelForSequenceClassification.from_pretrained("./distilbert_model")
        model_pipeline = pipeline(
            "text-classification",
            model=model,
            tokenizer=tokenizer,
            return_all_scores=True
        )
        model_type = "DistilBERT"
        print("Successfully loaded DistilBERT model.")
except Exception as e:
    print(f"Failed to load DistilBERT model. Reason: {e}")
    model_pipeline = None

# C) Fallback if no model is found
if model_pipeline is None:
    print("No model found. The API will return default responses.")
    model_type = "None"

# 4. Define the /predict endpoint
@app.post("/predict", response_model=PredictionResponse)
async def predict_reply(input_data: TextInput):
    """
    Classifies an email reply as positive, neutral, or negative.
    """
    # Return a default response if no model is loaded
    if model_type == "None":
        return {"label": "neutral", "confidence": 0.0}

    text_to_classify = input_data.text
    
    try:
        prediction_result = model_pipeline(text_to_classify, top_k=1)[0]
        predicted_label = prediction_result['label']
        confidence = prediction_result['score']
        
        # Map the transformer label (e.g., 'LABEL_0') to the original string label
        label_map = {
            'LABEL_0': 'negative',
            'LABEL_1': 'neutral',
            'LABEL_2': 'positive'
        }
        final_label = label_map.get(predicted_label, 'neutral')

    except Exception as e:
        print(f"Prediction failed with DistilBERT. Reason: {e}")
        final_label = 'neutral'
        confidence = 0.5

    return PredictionResponse(label=final_label, confidence=confidence)

# 5. Define a simple health check endpoint
@app.get("/health")
def health_check():
    """Returns a status of the API."""
    return {"status": "ok", "model_loaded": model_type}