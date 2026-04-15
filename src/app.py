from fastapi import FastAPI
import joblib
import os

app = FastAPI(title="MLOps Spam Detector API")

# Caminho do modelo (o artefato que você gerou no passo anterior)
MODEL_PATH = "models/model.pkl"

# Carregamos o modelo uma única vez quando a API inicia (eficiência!)
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("✅ Modelo carregado com sucesso!")
else:
    raise FileNotFoundError(f"❌ Erro: O arquivo {MODEL_PATH} não foi encontrado. Rode o train.py primeiro.")

@app.get("/")
def home():
    return {"message": "Spam Detector API is running!"}

@app.post("/predict")
def predict(text: str):
    # O modelo espera uma lista/array, por isso passamos [text]
    prediction = model.predict([text])[0]
    
    return {
        "input_text": text,
        "prediction": prediction
    }