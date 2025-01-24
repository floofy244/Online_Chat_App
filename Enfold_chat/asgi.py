# yourprojectname/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from room import routing  # Replace with your app name

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Enfold_chat.settings')  # Replace with your project name

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns  # Define this in your routing.py
        )
    ),
})