import requests
import pandas as pd
import json 

url = "https://worldometers.p.rapidapi.com/api/coronavirus/all/"

headers = {
    'x-rapidapi-host': "worldometers.p.rapidapi.com",
    'x-rapidapi-key': "0ebb74a56fmsh74eab977745ee42p1c8cc5jsnbeb2afa3f613"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

json_data = json.loads(response.text)

Data = pd.DataFrame(json_data['data'])