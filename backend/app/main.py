from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routes.weather_routes import router as weather_router
from .routes.suggestion_routes import router as suggestion_router

def get_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(weather_router)
    app.include_router(suggestion_router)
    return app
