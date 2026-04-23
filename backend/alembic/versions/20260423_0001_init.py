"""initial schema"""

from alembic import op
import sqlalchemy as sa

revision = "20260423_0001"
down_revision = None
branch_labels = None
depends_on = None


role_enum = sa.Enum("customer", "transporter", "admin", name="roleenum")
shipment_status_enum = sa.Enum(
    "open",
    "assigned",
    "picked_up",
    "in_transit",
    "delivered",
    "disputed",
    name="shipmentstatus",
)


def upgrade() -> None:
    role_enum.create(op.get_bind(), checkfirst=True)
    shipment_status_enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("email", sa.String(length=120), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("role", role_enum, nullable=False),
        sa.Column("is_approved", sa.Boolean(), nullable=False, server_default=sa.true()),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "shipments",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("customer_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("title", sa.String(length=120), nullable=False),
        sa.Column("pickup_location", sa.String(length=120), nullable=False),
        sa.Column("drop_location", sa.String(length=120), nullable=False),
        sa.Column("material_type", sa.String(length=80), nullable=False),
        sa.Column("weight_kg", sa.Float(), nullable=False),
        sa.Column("urgency", sa.String(length=40), nullable=False),
        sa.Column("status", shipment_status_enum, nullable=False),
        sa.Column("ai_price_estimate", sa.Float(), nullable=True),
        sa.Column("ai_summary", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )

    op.create_table(
        "bids",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("shipment_id", sa.Integer(), sa.ForeignKey("shipments.id"), nullable=False),
        sa.Column("transporter_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("eta_hours", sa.Integer(), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("is_selected", sa.Boolean(), nullable=False, server_default=sa.false()),
    )

    op.create_table(
        "messages",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("shipment_id", sa.Integer(), sa.ForeignKey("shipments.id"), nullable=False),
        sa.Column("sender_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("sent_at", sa.DateTime(), nullable=False),
    )

    op.create_table(
        "tracking_events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("shipment_id", sa.Integer(), sa.ForeignKey("shipments.id"), nullable=False),
        sa.Column("status", sa.String(length=40), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.Column("note", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("tracking_events")
    op.drop_table("messages")
    op.drop_table("bids")
    op.drop_table("shipments")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
    shipment_status_enum.drop(op.get_bind(), checkfirst=True)
    role_enum.drop(op.get_bind(), checkfirst=True)
