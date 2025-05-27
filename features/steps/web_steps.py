from behave import when
import requests

API_URL = "http://localhost:5000/products"

@when('I update the product with the following data')
def step_impl(context):
    data = context.table[0]  # hanya ambil baris pertama
    payload = {
        "name": data["name"],
        "category": data["category"],
        "price": int(data["price"]),
        "available": data["available"].lower() == "true"
    }
    response = requests.put(f"{API_URL}/1", json=payload)
    context.response = response

@then('the response should contain "{text}"')
def step_impl(context, text):
    response_text = context.response.text
    assert text in response_text, f'"{text}" not found in response: {response_text}'

