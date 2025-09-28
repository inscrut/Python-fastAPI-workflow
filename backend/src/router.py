from fastapi import APIRouter
from src.init import inv_client
from src.db_driver import engine, Base, PartAddSchema, PartSchema, SessionDep, PartModel
from sqlalchemy import select

router = APIRouter(
    prefix="/inv"
)

@router.get("/parts")
async def get_parts_list():
    return await inv_client.get_parts()

@router.get("/search/sku/{sku_id}")
async def search_stock_by_sku(sku_id: str):
    return await inv_client.get_stock_by_sku(sku_id)

@router.post("/db/setup")
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"status": True}


@router.post("/db/part/add")
async def part_db_add(data: PartAddSchema, session: SessionDep):
    new_part = PartModel(
        name=data.name,
        IPN=data.IPN,
        link=data.link
    )
    session.add(new_part)
    await session.commit()

    return {"status":True}

@router.get("/db/part/get")
async def part_db_get(session: SessionDep):
    query = select(PartModel)
    result = await session.execute(query)

    return result.scalars().all()