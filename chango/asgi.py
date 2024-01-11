import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import space.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chango.settings')

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket":AuthMiddlewareStack(
        URLRouter(
            space.routing.websocket_urlpatterns
        )
    )
}
)
