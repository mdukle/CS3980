# First FastAPI app

```bash 
python -m venv venv
.\venv\Scripts\activate
pip install fastapi
pip install uvicorn
```

Create a python file `api.py` with code. 

```bash
uvicorn api: app --reload 
```

After everything is looking good, make a `requirements.txt` file before commit. Exit the virtual environment first.

```bash
pip freeze > requirements.txt
```

Can then exit the virtual environment with deactivate.