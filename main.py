from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class Input(BaseModel):
    value: str


stack = []


@app.post("/push")
async def push(inputValue: Input):
    stack.append(inputValue.value)


@app.get("/pop")
async def pop():
    return {"value": stack.pop()}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
