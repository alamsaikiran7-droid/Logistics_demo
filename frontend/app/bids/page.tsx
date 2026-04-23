import { BidForm } from "@/components/BidForm";
import { Nav } from "@/components/Nav";
import { api } from "@/lib/api";

export default async function BidsPage() {
  const bids = await api<any[]>("/api/v1/bids/");

  return (
    <main className="shell stack">
      <Nav />
      <div className="grid two">
        <BidForm />
        <section className="card">
          <h2>Bid Stream</h2>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Shipment</th>
                <th>Amount</th>
                <th>ETA</th>
                <th>Selected</th>
              </tr>
            </thead>
            <tbody>
              {bids.map((bid) => (
                <tr key={bid.id}>
                  <td>{bid.id}</td>
                  <td>{bid.shipment_id}</td>
                  <td>{bid.amount}</td>
                  <td>{bid.eta_hours}h</td>
                  <td>{bid.is_selected ? "Yes" : "No"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </div>
    </main>
  );
}
