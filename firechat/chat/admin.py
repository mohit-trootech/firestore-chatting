from django.contrib import admin
from firechat.chat.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "content", "created", "is_read")
    list_filter = ("is_read", "sender")
    search_fields = ("content",)
    ordering = ("created",)
