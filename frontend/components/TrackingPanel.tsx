"use client";

import { useState } from "react";

import { API_URL } from "@/lib/api";

export function TrackingPanel() {
  const [status, setStatus] = useState("");

  async function submit(formData: FormData) {
    const payload = Object.fromEntries(formData.entries());
    const res = await fetch(`${API_URL}/api/v1/tracking/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        shipment_id: Number(payload.shipment_id),
        status: payload.status,
        latitude: Number(payload.latitude),
        longitude: Number(payload.longitude),
        note: payload.note,
      }),
    });
    setStatus(res.ok ? "Tracking event added." : "Tracking update failed.");
  }

  return (
    <form action={submit} className="card stack">
      <h3>Mock GPS Tracking</h3>
      <input name="shipment_id" type="number" placeholder="Shipment ID" required />
      <select name="status" defaultValue="in_transit">
        <option value="picked_up">Picked up</option>
        <option value="in_transit">In transit</option>
        <option value="delivered">Delivered</option>
      </select>
      <input name="latitude" type="number" step="0.0001" placeholder="Latitude" required />
      <input name="longitude" type="number" step="0.0001" placeholder="Longitude" required />
      <input name="note" placeholder="Driver note" required />
      <button type="submit">Push Tracking Update</button>
      {status ? <p className="muted">{status}</p> : null}
    </form>
  );
}
