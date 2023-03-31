import requests
import json

def generate_response(prompt):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': prompt}]
    }
    response = requests.post('https://chatgpt-api.shn.hk/v1/', headers=headers, data=json.dumps(data))
    print(response.text)
    response_data = json.loads(response.text)
    return response_data['messages'][0]['content']

while True:
    user_input = input("You: ")
    response = generate_response(user_input)
    print("Bot: " + response)

