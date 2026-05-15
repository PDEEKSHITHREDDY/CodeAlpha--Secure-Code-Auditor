from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio, json
from sniffer import start_sniff, stop_sniff

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = []

async def broadcast(data):
    dead = []
    for c in clients:
        try:
            await c.send_text(json.dumps(data))
        except:
            dead.append(c)
    for d in dead:
        clients.remove(d)

@app.get("/start")
def start():
    start_sniff(lambda d: asyncio.run(broadcast(d)) if d else None)
    return {"status": "started"}

@app.get("/stop")
def stop():
    stop_sniff()
    return {"status": "stopped"}

@app.get("/save")
def save():
    save_pcap()
    return {"status": "pcap saved"}

@app.websocket("/ws")
async def ws(ws: WebSocket):
    await ws.accept()
    clients.append(ws)
    try:
        while True:
            await ws.receive_text()
    except:
        clients.remove(ws)