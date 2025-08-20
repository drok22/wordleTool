# FastAPI Application

A basic FastAPI application setup.

## Requirements

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

   ```

2. Create a virtual environment:

   python -m venv venv
   source venv/bin/activate # On Windows use: venv\Scripts\activate

3. Install Dependencies:

   pip install -r requirements.txt

   If you don't have a requirements.txt, you can create one with:

   pip install fastapi uvicorn
   pip freeze > requirements.txt

# Run the app

    uvicorn main:app --reload

    main refers to the filename main.py
    app is the FastAPI instance inside main.py
    --reload auto-restarts the server when you make code changes (development only)

## Accessing the API

    API root: http://127.0.0.1:8000
    Interactive API docs (Swagger UI): http://127.0.0.1:8000/docs
    Alternative docs (ReDoc): http://127.0.0.1:8000/redoc
