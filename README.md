# Document Extraction using GPT-4o Vision

This project extracts structured information from NRIC / Passport documents using OpenAI GPT-4o Vision with strict JSON Schema enforcement.

## Features
- Image-based document extraction
- Structured JSON output using schema
- Gender / Race / Document validation


## Tech Stack
- Python
- FastAPI
- OpenAI GPT-4o Vision or other model like GPT-5.1
- JSON Schema
- Base64 Image Processing

## Setup Instructions

1. Clone the repository:

git clone https://github.com/YOUR_USERNAME/document-extraction-vision.git

2. Navigate to project folder:

cd document-extraction-vision

3. Create virtual environment:

python -m venv venv

4. Activate venv:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

5. Install dependencies:

pip install -r requirements.txt

6. Add environment variables:

Create `.env` file and add:

OPENAI_API_KEY=your_api_key_here

7. Run the server:

uvicorn main:app --reload

## API Endpoint

POST `/fetch_info/`

Upload an image to extract document details.

## Sample Output
	
{
  "first_name": "HAPPY",
  "last_name": "TRAVELER",
  "email": null,
  "mobile_number": null,
  "nric_or_passport_number": "340007237",
  "date_of_birth": "04 JUL 1967",
  "gender": "Female",
  "race": "Others",
  "occupation": null,
  "document_type": "Passport"
}
