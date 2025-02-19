from django.urls import path
from app.consumers import MyAsyncConsumer, MySyncConsumer

websocket_urlpatterns = [
    path('ws/sc/', MySyncConsumer.as_asgi()),
    path('ws/ac/', MyAsyncConsumer.as_asgi())
]