"use client";

import { useState } from "react";

import { API_URL } from "@/lib/api";

export function ShipmentForm() {
  const [status, setStatus] = useState("");

  async function submit(formData: FormData) {
    const payload = Object.fromEntries(formData.entries());
    const res = await fetch(`${API_URL}/api/v1/shipments/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ...payload,
        weight_kg: Number(payload.weight_kg),
      }),
    });
    setStatus(res.ok ? "Shipment created successfully." : "Failed to create shipment.");
  }

  return (
    <form
      action={submit}
      className="card stack"
    >
      <h3>Create Shipment</h3>
      <input name="title" placeholder="Shipment title" required />
      <input name="pickup_location" placeholder="Pickup location" required />
      <input name="drop_location" placeholder="Drop location" required />
      <input name="material_type" placeholder="Material type" required />
      <input name="weight_kg" type="number" step="0.1" placeholder="Weight (kg)" required />
      <select name="urgency" defaultValue="medium">
        <option value="low">Low urgency</option>
        <option value="medium">Medium urgency</option>
        <option value="high">High urgency</option>
      </select>
      <button type="submit">Create</button>
      {status ? <p className="muted">{status}</p> : null}
    </form>
  );
}
