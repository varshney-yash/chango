import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.space_name = self.scope['url_route']['kwargs']['space_name']
        self.space_group_name = 'chat_%s' % self.space_name
        await self.channel_layer.group_add(
            self.space_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code): 
        await self.channel_layer.group_discard(
            self.space_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.space_group_name,
            {
                'type':'chat_message',
                'message':data.get('message',None),
                'username':data.get('username',None),
                'space':data.get('space',None)
            }
        )

    async def chat_message(self,event):
        await self.send(text_data=json.dumps({
            'message':event.get('message',None),
            'username':event.get('username',None),
            'space':event.get('space',None)
        }))