import asyncio
import websockets
from game import *
import json


connected = set()
pgn = []
game = Game()

async def server(websocket, path):
    global pgn
    # Register.
    connected.add(websocket)
    print(websocket)
    try:
        async for move in websocket:
            a = (json.loads(move))
            if a["colour"] == "w":
                t_pgn = [a["move"], "OG"]
                white_move = a["move"]
            else:
                t_pgn = [white_move, a["move"]]
            print(t_pgn)

            # if game.analyse(pgn.append(t_pgn)) == True:
            #     pgn = pgn.append(t_pgn)
            # else:
            #     websocket.send("invalid")
            # pgn.append(t_pgn)
            # print(pgn)
            # for conn in connected:
            #     await conn.send("hi")
    finally:
        # Unregister.
        connected.remove(websocket)
    

start_server = websockets.serve(server, "localhost", 5555)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()