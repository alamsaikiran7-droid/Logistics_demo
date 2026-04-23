from sqlalchemy import select

from app.core.security import hash_password
from app.db.session import SessionLocal
from app.models.entities import RoleEnum, User


def seed_data() -> None:
    db = SessionLocal()
    try:
        existing = db.scalar(select(User).where(User.email == "admin@logistics.local"))
        if existing:
            return
        users = [
            User(
                name="Platform Admin",
                email="admin@logistics.local",
                password_hash=hash_password("admin123"),
                role=RoleEnum.admin,
            ),
            User(
                name="Alice Customer",
                email="customer@logistics.local",
                password_hash=hash_password("customer123"),
                role=RoleEnum.customer,
            ),
            User(
                name="TransMove Co",
                email="transporter@logistics.local",
                password_hash=hash_password("transporter123"),
                role=RoleEnum.transporter,
            ),
        ]
        db.add_all(users)
        db.commit()
    finally:
        db.close()
