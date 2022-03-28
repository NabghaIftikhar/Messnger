from django.urls import path
from chat.views import index, chat_thread
app_name = "chats"
urlpatterns = [
    path('chat/', index, name="chat"),
    path('chat/<int:pk>/', chat_thread, name="messages"),
]
