import asyncio
import websockets
from game import *
import demjson
import random
import json
from client import Player, CurrentGame
import uuid

# connected = set()
# game = Game()
# pgn = []
# test_pgn = []
# games = {"1": [], "0": []}
# pool = [1, 0]
# player = {}

# async def server(websocket, path):
#     global games, pool, pgn, player, test_pgn
#     connected.add(websocket)
#     pool = pool[::-1]
#     games[str(pool[-1])].append(websocket)
#     player[websocket] = str(pool[-1])
#     print(games)

#     await websocket.send(str(pool[-1]))

#     try:
#         async for data in websocket:
#             colour = player[websocket]
#             move = demjson.decode(data)["move"]
#             test_pgn.append(move)
#             print(test_pgn)
#             t = game.analyse(test_pgn)
#             game.reset()
#             if t[0] == 1:
#                 move = t[-1][-1]
#                 if move[0] in ["O-O", "O-O-O"]:
#                     pass
#                 else:
#                     move[0] = move[0][-2:]
#                 pgn.append(move)
#                 await games[str(int(not int(colour)))][-1].send(json.dumps({"move" : move}))
#             elif t[0]== 2:
#                 print("checkmate")
#                 move = t[-1][-1]
#                 if move[0] in ["O-O", "O-O-O"]:
#                     pass
#                 else:
#                     move[0] = move[0][-2:]
#                 pgn.append(move)
#                 await games[str(int(not int(colour)))][-1].send(json.dumps({"checkmate" : move}))
#             elif t[0] == 0:
#                 test_pgn.pop(-1)
#                 await games[str(int(colour))][-1].send(json.dumps({"invalid" : pgn}))
#                 print("invalid")
#             game.reset()
#     finally:
#         connected.remove(websocket)



player_pool = set()
connected = set()
game = Game()
pgn = []
test_pgn = []
players = []
games = []
colour_pool = [1,0]

async def player_pool_server(websocket, path):
    global player_pool, players, colour_pool, games, connected
    colour_pool = colour_pool[::-1]
    player_pool.add(websocket)

    try:
        async for name in websocket:
            if any(x.websocket == websocket for x in players):
                print("arlready exists")
                if len([str(e.type) == str(name) for e in games]) >0:
                    if len([e for e in games if e.pool<2]) > 0:
                        g = [e for e in games if e.pool<2][-1]
                else:
                    game_id = uuid.uuid4()
                    g = CurrentGame(name, game_id)
                    games.append(g)
                print("g", g)
                player =[e for e in players if e.websocket == websocket][-1]
                g.add_player(player)
                [e for e in players if e.websocket == websocket][-1].add_game(g.game_id)
                s = [str(player.player_id), str(g.game_id)]
                await websocket.send(json.dumps({"id" : s}))
            
            else:
                print(name)
                i = uuid.uuid4()
                p = Player(name,i, websocket, colour_pool[-1])
                players.append(p)

    finally:
        # print("Games" , games)
        # print("Players" , players)
        player_pool.remove(websocket)


async def server(websocket, path):
    global games, players
    # await websocket.send([e for e in players if e.websocket == websocket][-1].colour)
    try:
        async for data in websocket:
            if "init" in data:
                player_id = demjson.decode(data)["init"][0]
                game_id = demjson.decode(data)["init"][1]
                await websocket.send(str([e.colour for e in players if str(e.player_id) == str(player_id)][-1]))
                [e for e in players if str(e.player_id) == str(player_id)][-1].websocket = websocket
                connected.add(websocket)
            else:
                game_ob = [e for e in games if str(game_id) == str(e.game_id)][-1]
                player = [e for e in players if str(e.player_id) == str(player_id)][-1]
                colour = player.colour
                op_colour = int(not colour)
                move = demjson.decode(data)["move"]
                game_ob.test_pgn.append(move)
                print(game_ob.test_pgn)
                t = game.analyse(game_ob.test_pgn)
                print(game_ob.test_pgn)

                game.reset()
                if t[0] == 1:
                    move = t[-1][-1]
                    if move[0] in ["O-O", "O-O-O"]:
                        pass
                    else:
                        move[0] = move[0][-2:]
                    game_ob.pgn.append(move)
                    # print("valid")
                    await game_ob.get_opponent(colour).send(json.dumps({"move" : move}))
                elif t[0]== 2:
                    # print("checkmate")
                    move = t[-1][-1]
                    if move[0] in ["O-O", "O-O-O"]:
                        pass
                    else:
                        move[0] = move[0][-2:]
                    game_ob.pgn.append(move)
                    await game_ob.get_opponent(colour).send(json.dumps({"checkmate" : move}))
                    games.remove(game_ob)
                    for e in game_ob.players:
                        e.leave_game()
                elif t[0] == 0:
                    game_ob.test_pgn.pop(-1)
                    await game_ob.get_opponent(op_colour).send(json.dumps({"invalid" : game_ob.pgn}))
                    # print("invalid")
                game.reset()
    finally:
        connected.remove(websocket)

start_player_pool = websockets.serve(player_pool_server, "localhost", 4000)
start_server = websockets.serve(server, "localhost", 5555)
asyncio.get_event_loop().run_until_complete(start_player_pool)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
