import pytest
import requests

BASE_URL = "https://crudcrud.com/api/f136ae283a064327826139c908ff68b6"

@pytest.fixture(scope="module")
def create_user():
    user = {
        "name": "Fixture QA",
        "email": "fixture@test.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=user)
    assert response.status_code ==201
    print(f"\n[REPORT JIRA] Create User Request - Status Code: {response.status_code}")
    user_id = response.json()["_id"]
    return user_id

def test_get_user(create_user):
    response = requests.get(f"{BASE_URL}/users/{create_user}")
    assert response.status_code == 200


def test_update_user(create_user):
    ''' tento kod sme nahradili predošlým kodom s fixture
    # CREATE
    user = {
        "name": "Pytest QA",
        "email": "pytest@test.com"
    }

    response = requests.post(f"{BASE_URL}/users", json=user)
    assert response.status_code == 201

    user_id = response.json()["_id"]

    # GET
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Pytest QA"
    '''
    # UPDATE
    updated_user = {
        "name": "Pytest QA Senior",
        "email": "pytest@test.com"
    }

    response = requests.put(f"{BASE_URL}/users/{create_user}", json=updated_user)
    assert response.status_code == 200
def test_delete_user(create_user):
    # DELETE
    response = requests.delete(f"{BASE_URL}/users/{create_user}")
    assert response.status_code == 200
def test_verify_delete(create_user):
    # VERIFY DELETE
    response = requests.get(f"{BASE_URL}/users/{create_user}")
    assert response.status_code == 404
