# constants.py

SYSTEM_PROMPT = """
You are a strict document extraction engine.

Rules:
- Return ONLY valid JSON.
- Do not include explanations.
- If a field is missing, return null.
- Do not hallucinate values.
"""

USER_PROMPT_TEMPLATE = """
Extract the required fields from this document image.

Additional constraints:
- Gender must be one of: Male, Female, Prefer not to say.
- Race must be one of: Chinese, Malay, Indian, Others.
- Document type must be either: NRIC or Passport.
"""

JSON_SCHEMA = {
    "format": {
        "type": "json_schema",
        "name": "document_extraction",
        "strict": True,
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "first_name": {"type": ["string", "null"]},
                "last_name": {"type": ["string", "null"]},
                "email": {"type": ["string", "null"]},
                "mobile_number": {"type": ["string", "null"]},
                "nric_or_passport_number": {"type": ["string", "null"]},
                "date_of_birth": {"type": ["string", "null"]},
                "gender": {"type": ["string", "null"]},
                "race": {"type": ["string", "null"]},
                "occupation": {"type": ["string", "null"]},
                "document_type": {"type": ["string", "null"]}
            },
            "required": [
                "first_name",
                "last_name",
                "email",
                "mobile_number",
                "nric_or_passport_number",
                "date_of_birth",
                "gender",
                "race",
                "occupation",
                "document_type"
            ]
        }
    }
}
