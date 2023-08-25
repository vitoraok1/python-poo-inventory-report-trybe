from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product

""" abstract method importer reference:
https://docs.python.org/pt-br/3.7/library/abc.html"""


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        ...


class JsonImporter:
    pass


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
