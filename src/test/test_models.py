def test_create_model_for_brand(client):    
    brand_resp = client.post("/brands/", json={"name": "Honda"})
    brand_id = brand_resp.json()["id"]

    model_resp = client.post(f"/brands/{brand_id}/models", json={
        "name": "Civic",
        "average_price": 25000
    })
    assert model_resp.status_code == 201
    assert model_resp.json()["name"] == "Civic"

def test_get_models_by_brand(client):
    brand_resp = client.post("/brands/", json={"name": "Mazda"})
    brand_id = brand_resp.json()["id"]
    client.post(f"/brands/{brand_id}/models", json={
        "name": "Mazda 3",
        "average_price": 23000
    })

    response = client.get(f"/brands/{brand_id}/models")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
