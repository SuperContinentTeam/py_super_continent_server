import uvicorn
from fastapi import FastAPI
from fastapi.websockets import WebSocket

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        response_data = {"Message": "Health"}
        await websocket.send_json(response_data)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
