from src.http_client import INVHTTPClient
from src.config import settings

inv_client = INVHTTPClient(
    base_url=settings.INV_IP,
    api_key=settings.API_KEY_INVENTREE
)