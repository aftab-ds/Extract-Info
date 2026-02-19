from fastapi import APIRouter, UploadFile
from services import fetch_info


router = APIRouter(prefix='/fetch_info',tags=['Fetch Info'])



@router.post('/')
def fetch_info_service(img_file: UploadFile):

    response = fetch_info.call_gpt(img_file)


    return response

    