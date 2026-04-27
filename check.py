import os
from google import genai

# Read the API key from the local file
try:
    with open("API_Key.txt", "r") as key_file:
        # .strip() removes any accidental spaces or newlines from the file
        my_api_key = key_file.read().strip() 
except FileNotFoundError:
    print("Error: API_Key.txt not found. Please create the file and add your API key.")
    exit()

# Initialize the client using the fetched key
client = genai.Client(api_key=my_api_key)

# Make the API call
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain the primary differences between MongoDB and MySQL in two short sentences."
)

print(response.text)