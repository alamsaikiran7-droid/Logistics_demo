import { ChatPanel } from "@/components/ChatPanel";
import { Nav } from "@/components/Nav";

export default function ChatPage() {
  return (
    <main className="shell stack">
      <Nav />
      <ChatPanel />
    </main>
  );
}
