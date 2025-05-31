# https://catalog.api.2gis.com/3.0/suggests?q=Москва Петровка, 2&type=building&suggest_type=address&fields=items.point&key=YOUR_KEY
import asyncio

from app.models.suggestion_models import SuggestionOutput
from app.settings import settings
import httpx


async def get_suggestion_api(fragment: str) -> SuggestionOutput:
    """
    Function calls 2gis to get a bunch of suggestions that we retrieve from json 
    :param fragment: 
    :return SuggestionOutput: 
    """
    url = "https://catalog.api.2gis.com/3.0/suggests"
    params = {
        "q": fragment,
        "suggest_type": "route_endpoint",
        "key": settings.weather.api,
    }
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Правильный путь к данным в ответе 2GIS
        items = data.get('result', {}).get('items', [])
        suggestions = [
            {'full_name': item['full_name']}
            for item in items
            if 'full_name' in item
        ]
        return SuggestionOutput(suggestion=suggestions)

