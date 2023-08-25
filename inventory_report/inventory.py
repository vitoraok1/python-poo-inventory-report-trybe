from inventory_report.product import Product
from typing import Optional


class Inventory:
    def __init__(self, data: Optional[list[Product]] = None) -> None:
        self._data = data if data is not None else []

    @property
    def data(self) -> list[Product]:
        return self._data

    def add_data(self, data: list[Product]) -> None:
        self._data.extend(data)
