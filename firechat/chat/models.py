from django.db import models
from firechat.accounts.models import User
from django_extensions.db.models import TimeStampedModel


class CustomMessageManager(models.Manager):

    def all(self):
        return super().select_related("sender").all()

    def get_queryset(self):
        return super().get_queryset().filter(is_read=False)


class Message(TimeStampedModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    is_read = models.BooleanField(default=False)

    objects = CustomMessageManager()

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.content
