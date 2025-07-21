from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class NameRequest(BaseModel):
    name: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/hello")
def say_hello(data: NameRequest):
    return {"message": f"Hello {data.name}"}

if __name__ == "__main__":
    uvicorn.run("python_example_api.__main__:app", host="0.0.0.0", port=8000, reload=True)
