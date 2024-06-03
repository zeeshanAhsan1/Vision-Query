from .model import model_prediction

from typing import Union

from fastapi import FastAPI, UploadFile
import io
from PIL import Image

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}
    