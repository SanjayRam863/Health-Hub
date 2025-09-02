from fastapi import FastAPI
from app.routers import risk, bmi, symptoms, diet

app = FastAPI(
    title="Health Monitoring API",
    description="APIs for patient health monitoring, risk prediction, BMI, symptoms analysis, and diet planning.",
    version="1.0.0"
)

# Routers
app.include_router(risk.router)
app.include_router(bmi.router)
app.include_router(symptoms.router)
app.include_router(diet.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Health Monitoring API!"}