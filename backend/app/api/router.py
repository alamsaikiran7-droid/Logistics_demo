from fastapi import APIRouter

from app.api.routes import admin, ai, auth, bids, chat, shipments, tracking

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(shipments.router, prefix="/shipments", tags=["shipments"])
api_router.include_router(bids.router, prefix="/bids", tags=["bids"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])
api_router.include_router(tracking.router, prefix="/tracking", tags=["tracking"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
