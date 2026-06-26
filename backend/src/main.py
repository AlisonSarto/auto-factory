from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.mqtt import iniciar_mqtt
from src.controllers.api_router import router

iniciar_mqtt()

app = FastAPI(
    title="Central da Fábrica API",
    description="API central da fábrica"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Servidor da fábrica online"}

app.include_router(router)