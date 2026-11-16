import React, { useState } from 'react';
import '../styles/ResultCard.css';

export default function ResultCard({ result }) {
  const [copied, setCopied] = useState(false);
  const shortUrl = `${window.location.origin}/${result.short_code}`;

  const handleCopy = () => {
    navigator.clipboard.writeText(shortUrl);
    setCopied(true);
    setTimeout(() => setCopied(false), 3000);
  };

  return (
    <div className="result-card">
      <div className="result-card__header">
        <span className="result-card__label">Your Short Link</span>
        <span className="result-card__clicks">
          Clicks: {result.clicks}
        </span>
      </div>
      <div className="result-card__link-row">
        <a
          href={shortUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="result-card__link"
        >
          {shortUrl}
        </a>
        <button
          onClick={handleCopy}
          className="result-card__copy"
        >
          {copied ? 'Copied!' : 'Copy Link'}
        </button>
      </div>
      <div className="result-card__original">
        <span className="result-card__original-label">Original:</span> {result.long_url}
      </div>
    </div>
  );
}