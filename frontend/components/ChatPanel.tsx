"use client";

import { useEffect, useState } from "react";

import { API_URL } from "@/lib/api";

type ChatMessage = {
  id?: number;
  sender_id: number;
  content: string;
};

export function ChatPanel() {
  const [shipmentId, setShipmentId] = useState(1);
  const [senderId, setSenderId] = useState(2);
  const [content, setContent] = useState("");
  const [messages, setMessages] = useState<ChatMessage[]>([]);

  useEffect(() => {
    const ws = new WebSocket(`${API_URL.replace("http", "ws")}/api/v1/chat/ws/${shipmentId}`);
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data) as ChatMessage;
      setMessages((prev) => [...prev, data]);
    };
    return () => ws.close();
  }, [shipmentId]);

  async function sendMessage() {
    const payload = { shipment_id: shipmentId, sender_id: senderId, content };
    const res = await fetch(`${API_URL}/api/v1/chat/messages`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    if (res.ok) {
      const saved = (await res.json()) as ChatMessage;
      setMessages((prev) => [...prev, saved]);
      setContent("");
    }
  }

  return (
    <div className="card stack">
      <h3>Shipment Chat</h3>
      <div className="row">
        <input value={shipmentId} onChange={(e) => setShipmentId(Number(e.target.value))} type="number" />
        <input value={senderId} onChange={(e) => setSenderId(Number(e.target.value))} type="number" />
      </div>
      <div className="stack">
        {messages.map((message, idx) => (
          <div key={message.id ?? idx} className="pill">
            Sender {message.sender_id}: {message.content}
          </div>
        ))}
      </div>
      <textarea value={content} onChange={(e) => setContent(e.target.value)} placeholder="Type a message" />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}
