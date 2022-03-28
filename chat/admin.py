from django.contrib import admin

# Register your models here.
from chat.models import Thread, Chat


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    pass


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass
