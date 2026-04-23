import Link from "next/link";

const links = [
  ["/", "Home"],
  ["/login", "Login"],
  ["/dashboard", "Dashboard"],
  ["/shipments", "Shipments"],
  ["/bids", "Bids"],
  ["/chat", "Chat"],
  ["/tracking", "Tracking"],
  ["/admin", "Admin"],
];

export function Nav() {
  return (
    <nav className="nav">
      {links.map(([href, label]) => (
        <Link key={href} href={href}>
          {label}
        </Link>
      ))}
    </nav>
  );
}
