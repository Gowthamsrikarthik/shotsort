from fastapi import FastAPI, UploadFile
from pathlib import Path
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
    (UPLOAD_DIR / new_name).write_bytes(contents)
    return {"id": new_name, "original_name":file.filename}
    
