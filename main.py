from fastapi import FastAPI
from app.routes import router


app = FastAPI(title="Auto File Organizer Api")

app.include_router(router)