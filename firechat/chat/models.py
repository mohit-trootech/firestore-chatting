from django.db import models
from firechat.accounts.models import User
from django_extensions.db.models import TimeStampedModel


class Message(TimeStampedModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.content
