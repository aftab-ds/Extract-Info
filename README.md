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

```bash
git clone https://github.com/aftab-ds/Extract-Info.git
```

2. Navigate to project folder:

```bash
cd document-extraction-vision
```

3. Create virtual environment:

```bash
python -m venv venv
```

4. Activate venv:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Add environment variables:

Create `.env` file and add:
```bash
OPENAI_API_KEY=your_api_key_here
```

7. Run the server:

```bash
uvicorn main:app --reload
```

## API Endpoint

POST `/fetch_info/`

Upload an image to extract document details.

Accepted file types: `png`, `jpg/jpeg`, `webp`, `gif`, `bmp`, `tiff`.

If a non-image file (or mismatched file type) is uploaded, the API returns `400 Bad Request` with a clear error message.

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
