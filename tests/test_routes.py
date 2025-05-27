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

    def test_delete_product(self):
        response = self.client.delete("/products/1")
        self.assertEqual(response.status_code, 204)  # Atau 200 tergantung implementasi kamu

    def test_list_all_products(self):
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)
        # Optional: cek apakah response JSON berisi list
        self.assertIsInstance(response.get_json(), list)

    def test_list_by_name(self):
        response = self.client.get("/products?name=Printer")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        for item in data:
            self.assertEqual(item["name"], "Printer")

    def test_list_by_category(self):
        response = self.client.get("/products?category=Office")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        for item in data:
            self.assertEqual(item["category"], "Office")

    def test_list_by_availability(self):
        response = self.client.get("/products?available=true")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        for item in data:
            self.assertTrue(item["available"])

if __name__ == '__main__':
    unittest.main()

