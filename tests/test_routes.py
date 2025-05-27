import unittest
from flask import Flask
from service.routes import app

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_read_product(self):
        response = self.client.get("/products/1")
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        # Simulasi payload update produk
        update_data = {
            "name": "Updated Printer",
            "category": "Office",
            "price": 1400000,
            "available": True
        }

        # Kirim PUT ke /products/1
        response = self.client.put("/products/1", json=update_data)
        self.assertEqual(response.status_code, 200)
        # Bisa tambah assertEqual untuk response JSON jika perlu

if __name__ == '__main__':
    unittest.main()

