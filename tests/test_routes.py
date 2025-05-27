import unittest
from flask import Flask
from service.routes import app

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_read_product(self):
        response = self.client.get("/products/1")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

