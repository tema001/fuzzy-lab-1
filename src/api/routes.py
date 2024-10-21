import os

from fastapi import APIRouter, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request

from fuzzy.utils import main_proces

router = APIRouter()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@router.get('/', response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse('main.html', {"request": request})


@router.post('/submit', response_class=HTMLResponse)
def submit_form(
    request: Request,
    experience: int = Form(...),
    diploma_score: int = Form(...),
    prof_test: int = Form(...),
    eng_test: int = Form(...),
):
    num, term = main_proces(experience, diploma_score, prof_test, eng_test)
    return templates.TemplateResponse(
        'main.html',
        {
            'request': request,
            'response_text': f'Final score {num} - {term}',
            'experience': experience,
            'diploma_score': diploma_score,
            'prof_test': prof_test,
            'eng_test': eng_test,
        }
    )
