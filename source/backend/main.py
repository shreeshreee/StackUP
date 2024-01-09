from fastapi import FastAPI, status



app = FastAPI()

#run app: uvicorn main:app --reload

@app.get("/", status_code=status.HTTP_200_OK ,tags=["root"])
def root():
    return {"message": "Hello StackUP!"}
