from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        "000",
        "Product Name",
        "Company Name",
        "2023-08-25",
        "2023-12-31",
        "ABC123DEF456",
        "Keep in a cool and dry place",
    )

    assert product.id == "000"
    assert product.product_name == "Product Name"
    assert product.company_name == "Company Name"
    assert product.manufacturing_date == "2023-08-25"
    assert product.expiration_date == "2023-12-31"
    assert product.serial_number == "ABC123DEF456"
    assert product.storage_instructions == "Keep in a cool and dry place"
