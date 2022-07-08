from fastapi import Body, FastAPI
from models import Code, Language
from runners import CppRunner, PythonRunner
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/run/")
def run(code: Code = Body(...)):
    if code.language == Language.cpp:
        return CppRunner(code)
    if code.language == Language.python:
        return PythonRunner(code)
    return {"message": "Unknown language"}