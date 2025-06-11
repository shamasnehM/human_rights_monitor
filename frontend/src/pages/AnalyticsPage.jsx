import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function AnalyticsPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/reports/analytics").then((res) => {
      const formatted = Object.entries(res.data).map(([type, count]) => ({
        type,
        count,
      }));
      setData(formatted);
    });
  }, []);

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-800">Reports Analytics</h1>
      <div className="bg-white p-4 rounded shadow">
        {data.map((entry) => (
          <div key={entry.type} className="flex justify-between py-2 border-b">
            <span>{entry.type}</span>
            <span className="font-semibold">{entry.count}</span>
          </div>
        ))}
        {data.length === 0 && <p className="text-gray-500">No data yet.</p>}
      </div>
    </div>
  );
}