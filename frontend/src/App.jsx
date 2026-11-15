import React, { useState } from 'react';
import { shortenUrl } from './services/api';
import ShortenerForm from './components/ShortenerForm';
import ResultCard from './components/ResultCard';
import './styles/App.css';

export default function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleShorten = async (longUrl) => {
    setError('');
    setResult(null);

    if (!longUrl) {
      setError('Please enter a valid URL.');
      return;
    }

    try {
      setLoading(true);
      const data = await shortenUrl(longUrl);
      setResult(data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to shorten URL. Is the backend running?');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="app__content">
        {/* Header */}
        <div className="app__header">
          <span className="app__badge">
            FastAPI + React Production Stack
          </span>
          <h1 className="app__title">
            URL Shortener
          </h1>
          <p className="app__description">
            Lightning-fast URL redirection powered by Base62 encoding and MySQL.
          </p>
        </div>

        {/* Form Component */}
        <ShortenerForm onSubmit={handleShorten} loading={loading} error={error} />

        {/* Result Component */}
        {result && <ResultCard result={result} />}
      </div>

      <footer className="app__footer">
        Built with FastAPI, React, MySQL, and Docker.
      </footer>
    </div>
  );
}