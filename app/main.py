import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session

from .kafka_producer import producer
from .kafka_consumer import consumer
from .models import SessionLocal, Message, create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code (previously in @app.on_event("startup"))
    create_tables()
    await producer.start()
    await consumer.start()

    yield  # This line separates startup from shutdown logic

    # Shutdown code (previously in @app.on_event("shutdown"))
    await producer.stop()
    await consumer.stop()
app = FastAPI(title="DDD Python Env Demo", lifespan=lifespan)


class MessageSchema(BaseModel):
    content: str


class MessageResponse(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@app.post("/messages/", response_model=MessageResponse)
async def create_message(message: MessageSchema):
    await producer.send_message({"content": message.content})
    return {"id": 0, "content": message.content}  # ID will be assigned by Kafka consumer


@app.get("/messages/", response_model=List[MessageResponse])
def get_messages(db: Session = Depends(get_db)):
    messages = db.query(Message).all()
    return messages


@app.get("/health/")
def health_check():
    return {"status": "ok"}
