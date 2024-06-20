import requests

# Define the API URL
url = "https://quotes.rest/qod?language=en"

# Define your API key
auth_key = "ScrpUJv03VwS1EyA2WsvyZbqi6UttrhlvJPOjwsr"

# Define the headers with the authorization key
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {auth_key}"
}

# Make the GET request with the headers
res = requests.get(url=url, headers=headers)

# # Check the status code of the response
# if res.status_code == 200:
#     # Print the response in JSON format
#     print(res.json())
# else:
#     # Print an error message if the request failed
#     print(f"Error: {res.status_code} - {res.text}")

data = res.json

print(data)