import { Nav } from "@/components/Nav";
import { ShipmentForm } from "@/components/ShipmentForm";
import { api } from "@/lib/api";

export default async function ShipmentsPage() {
  const shipments = await api<any[]>("/api/v1/shipments/");

  return (
    <main className="shell stack">
      <Nav />
      <div className="grid two">
        <ShipmentForm />
        <section className="card">
          <h2>Shipment Board</h2>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Status</th>
                <th>AI Estimate</th>
              </tr>
            </thead>
            <tbody>
              {shipments.map((shipment) => (
                <tr key={shipment.id}>
                  <td>{shipment.id}</td>
                  <td>{shipment.title}</td>
                  <td>{shipment.status}</td>
                  <td>{shipment.ai_price_estimate ?? "-"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </div>
    </main>
  );
}
