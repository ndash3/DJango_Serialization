import requests
import json

url = 'http://127.0.0.1:8000/get/'

def get_method(id=None):
    data = {}
    if data is not None:
        data['id'] = id
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    new_data = r.json()
    print(new_data)

def post_request():
    data = {
        'name':'Pankaj',
        'city':'Bangalore',
        'rewards':35
    }
    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data)
    new_data = r.json()
    print(new_data)

def put_request():
    data = {
        'id':'2',
        'rewards':45
    }
    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data)
    new_data = r.json()
    print(new_data)

def delete_request():
    data = {'id':2}
    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    new_data = r.json()
    print(new_data)

if __name__ == '__main__':
    #get_method()
    #post_request()
    #put_request()
    delete_request()