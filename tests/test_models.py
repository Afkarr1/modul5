import unittest
from service.models import Product

class TestProductModel(unittest.TestCase):

    def test_read_product(self):
        product = Product(name="Printer", category="Office", price=1200000, available=True)
        self.assertEqual(product.name, "Printer")
        self.assertEqual(product.category, "Office")
        self.assertEqual(product.price, 1200000)
        self.assertTrue(product.available)

    def test_update_product(self):
        product = Product(name="Printer", category="Office", price=1200000, available=True)
        product.name = "Laser Printer"
        product.price = 1500000
        self.assertEqual(product.name, "Laser Printer")
        self.assertEqual(product.price, 1500000)

    def test_delete_product(self):
        products = []
        product1 = Product(name="Printer", category="Office", price=1200000, available=True)
        product2 = Product(name="Scanner", category="Office", price=900000, available=True)
        products.append(product1)
        products.append(product2)
        products.remove(product1)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, "Scanner")

    def test_list_all_products(self):
        products = [
            Product(name="Printer", category="Office", price=1200000, available=True),
            Product(name="Scanner", category="Office", price=900000, available=True),
            Product(name="Xerox", category="Office", price=5000000, available=False)
        ]

        self.assertEqual(len(products), 3)
        self.assertEqual(products[0].name, "Printer")
        self.assertEqual(products[1].name, "Scanner")
        self.assertEqual(products[2].name, "Xerox")


if __name__ == '__main__':
    unittest.main()

