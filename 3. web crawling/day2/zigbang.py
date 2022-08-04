import requests
import pandas as pd
import geohash2

def oneroom(addr):
    url = f"https://apis.zigbang.com/v2/search?leaseYn=N&q={addr}&serviceType=원룸"

    response = requests.get(url)
    data = response.json()["items"][0]
    lat, lng = data["lat"], data["lng"]
    
    geohash = geohash2.encode(lat, lng, precision=5) # precision default 값 : 12
    
    url = f"https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang\
&geohash={geohash}&needHasNoFiltered=true&rent_gteq=0&sales_type_in=전세|월세&service_type_eq=원룸"
    response = requests.get(url)
    items = response.json()["items"]
    item_id = [item["item_id"] for item in items]
    
    url = "https://apis.zigbang.com/v2/items/list"

    params = {
        "domain": "zigbang",
        "withCoalition": "true",
        "item_ids": item_id[:900]
    }

    response = requests.post(url, data=params)
    items = response.json()["items"]
    columns = ["item_id", "sales_type", "deposit", "rent", "size_m2", "address1", "manage_cost"]
    addr = "마포구 합정동"
    df =pd.DataFrame(items)[columns]
    df_filtered = df[df["address1"].str.contains(addr)].reset_index(drop=True)
    return df_filtered
