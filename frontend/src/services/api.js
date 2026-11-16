import axios from 'axios';

const API = axios.create({
  // Empty string routes requests relative to the current origin (http://localhost)
  baseURL: import.meta.env.VITE_API_URL || '',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const shortenUrl = async (longUrl) => {
  const response = await API.post('/api/shorten', { long_url: longUrl });
  return response.data;
};