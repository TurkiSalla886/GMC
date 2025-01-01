import requests

# Salla API URL for reviews
api_url = "https://api.salla.dev/v1/products/reviews"
headers = {"Authorization": "Bearer cd9e490b65ee8632dc6182a404e6c84d"}

# Fetch reviews
response = requests.get(api_url, headers=headers)
reviews = response.json()
print(reviews)  # Output the reviews
