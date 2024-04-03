# import requests
import json

# URL= "http://127.0.0.1:8000/studentapi/"

# def get_data(id = None):
#     data= {}
#     if id is not None:
#         data= {'id': id}
#     json_data= json.dumps(data)
#     r= requests.get(url= URL, data= json_data)
#     data= r.json()
#     print(data)

# get_data()

import requests

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    params = {}
    if id is not None:
        params = {'id': id}
    r = requests.get(url=URL, params=params)
    if r.status_code == 200:
        data = r.json()
        print(data)
    else:
        print("Failed to get data. Status code:", r.status_code)

# get_data()

def post_data():
    data={
        'name': 'haseeb',
        'roll': 110,
        'city': 'karachi'
    }
    json_data= json.dumps(data)
    r= requests.post(url= URL, data= json_data)
    data= r.json()
    print(data)

post_data()

def update_data():
    data={
        'id': 10,
        'roll': 109
    }
    json_data= json.dumps(data)
    r= requests.put(url= URL, data= json_data)
    data= r.json()
    print(data)

# update_data()
    
def delete_data():
    data={
        'id': 10
    }
    json_data= json.dumps(data)
    r= requests.delete(url= URL, data= json_data)
    data= r.json()
    print(data)

# delete_data()