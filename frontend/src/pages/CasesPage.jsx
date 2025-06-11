import React, { useEffect, useState } from 'react';
import axios from 'axios';

const API_BASE = "http://localhost:8000";

export default function CasesPage() {
  const [cases, setCases] = useState([]);
  const [form, setForm] = useState({ title: "", description: "", priority: "Low" });

  const fetchCases = () => {
    axios.get(`${API_BASE}/cases`).then(res => setCases(res.data));
  };

  useEffect(() => {
    fetchCases();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post(`${API_BASE}/cases`, form);
    setForm({ title: "", description: "", priority: "Low" });
    fetchCases();
  };

  const updateStatus = async (id, newStatus) => {
    await axios.patch(`${API_BASE}/cases/${id}`, { status: newStatus });
    fetchCases();
  };

  const deleteCase = async (id) => {
    await axios.delete(`${API_BASE}/cases/${id}`);
    fetchCases();
  };

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-800">Cases</h1>

      <form onSubmit={handleSubmit} className="bg-white p-4 rounded shadow space-y-4">
        <input
          type="text"
          placeholder="Title"
          className="border w-full p-2"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
          required
        />
        <textarea
          placeholder="Description"
          className="border w-full p-2"
          value={form.description}
          onChange={(e) => setForm({ ...form, description: e.target.value })}
          required
        />
        <select
          className="border p-2"
          value={form.priority}
          onChange={(e) => setForm({ ...form, priority: e.target.value })}
        >
          <option>Low</option>
          <option>Medium</option>
          <option>High</option>
        </select>
        <button className="bg-blue-600 text-white px-4 py-2 rounded">Create</button>
      </form>

      <div className="grid gap-4">
        {cases.map((c) => (
          <div key={c._id} className="bg-white p-4 rounded shadow">
            <h2 className="text-xl font-semibold">{c.title}</h2>
            <p>{c.description}</p>
            <p>Priority: {c.priority}</p>
            <p>Status: 
              <select
                value={c.status}
                onChange={(e) => updateStatus(c._id, e.target.value)}
                className="ml-2"
              >
                <option>Open</option>
                <option>In Progress</option>
                <option>Closed</option>
              </select>
            </p>
            <button
              onClick={() => deleteCase(c._id)}
              className="mt-2 bg-red-600 text-white px-3 py-1 rounded"
            >
              Delete
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}