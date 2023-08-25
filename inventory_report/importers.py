from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json

""" abstract method importer reference:
https://docs.python.org/pt-br/3.7/library/abc.html"""


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        ...


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path) as file:
            data = json.load(file)

        return [
            Product(
                id=element["id"],
                product_name=element["product_name"],
                company_name=element["company_name"],
                manufacturing_date=element["manufacturing_date"],
                expiration_date=element["expiration_date"],
                serial_number=element["serial_number"],
                storage_instructions=element["storage_instructions"],
            )
            for element in data
        ]


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
