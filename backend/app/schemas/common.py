from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from app.models.entities import RoleEnum, ShipmentStatus


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: RoleEnum


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: RoleEnum


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ShipmentCreate(BaseModel):
    title: str
    pickup_location: str
    drop_location: str
    material_type: str
    weight_kg: float
    urgency: str


class ShipmentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    pickup_location: str
    drop_location: str
    material_type: str
    weight_kg: float
    urgency: str
    status: ShipmentStatus
    ai_price_estimate: float | None
    ai_summary: str | None
    created_at: datetime


class BidCreate(BaseModel):
    shipment_id: int
    amount: float
    eta_hours: int
    message: str


class BidOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    shipment_id: int
    transporter_id: int
    amount: float
    eta_hours: int
    message: str
    is_selected: bool


class ChatMessageCreate(BaseModel):
    shipment_id: int
    sender_id: int
    content: str


class ChatMessageOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    shipment_id: int
    sender_id: int
    content: str
    sent_at: datetime


class TrackingCreate(BaseModel):
    shipment_id: int
    status: str
    latitude: float
    longitude: float
    note: str


class AIQuery(BaseModel):
    question: str


class PaymentIntentResponse(BaseModel):
    shipment_id: int
    provider: str
    order_id: str
    status: str
