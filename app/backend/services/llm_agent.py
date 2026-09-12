from dotenv import load_dotenv
from google import genai
from google.genai import types
from data_pipeline import pipeline
import os

class LLM_AGENT:
    load_dotenv()

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.5-flash"

    def roaster(self):
        obj = pipeline()

        system = """You are Tyler Durden from Fight Club. You roast people. You roast their taste in films."""
        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"Roast this set of films {obj.main()} from someone's letterboxd",
            config=types.GenerateContentConfig(
                system_instruction=system,
                temperature=0.7,
            )
        )

        print(response.text)

if __name__ == "__main__":
    agent = LLM_AGENT()
    agent.roaster()