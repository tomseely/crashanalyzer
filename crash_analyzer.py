from google import genai
from google.genai import types
import pathlib

file_object = open(".apikey.txt", "r")
client = genai.Client(api_key=file_object.read())

filepath = pathlib.Path('message.txt')

prompt = '''You are an expert Minecraft crash-log and general log analyzer that can identify issues
        within a person's Minecraft instance that causes their game to crash or have catastrophic errors.
        
        Analyze the root cause of this crash and provide 3 potential fixes for the user to resolve it.
        '''
response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents=[
        types.Part.from_bytes(
            data=filepath.read_bytes(),
            mime_type='text/plain'),
        prompt]
)

print(response.text)