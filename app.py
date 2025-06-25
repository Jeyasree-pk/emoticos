import openai
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
openai.api_key = "your_openai_api_key"

class MoodRequest(BaseModel):
    text: str

@app.post("/detect-mood")
def detect_mood(request: MoodRequest):
    prompt = f"What is the mood or emotion in the following sentence?\n\n\"{request.text}\"\n\nRespond with just one word."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5,
        temperature=0.2
    )

    mood = response.choices[0].message.content.strip()
    return {"mood": mood}
