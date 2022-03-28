from django.contrib.auth.models import User
from django.db import models


class Thread(models.Model):
    sender = models.ForeignKey(User, related_name='thread_sender', on_delete=models.PROTECT)
    receiver = models.ForeignKey(User, related_name='thread_receiver', on_delete=models.PROTECT)
    last_updated = models.DateTimeField()

    class Meta:
        unique_together = ('sender', 'receiver')
        ordering = ('-last_updated',)

    def __str__(self):
        return f"{self.sender.username} : {self.receiver.username}"


class Chat(models.Model):
    sender = models.ForeignKey(User, related_name='chat_sender', on_delete=models.PROTECT)
    receiver = models.ForeignKey(User, related_name='chat_receiver', on_delete=models.PROTECT)
    thread = models.ForeignKey(Thread, related_name='chat_thread', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.message
