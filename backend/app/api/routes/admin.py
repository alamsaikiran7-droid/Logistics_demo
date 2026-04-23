from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.entities import Bid, Message, Shipment, User

router = APIRouter()


@router.get("/analytics")
def analytics(db: Session = Depends(get_db)):
    return {
        "users": db.scalar(select(func.count()).select_from(User)),
        "shipments": db.scalar(select(func.count()).select_from(Shipment)),
        "bids": db.scalar(select(func.count()).select_from(Bid)),
        "messages": db.scalar(select(func.count()).select_from(Message)),
    }
