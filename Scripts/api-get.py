import requests                             # Import the requests library

# Fetch data from an example JSON API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Parse JSON response
json_data = response.json()

# Access specific fields in the JSON data
print("Post Title:", json_data["title"])    # Output: Post Title: Example Title
print("Post Body:", json_data["body"])      # Output: Post Body: Example Body

