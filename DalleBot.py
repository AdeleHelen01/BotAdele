import requests
import time
import os
#from PIL import Image

with open("keys.txt") as f:
    # converting our text file to a list of lines
    lines = f.read().split('\n')
    # openai api key
    api_key = lines[0]
    # discord token
    DISCORD_TOKEN = lines[1]
    api_base = lines[2]
# close the file
f.close()


api_version = '2022-08-03-preview'
url = "{}dalle/text-to-image?api-version={}".format(api_base, api_version)
headers= { "api-key": api_key, "Content-Type": "application/json" }
body = {
    "caption": " fat cat eating a carrot",
    "resolution": "1024x1024"
}
submission = requests.post(url, headers=headers, json=body)
operation_location = submission.headers['Operation-Location']
retry_after = submission.headers['Retry-after']
status = ""
while (status != "Succeeded"):
    time.sleep(int(retry_after))
    response = requests.get(operation_location, headers=headers)
    status = response.json()['status']
image_url = response.json()['result']['contentUrl']
print(image_url)
#data = requests.get(image_url).content

#f = open('img.jpg', 'wb')
#f.write(data)
# f.close()