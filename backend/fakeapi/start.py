from fastapi import FastAPI

app = FastAPI()

@app.get("/rooms")
async def get_rooms():
    fake_data = {"message": "Hello World!"}
    return fake_data