from pydantic import BaseModel

class GenerateRequest(BaseModel):
    prompt: str

class AnalyzeRequest(BaseModel):
    image_base64: str
    instruction: str