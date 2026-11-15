import React, { useState } from 'react';
import '../styles/ShortenerForm.css';

export default function ShortenerForm({ onSubmit, loading, error }) {
  const [longUrl, setLongUrl] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(longUrl);
  };

  return (
    <div className="shortener-form">
      <form onSubmit={handleSubmit} className="shortener-form__form">
        <div>
          <label className="shortener-form__label">
            Destination URL
          </label>
          <div className="shortener-form__controls">
            <input
              type="url"
              placeholder="https://example.com/very-long-url-path"
              value={longUrl}
              onChange={(e) => setLongUrl(e.target.value)}
              className="shortener-form__input"
              required
            />
            <button
              type="submit"
              disabled={loading}
              className="shortener-form__submit"
            >
              {loading ? 'Shortening...' : 'Shorten'}
            </button>
          </div>
        </div>
      </form>

      {error && (
        <div className="shortener-form__error">
          {error}
        </div>
      )}
    </div>
  );
}