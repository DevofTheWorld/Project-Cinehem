from dotenv import load_dotenv
from google import genai
from google.genai import types
from .data_pipeline import pipeline
import os

load_dotenv()

class LLM_AGENT:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.5-flash"

    def roaster(self):
        obj = pipeline()

        system = """You are film you reviewer that is known to have very
                    sharp and striking words. You happen to encounter someones letterboxd account,
                    so you relentlessly roast them. Also take note of release date and current date
                    so you dont roast in a wrong way."""
        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"Roast this set of films {obj.main()} which is from someone's letterboxd",
            config=types.GenerateContentConfig(
                system_instruction=system,
                temperature=0.7,
            )
        )

        print(response.text)

if __name__ == "__main__":
    agent = LLM_AGENT()
    agent.roaster()