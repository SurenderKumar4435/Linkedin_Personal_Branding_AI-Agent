import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    
    "app/__init__.py",
    "app/main.py",
    "app/routers/profile.py",
    "app/routers/content.py",
    "app/routers/posting.py",
    "app/routers/analytics.py",

    "app/services/profile_analyzer.py",
    "app/services/industry_research.py",
    "app/services/content_generator.py",
    "app/services/post_optimizer.py",
    "app/services/scheduler.py",
    "app/services/image_generator.py",
    "app/services/translator.py",
    "app/services/ethics_checker.py",
    
    "app/utils/linkedin_api.py",
    "app/utils/helper.py",
    "app/utils/db.py",

    "tests/test_content.py",
    "data/posts/",

    ".env",
    "requirements.txt",
    "REDME.md",
   " run.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")