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

Important Name Detection Rule:
The person's full name may NOT appear next to the label "Name".

For NRIC:
If a standalone line of uppercase text appears near the top of the document
(typically between the NRIC number and the Race/Sex/Date of Birth section),
assume this is the full name of the person.

For NRICs only:
1.Split the detected full name into:
- first_name
- last_name

2.If multiple words are present:
- The last word is the last_name
- All preceding words form the first_name

Example:
"LIM WEI MING"
first_name = "LIM WEI"
last_name = "MING"

Additional constraints:
- Gender must be one of: Male, Female, Prefer not to say.
- Race should be from the field seen in the image. Examples: Chinese, Malay, Indian, Javanese etc. If not seen put race: Others.
- Document type must be either: NRIC or Passport.

If a field is not found, return null.
Do not hallucinate missing values.
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
