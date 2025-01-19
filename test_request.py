import requests
import json

# URL of your Flask app's endpoint
url = "http://localhost:5000/webhook/customers"

# Data to send in the request
data = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

# Send POST request
response = requests.post(url, json=data)

# Print the response
print(response.status_code)  # Should be 200 if successful
print(response.json())  # Print the JSON response

