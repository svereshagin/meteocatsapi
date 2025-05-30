from .settings import settings
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:get_app",
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level,
        reload=settings.reload,
        lifespan="on",
        factory=True,
    )
