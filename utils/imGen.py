import json
import random
import requests

def getShiba():
        urls=json.loads(requests.get(f"https://shibe.online/api/shibes?count=1&httpsUrls=true").content)[0]
        if urls:
            return urls

# PATCH API-FUNCTIONCALL-TIMEOUT
# def getMeows():
#     urls=json.loads(requests.get("https://cataas.com/cat?json=true").content)["url"]
#     if urls:
#         return "https://cataas.com"+urls

def getDog():
    urls=json.loads(requests.get("https://dog.ceo/api/breeds/image/random").content)["message"]
    if urls:
        return urls

def getFox():
    urls=json.loads(requests.get("https://randomfox.ca/floof/").content)["image"]
    if urls:
        return urls
