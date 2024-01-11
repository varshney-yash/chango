import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.space_name = self.scope['url_route']['kwargs']['room_name']
        self.space_group_name = 'chat_%s' % self.space_name

        await self.channel_layer.group_add(
            self.space_name,
            self.space_group_name
        )

        await self.accept()

    async def disconnect(self): 
        await self.channel_layer.group_discard(
            self.space_group_name,
            self.space_name
        )