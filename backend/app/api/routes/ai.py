from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.entities import Message, Shipment
from app.schemas.common import AIQuery
from app.services.ai import answer_logistics_question, summarize_dispute

router = APIRouter()


@router.post("/chatbot")
def logistics_chatbot(payload: AIQuery):
    return answer_logistics_question(payload.question)


@router.get("/shipments/{shipment_id}/summary")
def shipment_summary(shipment_id: int, db: Session = Depends(get_db)):
    shipment = db.get(Shipment, shipment_id)
    return {"shipment_id": shipment_id, "summary": shipment.ai_summary if shipment else "Shipment not found"}


@router.get("/disputes/{shipment_id}/analyze")
def dispute_analysis(shipment_id: int, db: Session = Depends(get_db)):
    query = select(Message.content).where(Message.shipment_id == shipment_id)
    messages = list(db.scalars(query))
    return summarize_dispute(messages)
