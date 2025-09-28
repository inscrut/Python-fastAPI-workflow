from aiohttp import ClientSession

class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                'Authorization': api_key
            }
        )

class INVHTTPClient(HTTPClient):
    async def get_stock_by_sku(self, sku: str):
        async with self._session.get(
            "/api/stock/", 
            params={
                "in_stock": "true",
                "IPN": sku
            }
        ) as resp:
            result = await resp.json()
            return result
        
    async def get_parts(self):
        async with self._session.get(
            "/api/part/",
            params={
                "active": "true",
                "salable": "true"
            }
        ) as resp:
            result = await resp.json()
            return result