# yourappname/routing.py
from django.urls import re_path
from . import consumers  # Import your consumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_slug>[^/]+)/$', consumers.ChatConsumer.as_asgi()),  # URL for chat rooms
]