"use client";

import { useState } from "react";

import { API_URL } from "@/lib/api";

export function BidForm() {
  const [status, setStatus] = useState("");

  async function submit(formData: FormData) {
    const payload = Object.fromEntries(formData.entries());
    const res = await fetch(`${API_URL}/api/v1/bids/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        shipment_id: Number(payload.shipment_id),
        amount: Number(payload.amount),
        eta_hours: Number(payload.eta_hours),
        message: payload.message,
      }),
    });
    setStatus(res.ok ? "Bid submitted." : "Failed to submit bid.");
  }

  return (
    <form action={submit} className="card stack">
      <h3>Place Bid</h3>
      <input name="shipment_id" type="number" placeholder="Shipment ID" required />
      <input name="amount" type="number" step="0.01" placeholder="Bid amount" required />
      <input name="eta_hours" type="number" placeholder="ETA in hours" required />
      <textarea name="message" placeholder="Optional transporter note" required />
      <button type="submit">Submit Bid</button>
      {status ? <p className="muted">{status}</p> : null}
    </form>
  );
}
