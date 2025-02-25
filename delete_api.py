import requests
import json

api ="https://reqres.in/api"

authorization_token = "token token_value"

def delete_request(user_id):
    url = api + "/users/{user_id}"
    headers = {"Authorization" :authorization_token}
    # data = {
    #     "name": "Rushma",
    #     "job": "Quality assurance",
    #     "email":"rushma@gamil.com"
    # }
    response = requests.delete(url , headers=headers)
    json_data = response.json()
    # json_str = json.dumps(json_data, indent=4)
    assert response.status_code == 204
    # user_id= json_data["id"]

    print("the  deleted user is:", json_data)
    print("-----------------")
    print("user deleted successfully")

delete_request()