import { Nav } from "@/components/Nav";
import { AIConsole } from "@/components/AIConsole";
import { api } from "@/lib/api";

export default async function DashboardPage() {
  const shipments = await api<any[]>("/api/v1/shipments/");
  const bids = await api<any[]>("/api/v1/bids/");
  const analytics = await api<Record<string, number>>("/api/v1/admin/analytics");

  return (
    <main className="shell stack">
      <div className="hero">
        <span className="badge">Operations Overview</span>
        <h1>Unified Dashboard</h1>
        <p>One surface for customers, transporters, and admins to understand marketplace activity.</p>
      </div>
      <Nav />
      <div className="grid two">
        <section className="card">
          <h2>Platform Metrics</h2>
          <div className="stack">
            <div className="pill">Users: {analytics.users}</div>
            <div className="pill">Shipments: {analytics.shipments}</div>
            <div className="pill">Bids: {analytics.bids}</div>
            <div className="pill">Messages: {analytics.messages}</div>
          </div>
        </section>
        <section className="card">
          <h2>Marketplace Snapshot</h2>
          <p>{shipments.length} shipments and {bids.length} bids are currently available in the demo environment.</p>
        </section>
      </div>
      <AIConsole />
    </main>
  );
}
