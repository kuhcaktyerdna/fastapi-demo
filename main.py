from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request

from app.api.v1.posts_api import router as posts_router
from app.db.session import Base, engine
from app.exception.business_exceptions import EntityNotFoundException

app: FastAPI = FastAPI()
API_PREFIX: str = "/api/v1"

app.include_router(posts_router, prefix=API_PREFIX, tags=["posts"])

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check() -> dict:
    return {"status": "healthy"}

@app.exception_handler(EntityNotFoundException)
def entity_not_found_exception_handler(request: Request, exc: EntityNotFoundException) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"message": str(exc)}
    )
