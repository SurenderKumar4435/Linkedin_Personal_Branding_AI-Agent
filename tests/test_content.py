
import pytest
from app.services.content_generator import generate_linkedin_post

def test_generate_post():
    profile_summary = "Experienced Data Scientist with a focus on NLP and ML"
    industry_trends = "AI is booming, especially in enterprise automation"
    language = "en"

    post = generate_linkedin_post(profile_summary, industry_trends, language)

    # Assert the result is a non-empty string
    assert isinstance(post, str)
    assert len(post.strip()) > 0
