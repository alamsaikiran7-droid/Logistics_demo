"use client";

import { useState } from "react";

import { API_URL } from "@/lib/api";

export function AIConsole() {
  const [question, setQuestion] = useState("What is the best way to ship fragile items?");
  const [answer, setAnswer] = useState("");

  async function ask() {
    const res = await fetch(`${API_URL}/api/v1/ai/chatbot`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });
    const data = await res.json();
    setAnswer(`${data.answer} Sources: ${data.sources.join(", ")}`);
  }

  return (
    <div className="card stack">
      <h3>AI Logistics Assistant</h3>
      <textarea value={question} onChange={(e) => setQuestion(e.target.value)} />
      <button onClick={ask}>Ask Assistant</button>
      {answer ? <p>{answer}</p> : null}
    </div>
  );
}
