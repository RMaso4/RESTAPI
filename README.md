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

1. Activeer de virtual environment:

   **PowerShell:**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   **Command Prompt:**
   ```cmd
   .\.venv\Scripts\activate.bat
   ```

   Als je een execution policy error krijgt in PowerShell, run dan eerst:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

2. Installeer dependencies (als de venv actief is):
   ```bash
   pip install -r requirements.txt
   ```

3. Start de server:
   ```bash
   uvicorn main:app --reload
   ```

   **Let op:** Je kunt FastAPI niet starten met `python main.py` - je moet `uvicorn main:app --reload` gebruiken omdat FastAPI een ASGI framework is.

4. Open de API:
   - API endpoints: `http://127.0.0.1:8000/crypto`
   - Interactieve documentatie: `http://127.0.0.1:8000/docs`

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
