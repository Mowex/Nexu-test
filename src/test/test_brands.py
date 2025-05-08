def test_create_brand(client):
    response = client.post("/brands/", json={"name": "Toyota"})
    assert response.status_code == 201
    assert response.json()["name"] == "Toyota"

def test_get_brands(client):
    response = client.get("/brands/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
