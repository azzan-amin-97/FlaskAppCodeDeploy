import requests


def test_index():
    response = requests.get("http://127.1:5000/")
    assert response.status_code == 200
