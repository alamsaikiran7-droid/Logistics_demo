from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.entities import Shipment, ShipmentStatus, TrackingEvent
from app.schemas.common import TrackingCreate

router = APIRouter()


@router.get("/{shipment_id}")
def get_tracking(shipment_id: int, db: Session = Depends(get_db)):
    query = select(TrackingEvent).where(TrackingEvent.shipment_id == shipment_id).order_by(TrackingEvent.created_at)
    items = list(db.scalars(query))
    return {"shipment_id": shipment_id, "events": items}


@router.post("/")
def update_tracking(payload: TrackingCreate, db: Session = Depends(get_db)):
    event = TrackingEvent(**payload.model_dump())
    db.add(event)
    shipment = db.get(Shipment, payload.shipment_id)
    if shipment and payload.status in ShipmentStatus._value2member_map_:
        shipment.status = ShipmentStatus(payload.status)
    db.commit()
    db.refresh(event)
    return event
