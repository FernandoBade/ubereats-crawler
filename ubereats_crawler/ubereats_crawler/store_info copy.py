import json
import requests


def get_store_ids():
    url = "https://www.ubereats.com/api/getSeoFeedV1"

    querystring = {"localeCode": "cl"}

    payload = {"pathname": "/cl/category/santiago-rm/fast-food"}
    headers = {
        "cookie": "uev2.id.xp=af1ae106-e9e8-436e-a9dc-8bcd3db4df99;",
        "authority": "www.ubereats.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.5",
        "content-type": "application/json",
        "origin": "https://www.ubereats.com",
        "referer": "https://www.ubereats.com/cl/category/santiago/fast-food",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "x-csrf-token": "x"
    }

    response = requests.request(
        "POST", url, json=payload, headers=headers, params=querystring)
    jsondata = json.loads(response.text)
    ids = jsondata["data"]["elements"][4]["storesMap"]

    store_list = []
    for store_id in ids:
        store_info = ids[store_id]
        uuid = store_id
        nome = store_info["title"]
        location = store_info["location"]["formattedAddress"]
        latitude = store_info["location"]["latitude"]
        longitude = store_info["location"]["longitude"]


        store = {
            "uuid": uuid,
            "nome": nome,
            "location": location,
            "latitude": latitude,
            "longitude": longitude,
        }

        store_list.append(store)

    store_dict = {"restaurants": store_list}
    json_output = json.dumps(store_dict)

    with open("restaurants.json", "w") as file:
        file.write(json_output)

    return list(ids.keys())


get_store_ids()