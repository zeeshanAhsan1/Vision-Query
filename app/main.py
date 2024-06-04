from .model import model_prediction

from typing import Union

from fastapi import FastAPI, UploadFile
import io
from PIL import Image

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/ask")
def ask_query(text: str, image: UploadFile):
    content = image.file.read()
    
    image = Image.open(io.BytesIO(content))
    # image = Image.open(image.file)
    
    result = model_prediction(text, image)
    return {"answer": result}
    