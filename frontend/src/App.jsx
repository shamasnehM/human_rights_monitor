import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import CasesPage from "./pages/CasesPage";
import ReportsPage from "./pages/ReportsPage";
import VictimsPage from "./pages/VictimsPage";
import AnalyticsPage from "./pages/AnalyticsPage";

function App() {
  return (
    <Router>
      <nav className="p-4 bg-blue-700 text-white flex gap-4">
        <Link to="/">Cases</Link>
        <Link to="/reports">Reports</Link>
        <Link to="/victims">Victims</Link>
        <Link to="/analytics">Analytics</Link>
      </nav>
      <div className="p-6">
        <Routes>
          <Route path="/" element={<CasesPage />} />
          <Route path="/reports" element={<ReportsPage />} />
          <Route path="/victims" element={<VictimsPage />} />
          <Route path="/analytics" element={<AnalyticsPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;