# src/controllers/api_router.py
from fastapi import APIRouter

from src.controllers.api import recipes

router = APIRouter(prefix="/api")

router.include_router(
    recipes.router,
    prefix="/recipes",
    tags=["Preparo de receitas"]
)