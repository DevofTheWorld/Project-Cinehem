from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.llm_agent import LLM_AGENT

router = APIRouter()
agent = LLM_AGENT()

@router.post("/roast")
async def roast_films(file: UploadFile = File(...)):
    if not file.filename.endswith((".csv")):
        raise HTTPException(status_code=400, detail="Please upload a valid .csv file")

    try:
        roast_result = agent.roaster()
        return {"status": "success", "roast": roast_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))