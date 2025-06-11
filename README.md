
# 🕊️ Human Rights Monitor

A full-stack web application for monitoring and reporting human rights violations, built with **FastAPI**, **MongoDB**, and **React**.

---

## 📁 Project Structure

```
human_rights_monitor/
├── backend/                     # FastAPI backend
│   ├── main.py
│   ├── db.py
│   ├── models/
│   │   ├── case.py
│   │   ├── report.py
│   │   └── victim.py
│   └── routes/
│       ├── case_routes.py
│       ├── report_routes.py
│       ├── victim_routes.py
│       └── analytics_routes.py
├── frontend/                    # React frontend
│   ├── public/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── CasesPage.jsx
│   │   │   ├── ReportsPage.jsx
│   │   │   ├── VictimsPage.jsx
│   │   │   └── AnalyticsPage.jsx
│   │   └── App.jsx
│   └── package.json
└── README.md
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/shamasnehm/human_rights_monitor.git
cd human_rights_monitor
```

---

### 2. Backend (FastAPI)

#### 🔧 Requirements

- Python 3.10+
- MongoDB Atlas or local MongoDB instance


```

#### ▶️ Run the Server

```bash
uvicorn backend.main:app --reload
```

📚 API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 3. Frontend (React)

#### 🔧 Requirements

- Node.js (v18+)

#### 🚀 Run React App

```bash
cd frontend
npm install
npm start
```

🌐 View App: [http://localhost:3000](http://localhost:3000)

---

## 🌐 API Endpoints Summary

| Module              | Endpoint                         | Method      |
|---------------------|----------------------------------|-------------|
| **Cases**           | `/cases/`                        | GET/POST    |
|                     | `/cases/{id}`                    | PATCH       |
| **Reports**         | `/reports/`                      | GET/POST    |
|                     | `/reports/{id}`                  | PATCH       |
|                     | `/reports/analytics`             | GET         |
| **Victims**         | `/victims/`                      | GET/POST    |
|                     | `/victims/{id}`                  | PATCH/GET   |
|                     | `/victims/case/{case_id}`        | GET         |
| **Analytics**       | `/analytics/`                    | GET         |

---

## 🧠 MongoDB Collections

- `cases`
- `incident_reports`
- `victims`
- `report_evidence` 
- `case_status_history` 

---

## 👨‍💻 Project Team

This system was developed by a team of 3 students.  
Each student was responsible for a specific module:

1. **Case Management**
2. **Incident Reporting**
3. **Victim/Witness Database**
4. **Analytics & Visualization**

---

## 📌 Notes

- CORS is configured to allow access from React on `localhost:3000`.
- React communicates with FastAPI through Axios.
- File uploads and geolocation supported in the report module.

---

## 👨‍🏫 Instructor

This project was developed as part of the **Web Services** course – Spring 2025  
**Instructor:** Dr. Ahmad Hamo – Birzeit University

---

## 👥 Group Members

- **Mustafa Shamasneh** – `ID1201600`  
- **Abed Alrahman Thabet** – `ID1220919`  
- **Mohammad Al-Tawil** – `ID1192037`  

