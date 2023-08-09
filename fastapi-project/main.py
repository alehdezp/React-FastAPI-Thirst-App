from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from routers import drinks

app = FastAPI()

# Routers
app.include_router(drinks.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


"""@app.post("/buy")
async def buy_drink(drink_name: str, money_total: float):
    # Check if the drink is in the inventory
    if not any(drink.drink_type == drink_name for drink in inventory.drink_list):
        raise HTTPException(
            status_code=404,
            detail=f"Unfortunately, we don't have {drink_name} in our inventory",
        )
    drink_to_buy = list(
        filter(lambda drink: drink.drink_type == drink_name, inventory.drink_list)
    )[0]
    if drink_to_buy.amount > money_total:
        raise HTTPException(
            status_code=402,
            detail=f"Unfortunately, you don't enough money to buy a {drink_to_buy.drink_type}",
        )

    change_amount = money_total - drink_to_buy.amount
    # return all the drinks below the amount of money
    return {
        "status": "Accepted",
        "msg": f"Thanks for buying a {drink_to_buy.drink_type}. Your change is {change_amount}",
    }
"""
