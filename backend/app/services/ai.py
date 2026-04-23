from __future__ import annotations

import math


def estimate_price(weight_kg: float, urgency: str) -> float:
    base = 750 + (weight_kg * 12)
    urgency_factor = {"low": 1.0, "medium": 1.15, "high": 1.35}.get(urgency.lower(), 1.1)
    return round(base * urgency_factor, 2)


def generate_shipment_summary(title: str, pickup: str, drop: str, material: str) -> str:
    return (
        f"{title} is scheduled from {pickup} to {drop}. "
        f"The load contains {material} and has been prepared for marketplace bidding."
    )


def answer_logistics_question(question: str) -> dict[str, object]:
    answer = (
        "Mock RAG response: use shock-absorbing packaging, label the cargo clearly, "
        "and prefer vetted transporters with fragile-goods experience."
    )
    sources = [
        "Fragile Goods Handling SOP",
        "Insurance and Packaging FAQ",
    ]
    return {"question": question, "answer": answer, "sources": sources}


def summarize_dispute(messages: list[str]) -> dict[str, object]:
    joined = " ".join(messages).lower()
    issue_type = "delay" if "delay" in joined else "communication"
    severity = "medium" if len(messages) > 1 else "low"
    return {
        "issue_type": issue_type,
        "severity": severity,
        "recommendation": "Ask both parties for timestamped proof and issue a conditional refund if SLA was missed.",
    }


def rank_bid(amount: float, eta_hours: int, rating: float = 4.4) -> dict[str, object]:
    score = max(0.0, 100 - (amount / 100) - (eta_hours * 1.5) + (rating * 5))
    return {
        "score": round(score, 2),
        "explanation": f"Balanced price, ETA, and transporter quality into a score of {math.floor(score)}.",
    }
