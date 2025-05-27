from behave import given
import requests

API_URL = "http://localhost:5000/products"

@given('the following products')
def step_impl(context):
    for row in context.table:
        payload = {
            "name": row['name'],
            "category": row['category'],
            "price": int(row['price']),
            "available": row['available'].lower() == "true"
        }
        response = requests.post(API_URL, json=payload)
        assert response.status_code == 201

