import requests
import json


api ="https://reqres.in/api"
# api ="https://reqres.in/api/users/2"
# api ="https://reqres.in/api/users?per_page=7"

authorization_token = "token = any_token"

def get_request():
    url = api + "/users/"
    headers = {"Authorization" :authorization_token}
    data = {
        "name": "John",
        "job": "QA",
        "email":"john@gamil.com"
    }
    response = requests.post(url , json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    assert response.status_code == 201
    user_id= json_data["id"]

    print("the  new users posted for the api are:", json_str)
    print("-----------------")
    print("the id for new user is:", user_id)


get_request()