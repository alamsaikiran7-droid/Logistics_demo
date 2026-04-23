from collections import defaultdict

from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.entities import Message
from app.schemas.common import ChatMessageCreate, ChatMessageOut

router = APIRouter()
active_connections: dict[int, list[WebSocket]] = defaultdict(list)


@router.get("/{shipment_id}", response_model=list[ChatMessageOut])
def get_messages(shipment_id: int, db: Session = Depends(get_db)):
    query = select(Message).where(Message.shipment_id == shipment_id).order_by(Message.sent_at)
    return list(db.scalars(query))


@router.post("/messages", response_model=ChatMessageOut)
def create_message(payload: ChatMessageCreate, db: Session = Depends(get_db)):
    message = Message(**payload.model_dump())
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


@router.websocket("/ws/{shipment_id}")
async def websocket_chat(websocket: WebSocket, shipment_id: int):
    await websocket.accept()
    active_connections[shipment_id].append(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            for connection in active_connections[shipment_id]:
                await connection.send_json(data)
    except WebSocketDisconnect:
        active_connections[shipment_id].remove(websocket)
