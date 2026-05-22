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

