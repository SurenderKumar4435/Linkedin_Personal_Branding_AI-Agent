


from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.content_generator import generate_linkedin_post

router = APIRouter()

class ContentRequest(BaseModel):
    job_title: str
    topic: str

@router.post("/generate")
def generate_content(req: ContentRequest):
    try:
        post = generate_linkedin_post(req.job_title, req.topic)
        return {"generated_post": post}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate content: {str(e)}")
