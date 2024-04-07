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
    headers={'content-Type':'application/json'}
    r = requests.get(url=URL, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        print(data)
    else:
        print("Failed to get data. Status code:", r.status_code)

# get_data(1)

def post_data():
    data={
        'name': 'Shahyan',
        'roll': 105,
        'city': 'peshawar'
    }
    headers={'content-Type':'application/json'}
    json_data= json.dumps(data)
    r= requests.post(url= URL, headers=headers, data= json_data)
    data= r.json()
    print(data)

post_data()

def update_data():
    data={
        'id': 1,
        'name': 'Ahmed',
        'city':'Thatta'
    }
    headers={'content-Type':'application/json'}
    json_data= json.dumps(data)
    r= requests.put(url= URL,headers=headers, data= json_data)
    data= r.json()
    print(data)

# update_data()
    
def delete_data():
    data={
        'id': 4
    }
    json_data= json.dumps(data)
    headers={'content-Type':'application/json'}
    r= requests.delete(url= URL, headers=headers, data= json_data)
    data= r.json()
    print(data)

# delete_data()