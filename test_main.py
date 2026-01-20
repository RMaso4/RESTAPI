import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_crypto_list():
    response = client.get("/crypto")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all("symbol" in coin and "name" in coin and "price" in coin for coin in data)

def test_get_crypto():
    response = client.get("/crypto/btc")
    assert response.status_code == 200
    data = response.json()
    assert data["symbol"] == "BTC"

def test_add_to_watchlist():
    coin = {"symbol": "XRP", "name": "Ripple"}
    response = client.post("/crypto", json=coin)
    assert response.status_code == 200
    data = response.json()
    assert data["symbol"] == "XRP"

def test_get_watchlist():
    response = client.get("/crypto/watchlist")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_update_watchlist():
    coin = {"symbol": "XRP", "name": "Ripple Updated"}
    response = client.put("/crypto/XRP", json=coin)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Ripple Updated"

def test_delete_from_watchlist():
    response = client.delete("/crypto/XRP")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Deleted"
