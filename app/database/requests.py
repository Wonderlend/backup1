from app.database.models import async_session
from sqlalchemy import select, update
from app.database.models import User


async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def send_photo_to_user(bot, chat_id, photo_url, caption):
    await bot.send_photo(chat_id=chat_id, photo=photo_url, caption=caption)


async def get_day(tg_id: int):
    async with async_session() as session:
        day = await session.scalar(select(User.day).where(User.tg_id == tg_id))
        return day


async def update_day(tg_id: int, new_day: int):
    async with async_session() as session:
        stmt = update(User).where(User.tg_id == tg_id).values(day=new_day)
        result = await session.execute(stmt)
        await session.commit()
