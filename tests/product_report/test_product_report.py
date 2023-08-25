from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        "000",
        "Product Name",
        "Company Name",
        "2023-08-25",
        "2023-12-31",
        "ABC123DEF456",
        "Keep in a cool and dry place",
    )
    expected_string = (
        "The product 000 - Product Name with serial number ABC123DEF456 "
        "manufactured on 2023-08-25 by the company Company Name "
        "valid until 2023-12-31 must be stored according to the following "
        "instructions: Keep in a cool and dry place."
    )

    actual_string = str(product)

    assert actual_string == expected_string
