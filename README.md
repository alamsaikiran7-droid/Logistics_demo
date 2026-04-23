# AI-Powered Logistics Intelligence Platform

Mock-first logistics marketplace with GenAI-inspired workflows. This project includes a Next.js frontend, a FastAPI backend, PostgreSQL-ready SQLAlchemy models, Alembic migration scaffolding, websocket chat, mock GPS tracking, and mock AI/payment flows so it runs without API keys.

## Stack

- Frontend: Next.js 14 App Router
- Backend: FastAPI + SQLAlchemy
- Database: PostgreSQL via Docker Compose, SQLite fallback for quick local runs
- AI Layer: Mock AI service with RAG-style endpoints and structured dispute analysis
- Auth: JWT-ready auth endpoints with role fields for customer, transporter, and admin

## Demo Accounts

- `admin@logistics.local` / `admin123`
- `customer@logistics.local` / `customer123`
- `transporter@logistics.local` / `transporter123`

## Run With Docker

```bash
docker-compose up --build
```

- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`
- Health: `http://localhost:8000/health`

## Run Backend Locally

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The backend uses `backend/.env.example` values by default. For a quick local run without Postgres, set:

```bash
DATABASE_URL=sqlite:///./logistics.db
```

## Run Frontend Locally

```bash
cd frontend
npm install
npm run dev
```

If needed, set:

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Main Features

- Customer shipment creation with AI estimate and auto-summary
- Transporter bid submission and selection
- Mock Razorpay-style payment order creation
- Real-time shipment chat over WebSockets
- Mock GPS tracking updates
- Admin analytics endpoint
- Mock RAG-style logistics assistant
- Structured dispute analysis from shipment messages

## API Overview

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `GET /api/v1/shipments/`
- `POST /api/v1/shipments/`
- `GET /api/v1/bids/`
- `POST /api/v1/bids/`
- `POST /api/v1/bids/{bid_id}/accept`
- `GET /api/v1/chat/{shipment_id}`
- `POST /api/v1/chat/messages`
- `WS /api/v1/chat/ws/{shipment_id}`
- `POST /api/v1/tracking/`
- `POST /api/v1/ai/chatbot`
- `GET /api/v1/ai/shipments/{shipment_id}/summary`
- `GET /api/v1/ai/disputes/{shipment_id}/analyze`
- `GET /api/v1/admin/analytics`

## Notes

- The current version uses mock AI responses and a mock payment provider so the platform runs without external keys.
- The backend includes PostgreSQL-compatible models and Alembic migration scaffolding, while also supporting SQLite for lightweight local startup.
- FAISS is included as a dependency placeholder for local vector search extension, though the current mock assistant uses static retrieval responses.
