import schedule
import time
import logging
import threading
from datetime import datetime
from typing import Optional
from fastapi import FastAPI, HTTPException, Query, Body
from pydantic import BaseModel
from dateutil import parser as date_parser
from fastapi.responses import FileResponse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

app = FastAPI()

# --- Dummy favicon to avoid 404 ---
@app.get("/favicon.ico")
def favicon():
    # You can place an actual favicon.ico file in the same folder and return it
    return FileResponse("favicon.ico")

class ScheduleRequest(BaseModel):
    scheduled_time: str
    content: str

def parse_scheduled_time(scheduled_time: str) -> Optional[datetime]:
    try:
        parsed = date_parser.parse(scheduled_time)
        return parsed
    except Exception:
        return None

def job_to_run(content: str):
    logging.info(f"✅ Scheduled post published! Content: {content}")

def schedule_post_job(parsed_time: datetime, content: str):
    delay = (parsed_time - datetime.now()).total_seconds()
    if delay <= 0:
        raise ValueError("Scheduled time must be in the future")
    
    # Run job once at exact datetime
    def delayed_job():
        time.sleep(delay)
        job_to_run(content)
    
    threading.Thread(target=delayed_job, daemon=True).start()
    logging.info(f"📅 Post scheduled at {parsed_time} with content: {content}")

@app.post("/post/schedule")
def schedule_post(
    scheduled_time: Optional[str] = Query(None),
    content: Optional[str] = Query(None),
    body: Optional[ScheduleRequest] = Body(None)
):
    # Prefer JSON body if provided, else fallback to query params
    if body:
        scheduled_time = body.scheduled_time
        content = body.content

    logging.info(f"Received scheduled_time={scheduled_time}, content={content}")

    if not scheduled_time or not content:
        raise HTTPException(status_code=400, detail="scheduled_time and content are required")

    parsed_time = parse_scheduled_time(scheduled_time)
    if not parsed_time:
        raise HTTPException(status_code=400, detail="Invalid scheduled_time format. Please use a valid date/time string.")

    try:
        schedule_post_job(parsed_time, content)
        return {
            "status": "success",
            "scheduled_time": parsed_time.isoformat(),
            "content": content
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Scheduling failed: {str(e)}")
    except Exception:
        logging.exception("Unexpected error while scheduling post")
        raise HTTPException(status_code=500, detail="Internal Server Error")
