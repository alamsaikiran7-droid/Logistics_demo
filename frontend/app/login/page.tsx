"use client";

import { useState } from "react";

import { Nav } from "@/components/Nav";
import { API_URL } from "@/lib/api";

export default function LoginPage() {
  const [result, setResult] = useState("");

  async function submit(formData: FormData) {
    const payload = Object.fromEntries(formData.entries());
    const res = await fetch(`${API_URL}/api/v1/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    if (res.ok) {
      localStorage.setItem("token", data.access_token);
      localStorage.setItem("role", data.role);
      setResult(`Logged in as ${data.role}. Token stored in localStorage.`);
      return;
    }
    setResult(data.detail || "Login failed");
  }

  return (
    <main className="shell stack">
      <Nav />
      <div className="grid two">
        <form action={submit} className="card stack">
          <h1>Demo Login</h1>
          <input name="email" placeholder="Email" required />
          <input name="password" type="password" placeholder="Password" required />
          <button type="submit">Login</button>
          {result ? <p className="muted">{result}</p> : null}
        </form>
        <section className="card stack">
          <h2>Quick Start</h2>
          <p>Use any seeded account from the home page. The backend returns a JWT and role for demo flows.</p>
        </section>
      </div>
    </main>
  );
}
