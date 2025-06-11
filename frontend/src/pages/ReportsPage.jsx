import React, { useEffect, useState } from 'react';
import axios from 'axios';

const API_BASE = "http://localhost:8000";

export default function ReportsPage() {
  const [reports, setReports] = useState([]);
  const [form, setForm] = useState({ title: "", description: "", type: "" });

  const fetchReports = () => {
    axios.get(`${API_BASE}/reports`).then(res => setReports(res.data));
  };

  useEffect(() => {
    fetchReports();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post(`${API_BASE}/reports`, form);
    setForm({ title: "", description: "", type: "" });
    fetchReports();
  };

  const updateStatus = async (id, status) => {
    await axios.patch(`${API_BASE}/reports/${id}`, { status });
    fetchReports();
  };

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-800">Incident Reports</h1>

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
        <input
          type="text"
          placeholder="Type of Violation"
          className="border w-full p-2"
          value={form.type}
          onChange={(e) => setForm({ ...form, type: e.target.value })}
        />
        <button className="bg-blue-600 text-white px-4 py-2 rounded">Submit</button>
      </form>

      <div className="grid gap-4">
        {reports.map((r) => (
          <div key={r._id} className="bg-white p-4 rounded shadow">
            <h2 className="text-xl font-semibold">{r.title}</h2>
            <p>{r.description}</p>
            <p>Type: {r.type}</p>
            <p>Status: 
              <select
                value={r.status}
                onChange={(e) => updateStatus(r._id, e.target.value)}
                className="ml-2"
              >
                <option>Pending</option>
                <option>Reviewed</option>
                <option>Resolved</option>
              </select>
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}