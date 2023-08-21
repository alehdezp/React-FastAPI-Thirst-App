import os
import json
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import HTTPException

from database import get_drinks_db


router = APIRouter(
    prefix="/drinks", tags=["drinks"], responses={404: {"description": "Not found"}}
)


class Drink(BaseModel):
    drink_type: str
    description_drink: Optional[str] = None
    amount: float
    description_amount: Optional[str] = None


class InventoryDrinks(BaseModel):
    drink_list: list[Drink]


# Ruta para obtener todas las bebidas
@router.get(
    "/", response_model=list[Drink], description="Get all drinks from the inventory"
)
async def get_drinks():
    try:
        drinks_db = get_drinks_db()
        inventory = list(drinks_db.find({}))
        return inventory
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# TODO: Change the whole program to use mongodb instead the JSON file
@router.post("/{drink_type}")
async def new_drink(
    drink_type: str,
    amount: int,
    description_drink: Optional[str] = None,
    description_amount: Optional[str] = None,
):
    drink_type = drink_type.lower()
    if drink_type in [drink.drink_type.lower() for drink in inventory.drink_list]:
        raise HTTPException(
            status_code=409,
            detail=f"The drink {drink_type} already exists in the inventory",
        )

    drink = Drink(
        drink_type=drink_type,
        description_drink=description_drink,
        amount=amount,
        description_amount=description_amount,
    )

    inventory.drink_list.append(drink)
    # Respond in json format
    return {"status": "OK", "msg": "Drink added"}


@router.get("/{drink_type}")
async def get_drink(drink_type: str):
    drink_type = drink_type.lower()
    # Check if the drink is in the inventory
    if not any(
        drink.drink_type.lower() == drink_type for drink in inventory.drink_list
    ):
        raise HTTPException(
            status_code=404,
            detail=f"Unfortunately, we don't have {drink_type} in our inventory",
        )

    drink = list(
        filter(
            lambda drink: drink.drink_type.lower() == drink_type, inventory.drink_list
        )
    )[0]

    return drink


# create the put method
@router.put("/{drink_type}")
async def update_drink(
    drink_type: str, amount: int, description_drink: str, description_amount: str
):
    drink_type = drink_type.lower()
    # Check if the drink is in the inventory
    if not any(
        drink.drink_type.lower() == drink_type for drink in inventory.drink_list
    ):
        raise HTTPException(
            status_code=404,
            detail=f"Unfortunately, we don't have {drink_type} in our inventory",
        )

    drink_to_update = list(
        filter(
            lambda drink: drink.drink_type.lower() == drink_type, inventory.drink_list
        )
    )[0]

    drink_to_update.amount = amount
    drink_to_update.description_drink = description_drink
    drink_to_update.description_amount = description_amount

    return {"status": "OK", "msg": "Drink updated"}


@router.delete("/{drink_type}")
async def delete_drink(drink_type: str):
    drink_type = drink_type.lower()
    # Check if the drink is in the inventory
    if not any(
        drink.drink_type.lower() == drink_type for drink in inventory.drink_list
    ):
        raise HTTPException(
            status_code=404,
            detail=f"Unfortunately, we don't have {drink_type} in our inventory",
        )

    drink_to_delete = list(
        filter(
            lambda drink: drink.drink_type.lower() == drink_type, inventory.drink_list
        )
    )[0]

    inventory.drink_list.remove(drink_to_delete)

    return {"status": "OK", "msg": "Drink deleted"}


current_path = os.getcwd()
json_path = "/src/bebidas.json"
full_path = current_path + json_path


# Leer el archivo JSON y almacenar los datos en una lista de objetos Drink
with open(full_path, "r") as file:
    bebidas_data = json.load(file)
# Crear una instancia de InventoryDrinks con los datos del archivo JSON
inventory = InventoryDrinks(drink_list=bebidas_data)
