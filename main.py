import requests
import json

# 1. Fetch data from the Affiliate API (e.g., Amazon, Impact, etc.)
def get_latest_deals():
    # Use your API credentials here
    # This is a placeholder for your actual API request
    response = requests.get("YOUR_AFFILIATE_API_ENDPOINT")
    return response.json()

# 2. Save the data to a JSON file
def update_store_data():
    data = get_latest_deals()
    with open('data/products.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    update_store_data()
import json
import random

# Your unique logic: This is where you would call an API
# For now, this generates a random "test" product to prove the automation works
def generate_test_product():
    new_product = {
        "id": random.randint(100, 999),
        "title": "New Featured Gadget",
        "description": "This deal was added automatically by your bot!",
        "price": "₹" + str(random.randint(1000, 5000)),
        "image": "https://via.placeholder.com/250",
        "affiliate_link": "#"
    }
    return [new_product]

# Save to your data file
with open('data.json', 'w') as f:
    json.dump(generate_test_product(), f, indent=4)

