import requests
import json

api ="https://reqres.in/api"

authorization_token = "token token_value"

def put_request():
    url = api + "/users/{user_id}"
    headers = {"Authorization" :authorization_token}
    data = {
        "name": "Rushma",
        "job": "Quality assurance",
        "email":"rushma@gamil.com"
    }
    response = requests.put(url , json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    assert response.status_code == 200
    # user_id= json_data["id"]

    print("the  updated user is:", json_str)
    print("-----------------")
    # print("the id for new user is:", user_id)

put_request()