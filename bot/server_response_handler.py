from aiohttp.client_ws import ClientWebSocketResponse

class ServerResponseHandler:
    @classmethod
    async def handle_message(cls, server_message: str, socket: ClientWebSocketResponse):
        if await cls.is_ping(server_message): await cls.then_pong(socket)
        else:
            print(server_message)
    
    @staticmethod
    async def is_ping(message: str):
        return message.startswith('PING')

    @staticmethod
    async def then_pong(socket: ClientWebSocketResponse):
        await socket.send_str("PONG :tmi.twitch.tv")