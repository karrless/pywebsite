from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/")
def index():
    return RedirectResponse(url="/resume/temp", status_code=status.HTTP_302_FOUND)

