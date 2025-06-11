
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Import routers
from backend.routes.case_routes import router as case_router
from backend.routes.report_routes import router as report_router
from backend.routes.victim_routes import router as victim_router
from backend.routes.analytics_routes import router as analytics_router

app = FastAPI(
    title="Human Rights Monitor API",
    description="FastAPI backend for monitoring human rights violations",
    version="1.0.0"
)

# Enable CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register route modules
app.include_router(case_router, tags=["Case Management"])
app.include_router(report_router, tags=["Incident Reporting"])
app.include_router(victim_router, tags=["Victim/Witness Database"])
app.include_router(analytics_router, tags=["Data Analysis"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Human Rights Monitor API"}




app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
