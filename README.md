# Cryptocurrency REST API

Deze API geeft informatie over populaire cryptocurrency prijzen en biedt een eenvoudige watchlist functionaliteit.

## Functionaliteit

- **GET /crypto**: Lijst van populaire coins met naam, symbool, prijs, en 24h verandering
- **GET /crypto/{symbol}**: Prijs van één specifieke coin
- **POST /crypto**: Voeg een coin toe aan je watchlist
- **GET /crypto/watchlist**: Bekijk je watchlist
- **PUT /crypto/{symbol}**: Update een coin in je watchlist
- **DELETE /crypto/{symbol}**: Verwijder een coin uit je watchlist

Data wordt opgehaald via de CoinGecko API.

## Installatie

1. Installeer dependencies:
   ```
pip install -r requirements.txt
   ```
2. Start de server:
   ```
uvicorn main:app --reload
   ```

## Testen

Tests zijn geschreven met pytest en FastAPI TestClient.

```bash
pytest test_main.py
```

## Voorbeeld response

GET /crypto:
```json
[
  {"symbol": "BTC", "name": "Bitcoin", "price": 27000, "change": 2.3},
  {"symbol": "ETH", "name": "Ethereum", "price": 1800, "change": -1.2}
]
```

## Testrapport

Zie `testrapport.txt` voor testresultaten per release.

## Externe API
- [CoinGecko API](https://www.coingecko.com/en/api)

## Postman/cURL
Voorbeeld cURL:
```bash
curl http://127.0.0.1:8000/crypto
```

## Github
Upload deze map naar je eigen Github repository en deel de link.
