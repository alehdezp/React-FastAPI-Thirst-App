import os
import json
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

drinks = APIRouter()


class Drink(BaseModel):
    drink_type: str
    description_drink: Optional[str] = None
    amount: float
    description_amount: Optional[str] = None


class InventoryDrinks(BaseModel):
    drink_list: list[Drink]


# Ruta para obtener todas las bebidas
@drinks.get("/drinks")
async def get_drinks():
    return inventory


# Ruta al archivo JSON, home path + /Projects/REACT-FASTAPI-THIRST-APP/fastapi-project/src/bebidas.json
# home path
home_path = os.path.expanduser("~")
file_path = "/Proyectos/React-FastAPI-Thirst-App/fastapi-project/src/bebidas.json"
full_path = home_path + file_path


# Leer el archivo JSON y almacenar los datos en una lista de objetos Drink
with open(full_path, "r") as file:
    bebidas_data = json.load(file)
# Crear una instancia de InventoryDrinks con los datos del archivo JSON
inventory = InventoryDrinks(drink_list=bebidas_data)
