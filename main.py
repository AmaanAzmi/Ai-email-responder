def generate_reply(email_text: str) -> str:
    # Temporary dummy logic – will replace with AI later
    return "Thank you for your email. I will get back to you soon."

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

