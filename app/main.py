from fastapi import FastAPI, UploadFile
from pathlib import Path
from app.ocr import extract_text
import uuid

app = FastAPI()

@app.get("/health")
def health():
    return {"status":"ok"}

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/screenshots")
async def upload_screenshot(file:UploadFile):
    contents = await file.read()
    new_name = f"{uuid.uuid4()}{Path(file.filename).suffix}"
    saved_path = UPLOAD_DIR/ new_name
    saved_path.write_bytes(contents)
    text = extract_text(saved_path)
    return {"id": new_name, "original_name": file.filename, "ocr_text": text}
    
