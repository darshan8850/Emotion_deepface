# from youdotcom import Chat # import all the classes

# chat = Chat.send_message(message="how is your day?", api_key="BSSJG6RTBHVWED5DL09P3WVSD4DFOTOWIBY") # send a message to YouChat. passing the message and your api key.

# # you can get an api key form the site: https://api.betterapi.net/ (with is also made by me)

# print(chat)  # returns the message and some other data

from youdotcom import Chat # import all the classes
import requests # import requests for the api call
API_KEY = "BSSJG6RTBHVWED5DL09P3WVSD4DFOTOWIBY" # your api key

url = "https://api.betterapi.net/youdotcom/chat?message=hello&key=" + API_KEY # set api url
json = requests.get(url).json() # load json form api

print(json.keys()) # print -> dict_keys(['error'])

print(json["error"]) # print -> Error, not likly made by you: not enough values to unpack (expected 2, got 1)

print(json["message"]) # print -> KeyError: 'message'