from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi
from .api import art_pieces, reviews, tags, users
from .database import engine
from . import models
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Art Review API",
    description="An API for uploading and reviewing art pieces",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the uploads directory
os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(art_pieces.router, prefix="/art-pieces", tags=["art_pieces"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
app.include_router(tags.router, prefix="/tags", tags=["tags"])
app.include_router(users.router, prefix="/users", tags=["users"])

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Art Review API",
        version="1.0.0",
        description="An API for uploading and reviewing art pieces",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)