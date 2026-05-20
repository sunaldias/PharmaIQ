# pharmaIQ

# AI Service Setup

## 1. Create virtual environment
python -m venv venv

## 2. Activate it
source venv/bin/activate
# or venv\Scripts\activate on Windows

## 3. Install dependencies
pip install -r requirements.txt

## 4. Add environment variables
Create a .env file

## 5. Run the server
uvicorn app.main:app --reload