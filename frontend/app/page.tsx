import Link from "next/link";

import { Nav } from "@/components/Nav";

export default function HomePage() {
  return (
    <main className="shell stack">
      <div className="hero stack">
        <span className="badge">GenAI Logistics Demo</span>
        <h1>AI-Powered Logistics Intelligence Platform</h1>
        <p>
          A mock-first marketplace where customers create shipments, transporters bid, admins monitor
          operations, and AI assists with support, pricing, summaries, and dispute intelligence.
        </p>
        <div className="row">
          <Link href="/dashboard" className="button">
            Open Dashboard
          </Link>
          <Link href="/login" className="button secondary">
            Demo Login
          </Link>
        </div>
      </div>
      <Nav />
      <div className="grid two">
        <section className="card">
          <h2>Seeded Demo Accounts</h2>
          <div className="stack">
            <div className="pill">Admin: admin@logistics.local / admin123</div>
            <div className="pill">Customer: customer@logistics.local / customer123</div>
            <div className="pill">Transporter: transporter@logistics.local / transporter123</div>
          </div>
        </section>
        <section className="card">
          <h2>Included Features</h2>
          <div className="stack">
            <div className="pill">JWT + RBAC backend</div>
            <div className="pill">Shipment and bidding workflows</div>
            <div className="pill">Real-time websocket chat</div>
            <div className="pill">Mock AI assistant and dispute analysis</div>
            <div className="pill">Mock Razorpay-style order creation</div>
          </div>
        </section>
      </div>
    </main>
  );
}
