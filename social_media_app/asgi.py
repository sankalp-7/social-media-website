import os



from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import Chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_app.settings')
from django.core.asgi import get_asgi_application
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Chat.routing.websocket_urlpatterns
        )
    )
})