import requests
from datetime import datetime
USERNAME = "jan0fu"
TOKEN = "9jf0sdf3jslf43jds34jdsf4s78"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.5"
}
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#response = requests.post(url=post_endpoint, json=post_config, headers=headers)

put_date = "20221212"
put_config = {"quantity": "1.0"}
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{put_date}"
response = requests.put(url=put_endpoint, json=put_config, headers=headers)
print((response.text))
