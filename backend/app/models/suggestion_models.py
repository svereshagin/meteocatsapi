from pydantic import BaseModel, Field

class SuggestionInput(BaseModel):
    address: str

class SuggestionOutput(BaseModel):
    suggestion: list[dict]