from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.entities import Bid, Shipment, ShipmentStatus
from app.schemas.common import BidCreate, BidOut, PaymentIntentResponse
from app.services.ai import rank_bid

router = APIRouter()


@router.get("/", response_model=list[BidOut])
def list_bids(db: Session = Depends(get_db)):
    return list(db.scalars(select(Bid)))


@router.post("/", response_model=BidOut)
def create_bid(payload: BidCreate, transporter_id: int = 3, db: Session = Depends(get_db)):
    shipment = db.get(Shipment, payload.shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    bid = Bid(
        shipment_id=payload.shipment_id,
        transporter_id=transporter_id,
        amount=payload.amount,
        eta_hours=payload.eta_hours,
        message=payload.message,
    )
    db.add(bid)
    db.commit()
    db.refresh(bid)
    return bid


@router.post("/{bid_id}/accept", response_model=PaymentIntentResponse)
def accept_bid(bid_id: int, db: Session = Depends(get_db)):
    bid = db.get(Bid, bid_id)
    if not bid:
        raise HTTPException(status_code=404, detail="Bid not found")
    bid.is_selected = True
    bid.shipment.status = ShipmentStatus.assigned
    db.commit()
    return PaymentIntentResponse(
        shipment_id=bid.shipment_id,
        provider="mock-razorpay",
        order_id=f"order_{bid.id}_{bid.shipment_id}",
        status="created",
    )


@router.get("/{bid_id}/rank")
def get_bid_rank(bid_id: int, db: Session = Depends(get_db)):
    bid = db.get(Bid, bid_id)
    if not bid:
        raise HTTPException(status_code=404, detail="Bid not found")
    return rank_bid(bid.amount, bid.eta_hours)
