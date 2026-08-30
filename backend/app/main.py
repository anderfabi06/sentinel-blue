from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
from agent.graph import sentinel_agent

app = FastAPI(
    title="Sentinel Blue API",
    description="Asistente de IA para NOC/SOC",
    version="0.1.0"
)

class IncidentRequest(BaseModel):
    source: str
    details: Dict[str, Any]

@app.get("/health")
async def health_check():
    return {"status": "ok", "agent": "Sentinel Blue", "engine": "Gemini 3.6 Flash"}

@app.post("/api/v1/analyze")
async def analyze_event(request: IncidentRequest):
    initial_state = {
        "messages": [],
        "incident_data": {
            "source": request.source,
            "details": request.details
        },
        "detected_indicators": [],
        "recommendation": None,
        "requires_approval": False
    }
    
    # Invocación del flujo de agente con Gemini
    result = await sentinel_agent.ainvoke(initial_state)
    
    return {
        "status": "success",
        "analysis": result.get("recommendation"),
        "requires_approval": result.get("requires_approval", False)
    }