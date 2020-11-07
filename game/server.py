import asyncio
import websockets
from game import *
import json
import random


connected = set()
pgn = []
games ={"w": [], "b" : []}
pool = ["w", "b"]
game = Game()

async def server(websocket, path):
    global games, pool
    connected.add(websocket)
    pool = pool[::-1]
    games[pool[-1]].append(websocket)

    print(games)

    await websocket.send(pool[-1])

    try:
        async for data in websocket:
            print(data)
    finally:
        connected.remove(websocket)
    

start_server = websockets.serve(server, "192.168.0.5", 5555)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()