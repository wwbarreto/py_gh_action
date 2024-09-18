from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_create_product():
	response = client.post("/api/v1/products/",
		json={
			"name": "Coquinha Café",
			"description": "Muito bom",
			"price": 2
		})
	assert response.status_code == 200
	assert response.json()["name"] == "Coquinha Café"

def test_get_product():
	response = client.get("/api/v1/products/")
	assert response.status_code == 200

