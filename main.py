import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set. Check your .env file.")

# Configure Gemini client
client = genai.Client(api_key=api_key)

def generate_reply(email_text: str) -> str:
    """
    Use Gemini to generate a professional reply to the given email.
    """
    prompt = f"""
You are a polite, professional email assistant.

Read the email below and write a clear, concise reply in a professional tone.

EMAIL:
{email_text}
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # fast, cheap model good for this use case[web:86]
        contents=prompt,
    )

    # response.text gives the generated text in the simple SDK examples[web:86][web:88]
    return response.text

if __name__ == "__main__":
    sample_email = """
    Hi, I want to know more about your pricing and features.
    Please send me the details.
    """
    reply = generate_reply(sample_email)
    print("EMAIL:")
    print(sample_email.strip())
    print("\nGENERATED REPLY:")
    print(reply)


