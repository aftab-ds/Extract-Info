import os
import base64
import json
from dotenv import load_dotenv
from openai import OpenAI
from constants import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE, JSON_SCHEMA
from fastapi import UploadFile, HTTPException
from PIL import Image
import io

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found")

client = OpenAI(api_key=api_key)


def validate_image(file: UploadFile):

    contents = file.file.read()

    try:
        img = Image.open(io.BytesIO(contents))
        img.verify()
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid file. Please upload a valid image."
        )

    # reset pointer so it can be reused later
    file.file.seek(0)

    return True



def read_image(image: UploadFile):
    image_bytes = image.file.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    image.file.seek(0)
    return f"data:image/png;base64,{image_base64}"


def call_gpt(image):

    image_data_url = read_image(image=image)

    response = client.responses.create(
        model="gpt-5.1",
        input=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "input_text",
                        "text": SYSTEM_PROMPT
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": USER_PROMPT_TEMPLATE
                    },
                    {
                        "type": "input_image",
                        "image_url": image_data_url
                    }
                ]
            }
        ],
        text=JSON_SCHEMA,
        max_output_tokens=200
    )

    final_response = response.output_text

    try:
        return json.loads(final_response)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON returned", "raw": final_response}
