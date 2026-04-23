import { Nav } from "@/components/Nav";
import { api } from "@/lib/api";

export default async function AdminPage() {
  const analytics = await api<Record<string, number>>("/api/v1/admin/analytics");
  const dispute = await api<Record<string, string>>("/api/v1/ai/disputes/1/analyze").catch(() => ({
    issue_type: "none",
    severity: "low",
    recommendation: "Create a shipment and chat messages to generate a dispute analysis.",
  }));

  return (
    <main className="shell stack">
      <Nav />
      <div className="grid two">
        <section className="card">
          <h1>Admin Command Center</h1>
          <div className="stack">
            <div className="pill">Users: {analytics.users}</div>
            <div className="pill">Shipments: {analytics.shipments}</div>
            <div className="pill">Bids: {analytics.bids}</div>
            <div className="pill">Messages: {analytics.messages}</div>
          </div>
        </section>
        <section className="card">
          <h2>AI Dispute Recommendation</h2>
          <p>Issue: {dispute.issue_type}</p>
          <p>Severity: {dispute.severity}</p>
          <p>{dispute.recommendation}</p>
        </section>
      </div>
    </main>
  );
}
