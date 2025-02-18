from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import time, asyncio



class MySyncConsumer(SyncConsumer):
    # called when client initially opens a connection and is about to finish the websocket handshake..
    def websocket_connect(self, event):
        print('sync Websocket Connected...', event)
        self.send({
            'type':'websocket.accept'
        })
    
    # called when data is received from client
    def websocket_receive(self, event):
        print('Msg received...', event)
        for i in range(10):
            self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            sleep(1)
    
    # called when connection is lost
    def websocket_disconnect(self, event):
        print('Websocket disconnected...', event)
        raise StopConsumer()
        
        
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('async Websocket Connected...', event)
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        print('Msg received...', event)
        for i in range(10):
            await self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            await asyncio.sleep(1)
    
    async def websocket_disconnect(self, event):
        print('Websocket disconnected...', event)
        raise StopConsumer()