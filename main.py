from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.v1.posts_api import router as posts_router
from app.exception.business_exceptions import EntityNotFoundException

app = FastAPI()

app.include_router(posts_router)

@app.get("/health")
def health_check() -> dict:
    return {"status": "healthy"}

@app.exception_handler(EntityNotFoundException)
def entity_not_found_exception_handler(exc: EntityNotFoundException) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"message": str(exc)}
    )
