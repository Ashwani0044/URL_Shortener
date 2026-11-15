import axios from 'axios'

const API = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {
        'Content-Type': 'application/json',
    },
})

export const shortenUrl = async (longUrl) => {
    const response = await API.post('/api/shorten', { long_url: longUrl });
    return response.data;
};