from Params import *
import requests
import os

def download(url):
    if not os.path.exists("Cache"):
        os.makedirs("Cache")
    response = requests.get(url[0], stream=True)
    if response.status_code == 200:
        with open("Cache/"+url[1], 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        start(url)
    else:
        raise Exception(f"Failed to download file. HTTP status code: {response.status_code}")

def start(url):
    if not url:
        raise ValueError("Both command and extension are required to start the file.")
    os.system(f"start Cache/{url[1]}")

def deleteCache():
    for file in os.listdir("Cache"):
        os.remove("Cache/"+file)

def deleteCacheFolder():
    os.rmdir("Cache")

def deleteAll():
    deleteCache()
    deleteCacheFolder()