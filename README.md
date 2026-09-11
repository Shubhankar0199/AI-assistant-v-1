<<<<<<< HEAD
import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim() || loading) return;

    const userMessage = message;

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: userMessage,
      },
    ]);

    setMessage("");
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: userMessage,
        }),
      });

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.answer,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Something went wrong. Please try again.",
        },
      ]);
    }

    setLoading(false);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="app">

      <header className="header">
        <h2>Shubhankar AI</h2>
        <span>AI Portfolio</span>
      </header>

      <main className="chat-container">

        {messages.length === 0 && (
          <div className="welcome">
            <h1>Hi, I'm Shubhankar's AI</h1>
            <p>Ask me anything about Shubhankar.</p>

            <div className="suggestions">
              <button
                onClick={() => setMessage("Tell me about Shubhankar")}
              >
                Tell me about Shubhankar
              </button>

              <button
                onClick={() => setMessage("What are Shubhankar's skills?")}
              >
                What are his skills?
              </button>

              <button
                onClick={() => setMessage("Tell me about his projects")}
              >
                Tell me about his projects
              </button>
            </div>
          </div>
        )}

        <div className="messages">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message ${
                msg.role === "user" ? "user" : "assistant"
              }`}
            >
              <div className="avatar">
                {msg.role === "user" ? "You" : "AI"}
              </div>

              <div className="message-content">
                {msg.content}
              </div>
            </div>
          ))}

          {loading && (
            <div className="message assistant">
              <div className="avatar">AI</div>

              <div className="message-content loading">
                Thinking...
              </div>
            </div>
          )}
        </div>

      </main>

      <div className="input-area">

        <div className="input-box">

          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask something about Shubhankar..."
            rows="1"
          />

          <button
            onClick={sendMessage}
            disabled={!message.trim() || loading}
          >
            ↑
          </button>

        </div>

        <p>Shubhankar AI can only answer using provided information.</p>

      </div>

    </div>
  );
}

export default App;
=======
# Assistance-v1
Ai that know my professional life 
>>>>>>> c63a1fa175bf47d7aa6f44a9e7a64b5fb0a7fb6d
# AI-assistant-v-1
