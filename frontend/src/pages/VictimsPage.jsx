import React, { useEffect, useState } from 'react';
import axios from 'axios';

const API_BASE = "http://localhost:8000";

export default function VictimsPage() {
  const [victims, setVictims] = useState([]);
  const [form, setForm] = useState({ name: "", statement: "", severity: "Low" });

  const fetchVictims = () => {
    axios.get(`${API_BASE}/victims`).then(res => setVictims(res.data));
  };

  useEffect(() => {
    fetchVictims();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post(`${API_BASE}/victims`, form);
    setForm({ name: "", statement: "", severity: "Low" });
    fetchVictims();
  };

  const updateSeverity = async (id, severity) => {
    await axios.patch(`${API_BASE}/victims/${id}`, { severity });
    fetchVictims();
  };

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-800">Victims / Witnesses</h1>

      <form onSubmit={handleSubmit} className="bg-white p-4 rounded shadow space-y-4">
        <input
          type="text"
          placeholder="Name"
          className="border w-full p-2"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
          required
        />
        <textarea
          placeholder="Statement"
          className="border w-full p-2"
          value={form.statement}
          onChange={(e) => setForm({ ...form, statement: e.target.value })}
          required
        />
        <select
          className="border p-2"
          value={form.severity}
          onChange={(e) => setForm({ ...form, severity: e.target.value })}
        >
          <option>Low</option>
          <option>Medium</option>
          <option>High</option>
        </select>
        <button className="bg-blue-600 text-white px-4 py-2 rounded">Add</button>
      </form>

      <div className="grid gap-4">
        {victims.map((v) => (
          <div key={v._id} className="bg-white p-4 rounded shadow">
            <h2 className="text-xl font-semibold">{v.name}</h2>
            <p>{v.statement}</p>
            <p>Severity:
              <select
                value={v.severity}
                onChange={(e) => updateSeverity(v._id, e.target.value)}
                className="ml-2"
              >
                <option>Low</option>
                <option>Medium</option>
                <option>High</option>
              </select>
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}