import requests

# Data to send to the API
post_data = {
    "title": "New Post",
    "body": "This is the content of the post!",
    "userId": 1
    }

# Sending a POST request
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json=post_data # Automatically converts the dictionary to a JSON string!
    )

print("Response:", response.json())
