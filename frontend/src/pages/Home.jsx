import { useState } from "react";
import ReactMarkdown from "react-markdown";
import { fetchResearch } from "../services/api";
import "../App.css";

function Home() {

  // Topic input
  const [topic, setTopic] = useState("");

  // Research result
  const [data, setData] = useState(null);

  // Search history
  const [history, setHistory] = useState([]);

  // Loading
  const [loading, setLoading] = useState(false);

  // Chat states
  const [question, setQuestion] = useState("");
  const [chatAnswer, setChatAnswer] = useState("");

  // Search function
  const handleSearch = async () => {

    if (!topic) return;

    setLoading(true);

    try {

      const result = await fetchResearch(topic);

      setData(result);

      // Add to history
      setHistory((prev) => [topic, ...prev]);

    } catch (error) {

      console.log(error);

    }

    setLoading(false);
  };

  // Chat with research
  const askQuestion = async () => {

    if (!question) return;

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            report: data.report,
            question: question,
          }),
        }
      );

      const result = await response.json();

      setChatAnswer(result.answer);

    } catch (error) {

      console.log(error);

    }
  };

  return (

    <div className="layout">

      {/* Sidebar */}
      <div className="sidebar">

        <h2>Research History</h2>

        {history.length === 0 && (
          <p className="empty-history">
            No research history
          </p>
        )}

        <ul>

          {history.map((item, index) => (

            <li
              key={index}
              className="history-item"
              onClick={() => setTopic(item)}
            >

              {item}

            </li>

          ))}

        </ul>

      </div>

      {/* Main Content */}
      <div className="main">

        <div className="center-box">

          <h1 className="title">
            Autonomous Research Assistant
          </h1>

          {/* Search Box */}
          <div className="search-box">

            <input
              type="text"
              placeholder="Enter topic or compare: AI vs Blockchain"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
            />

            <button onClick={handleSearch}>
              Search
            </button>

          </div>

          {/* Loading */}
          {loading && (

            <p className="loading">
              Generating research...
            </p>

          )}

        </div>

        {/* Research Report */}
        {data && (

          <div className="report-container">

            <h2>Research Report</h2>

            {/* Report */}
            <div className="report-text">

              <ReactMarkdown>
                {data.report}
              </ReactMarkdown>

            </div>

            {/* Sources */}
            <h3>Sources</h3>

            <ul>

              {data.sources.map((s, i) => (

                <li key={i}>

                  <a
                    href={s.url}
                    target="_blank"
                    rel="noreferrer"
                  >

                    {s.title}

                  </a>

                </li>

              ))}

            </ul>

            {/* PDF Download */}
            <a
              className="download-btn"
              href={data.pdf}
              download
            >

              Download PDF

            </a>

            {/* Chat Section */}
            <div className="chat-section">

              <h3>Ask About This Research</h3>

              <div className="chat-box">

                <input
                  type="text"
                  placeholder="Ask follow-up question..."
                  value={question}
                  onChange={(e) =>
                    setQuestion(e.target.value)
                  }
                />

                <button onClick={askQuestion}>
                  Ask AI
                </button>

              </div>

              {/* Chat Response */}
              {chatAnswer && (

                <div className="chat-answer">

                  <ReactMarkdown>
                    {chatAnswer}
                  </ReactMarkdown>

                </div>

              )}

            </div>

          </div>

        )}

      </div>

    </div>
  );
}

export default Home;