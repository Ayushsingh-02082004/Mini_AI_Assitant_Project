from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

llm = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

