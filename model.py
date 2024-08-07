from pydantic import BaseModel


class ShopItem(BaseModel):
    name: str
    description: str | None = None
    price: int
    tax: float | None = None
