from fastapi import APIRouter
from app.models.suggestion_models import SuggestionOutput
from app.utils.suggustion_utils import get_suggestion_api

router = APIRouter(prefix='/suggestions')

@router.get('/{fragment}', response_model=SuggestionOutput)
async def get_suggestion(fragment: str):
    suggestion = await get_suggestion_api(fragment)
    return suggestion

