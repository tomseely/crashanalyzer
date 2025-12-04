from google import genai
from google.genai import types
import os

# Get the absolute path of the current file
file_path = os.path.abspath(__file__)

# Extract the directory name from the file path
directory_name = os.path.dirname(file_path)

# gets Gemini client using API key from environment variable or through the hidden .apikey.txt file
def get_client():
    key = os.getenv("GENAI_API_KEY")
    if not key:
        try:
            with open(directory_name + "/../.apikey.txt", "r") as f:
                key = f.read().strip()
        except Exception:
            key = None
    if not key:
        raise RuntimeError("No GENAI_API_KEY found! (set env GENAI_API_KEY or .apikey.txt)")
    return genai.Client(api_key=key)


# function that takes log file (text) to call Gemini API and returns its output
def analyze_crash(text: str, model: str = "gemini-2.5-pro") -> str:
    client = get_client()
    with open(directory_name + "/../data/directive.txt", "r") as f:
        directive = f.read()
    prompt = (
        "You are an expert Minecraft crash-log and general log analyzer that can identify issues "
        "within a person's Minecraft instance that causes their game to crash or have catastrophic errors.\n\n"
        "Analyze the root cause of this crash concisely and provide concise instructions to resolve the error.\n"
        "If the given file is not a Minecraft log or crash log tell them its an incorrect file and thats it.\n"
        "For better log analysis here are additional directives for common problems that pure log analysis may not find:\n"
        + directive
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