import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from models import UnitModel, get_db
from schemas import Unit

app = FastAPI()
templates = Jinja2Templates(directory='templates')

load_dotenv()

SECRET_TOKEN = os.environ.get("TOKEN")
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)


def verify_token(api_key: str = Depends(api_key_header)) -> None:
    if not api_key:
        raise HTTPException(status_code=403, detail='Missing token')
    if api_key != SECRET_TOKEN:
        raise HTTPException(status_code=401, detail="Not valid token")


@app.get('/units/{unit_id}', response_model=Unit)
async def get_unit(
    unit_id: int,
    db: Session = Depends(get_db),
    verify: None = Depends(verify_token)
):
    unit = db.query(UnitModel).filter(UnitModel.id == unit_id).first()
    if not unit:
        raise HTTPException(status_code=404, detail='Unit not found')
    return unit


@app.get('/unit_info/{unit_id}', response_class=HTMLResponse)
async def get_unit(
    request: Request,
    unit_id: int,
    db: Session = Depends(get_db),
    verify: None = Depends(verify_token)
):
    unit = db.query(UnitModel).filter(UnitModel.id == unit_id).first()
    if not unit:
        raise HTTPException(status_code=404, detail='Unit not found')

    unit = Unit.model_validate(unit)
    unit_dict = Unit.model_dump(unit, by_alias=True)

    context = {
        'request': request,
        'unit_info': [
            {'наименование': unit_dict['short_name']},
            {'тип': unit_dict['type']},
            {'статус': unit_dict['org_status']},
            {'директор': unit_dict['director']['person']['fullname']},
        ]
    }
    return templates.TemplateResponse('unit.html', context)
