import os # i have no idea of the os library
from dotenv import load_dotenv # this is importing the .env file in my python project
from google import genai # this is importing the library from google i guess

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") # the code is assigning a value to api key and making it load the file
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set. Check your .env file.") # guiding the code to give an error if the code didnt run reply with the error

# Configure Gemini client
client = genai.Client(api_key=api_key)

def generate_reply(email_text: str, tone: str = "formal") -> str: #i know the def is a function but i have no idea of whats happening in the code, the rest of the code i have no idea
    """
    Use Gemini to generate a professional reply to the given email.
    """
    prompt = f"""
You are a polite, professional email assistant.

Write the reply in a {tone} to the email below. Follow these rules:
- Start with a short greeting according to sri lankan tradition.
- Answer the user's questions clearly.
- If something is unclear, ask 1-2 clarifying questions.
- End with a friendly sign-off.
- Keep the reply under 8 sentences

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
    print("=== AI Email Responder ===")

    tone = input("Choose tone (formal/casual): ").strip().lower()
if tone not in ("formal", "casual"):
    tone = "formal"
    print("Paste your email below. End input with a blank line.")
    print("---------------------------")

    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    email_text = "\n".join(lines).strip()

    if not email_text:
        print("No email text provided. Existing.")
    else:
        print("\nGenerating reply...\n")
        reply = generate_reply(email_text, tone=tone)
        print("=== GENERATED REPLY ===")
        print(reply)


