from fastapi import APIRouter
from src.services.recipes_service import RecipeService

router = APIRouter()
recipes_service = RecipeService()

@router.post("/start")
def start_recipe(flavor: str, liters: int):
    response = recipes_service.start(flavor, liters)

    return {"mensagem": f"Recipe enviado para o tópico"}