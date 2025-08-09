


from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.post_optimizer import optimize_post
from app.services.scheduler import schedule_post_job
from app.services.compliance_checker import check_post_compliance

router = APIRouter()

class ScheduleRequest(BaseModel):
    post: str
    schedule_time: str  # e.g., "10:00"

@router.post("/schedule")
def schedule_post(req: ScheduleRequest):
    # Step 1: Compliance check
    is_compliant, issues = check_post_compliance(req.post)
    if not is_compliant:
        raise HTTPException(status_code=400, detail=f"Non-compliant post. Found: {issues}")

    # Step 2: Optimize the post
    optimized = optimize_post(req.post)

    # Step 3: Schedule using `schedule` library
    try:
        schedule_post_job(optimized, req.schedule_time)
        return {"status": "✅ Post scheduled", "content": optimized, "time": req.schedule_time}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Scheduling failed: {str(e)}")



