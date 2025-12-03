from google import genai
from google.genai import types
import os

def get_client():
    key = os.getenv("GENAI_API_KEY")
    if not key:
        try:
            with open(".apikey.txt", "r") as f:
                key = f.read().strip()
        except Exception:
            key = None
    if not key:
        raise RuntimeError("No GENAI_API_KEY found! (set env GENAI_API_KEY or .apikey.txt)")
    return genai.Client(api_key=key)

def analyze_crash(text: str, model: str = "gemini-2.5-pro") -> str:
    client = get_client()
    prompt = (
        "You are an expert Minecraft crash-log and general log analyzer that can identify issues "
        "within a person's Minecraft instance that causes their game to crash or have catastrophic errors.\n\n"
        "Analyze the root cause of this crash concisely and provide concise instructions to resolve the error."
    )
    response = client.models.generate_content(
        model=model,
        contents=[
            types.Part.from_bytes(
                data=text.encode("utf-8"),
                mime_type='text/plain'),
            prompt
        ],
    )
    return response.text