


from fastapi import APIRouter
from datetime import datetime
import random

router = APIRouter()

@router.get("/performance")
def analyze_performance(post_id: str = "latest"):
    # Simulate fetching post metrics (could be tied to real post ID in future)
    performance_data = {
        "post_id": post_id,
        "timestamp": datetime.utcnow().isoformat(),
        "metrics": {
            "likes": random.randint(50, 300),
            "comments": random.randint(10, 50),
            "shares": random.randint(5, 20),
            "views": random.randint(500, 5000),
            "engagement_rate": round(random.uniform(2.5, 8.5), 2)
        }
    }
    return performance_data
