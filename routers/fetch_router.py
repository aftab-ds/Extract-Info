from fastapi import APIRouter, UploadFile, File
from services import fetch_info


router = APIRouter(prefix='/fetch_info',tags=['Fetch Info'])



@router.post('')
def fetch_info_service(img_file: UploadFile = File(...)):

    fetch_info.validate_image(img_file)

    response = fetch_info.call_gpt(img_file)


    return response

    