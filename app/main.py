



from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routers import profile, content, posting, analytics

from fastapi import FastAPI
from app.routers import profile, content, posting, analytics

app = FastAPI()

app.include_router(profile.router, prefix="/profile")

app = FastAPI(
    title="LinkedIn Personal Branding AI Agent",
    description="An AI-powered tool to optimize personal branding on LinkedIn using OpenAI, automation, and data insights.",
    version="1.0.0",
)

# ✅ CORS Middleware (for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Custom Error Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "detail": str(exc)},
    )

# ✅ Include all routers
app.include_router(profile.router, prefix="/profile", tags=["Profile Analyzer"])
app.include_router(content.router, prefix="/content", tags=["Content Generator"])
app.include_router(posting.router, prefix="/post", tags=["Post Scheduler"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])


