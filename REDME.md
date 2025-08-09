# 


```bash
conda create -n linkedin python=3.10 -y
```


```bash
conda activate linkedin
```


pip install -r requirements.txt 

# Use this command for run the project
uvicorn app.main:app --reload

# By Use this command show your project on Browser
http://127.0.0.1:8000/docs