from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.entities import Shipment, User
from app.schemas.common import ShipmentCreate, ShipmentOut
from app.services.ai import estimate_price, generate_shipment_summary

router = APIRouter()


@router.get("/", response_model=list[ShipmentOut])
def list_shipments(db: Session = Depends(get_db)):
    return list(db.scalars(select(Shipment).order_by(Shipment.created_at.desc())))


@router.post("/", response_model=ShipmentOut)
def create_shipment(payload: ShipmentCreate, customer_id: int = 2, db: Session = Depends(get_db)):
    customer = db.get(User, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    shipment = Shipment(
        customer_id=customer.id,
        title=payload.title,
        pickup_location=payload.pickup_location,
        drop_location=payload.drop_location,
        material_type=payload.material_type,
        weight_kg=payload.weight_kg,
        urgency=payload.urgency,
        ai_price_estimate=estimate_price(payload.weight_kg, payload.urgency),
        ai_summary=generate_shipment_summary(
            payload.title,
            payload.pickup_location,
            payload.drop_location,
            payload.material_type,
        ),
    )
    db.add(shipment)
    db.commit()
    db.refresh(shipment)
    return shipment
