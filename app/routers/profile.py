





from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.profile_analyzer import analyze_resume
import tempfile
import shutil
import os

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    # ✅ Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        # ✅ Use a temporary file safely (auto-deletes on exit)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            temp_path = tmp.name

        # ✅ Analyze the resume
        result = analyze_resume(temp_path)

    finally:
        # ✅ Clean up the temp file after processing
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return result
