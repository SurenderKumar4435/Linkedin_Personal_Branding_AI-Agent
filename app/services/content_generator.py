

import re
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Create OpenAI client using environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clean_generated_text(text: str) -> str:
    """Remove placeholders, excessive spaces/newlines, and unwanted formatting."""
    # Remove placeholders like [Industry], [Hashtag], etc.
    text = re.sub(r"\[.*?\]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Normalize multiple newlines to max 2
    text = re.sub(r"(\n\s*){3,}", "\n\n", text)

    # Optional: remove emojis (uncomment if you want no emojis)
    # text = re.sub(r"[^\w\s,.!?;:()\-]", "", text)

    return text.strip()

def generate_linkedin_post(profile_summary: str, industry_trends: str, language: str = "en") -> str:
    if not profile_summary or not industry_trends:
        return "Profile summary and industry trends are required."

    prompt = f"""
You are a LinkedIn personal branding expert.
Write a professional, engaging, and relevant LinkedIn post tailored for the following user profile:

Profile Summary:
{profile_summary}

Trending Topics in the Industry:
{industry_trends}

Language: {language}

Requirements:
- Keep the tone friendly and professional.
- Keep it concise (max 150 words).
- Encourage engagement.
- Avoid jargon.
- Do NOT use placeholders like [Industry], [Hashtag], or [mention any recent changes].
- Replace all placeholders with realistic examples.
- Ensure the text is clean, well-formatted, and ready to post on LinkedIn without extra symbols or filler.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Updated to latest small, fast model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )

        raw_text = response.choices[0].message.content.strip()
        return clean_generated_text(raw_text)

    except Exception as e:
        return f"Error generating LinkedIn post: {str(e)}"

