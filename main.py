from fastapi import FastAPI
from gemini_client import generate_multimodal
from analyze_prompt import ANALYZE_PROMPT
from pydantic_models import AnalyzeRequest

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze")
async def analyze(request: AnalyzeRequest):

    prompt = f"""
            {ANALYZE_PROMPT}

            Instruction:
            {request.instruction}
            """

    result = generate_multimodal(prompt, request.image_base64)

    return {"analysis": result}