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

if __name__ == '__main__':
    unittest.main()

