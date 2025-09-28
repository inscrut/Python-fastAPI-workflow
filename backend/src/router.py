from fastapi import APIRouter
from src.init import inv_client

router = APIRouter(
    prefix="/inv"
)

@router.get("/parts")
async def get_parts_list():
    return await inv_client.get_parts()

@router.get("/search/sku/{sku_id}")
async def search_stock_by_sku(sku_id: str):
    return await inv_client.get_stock_by_sku(sku_id)
