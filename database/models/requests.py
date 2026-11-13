from database.engine import async_session
from database.models.message import Message
from sqlalchemy import select

async def save_message(user_id: int,role:str, content:str ):
    async with async_session() as session:
        message = Message(
            user_id=user_id,
            role=role,
            content=content
        )
        session.add(message)
        await session.commit()

async def get_user_messages(user_id: int):
    async with async_session() as session:
        selected_message = await session.execute(select(Message).where(Message.user_id == user_id).order_by(Message.id.desc()).limit(10))
        message = selected_message.scalars().all()
        message.reverse()
        return message