# -*- coding: utf-8 -*-
from firechat.accounts.models import User, SocialMediaLink
from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from firechat.utils.constants import Status, AdminAction


class SocialMediaInline(admin.StackedInline):
    model = SocialMediaLink
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "is_active"]
    readonly_fields = [
        "id",
        "last_streak_update",
        "thumbnail_preview",
    ]
    fieldsets = [
        (
            "Customer Details",
            {
                "fields": [
                    "id",
                    "profile",
                    "thumbnail_preview",
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "password",
                    "age",
                    "address",
                    "phone",
                ]
            },
        ),
        (
            "Status Details",
            {
                "classes": ["collapse"],
                "fields": ["status", "is_staff", "is_superuser", "is_active"],
            },
        ),
        (
            "Login Details",
            {"classes": ["collapse"], "fields": ["date_joined", "last_login"]},
        ),
        (
            "Group Details",
            {"classes": ["collapse"], "fields": ["groups", "user_permissions"]},
        ),
        (
            "Following Details",
            {"classes": ["collapse"], "fields": ["following"]},
        ),
        (
            "Streak Details",
            {"classes": ["collapse"], "fields": ["streak", "last_streak_update"]},
        ),
    ]
    search_fields = ["username"]
    list_filter = [
        "is_staff",
        "is_active",
        "is_superuser",
    ]
    ordering = ["id"]
    inlines = [
        SocialMediaInline,
    ]
    filter_horizontal = ["groups", "user_permissions", "following"]
    actions = ["mark_inactive", "mark_active"]

    @admin.action(description=AdminAction.USER_ADMIN_STATUS_UNACTIVE_DESCRIPTION.value)
    def mark_inactive(self, request, queryset):
        updated = queryset.update(is_active=Status.STATUS_INACTIVE.value)
        self.message_user(
            request,
            ngettext(
                AdminAction.USER_INACTIVE_SUCCESS_MESSAGE.value,
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description=AdminAction.USER_ADMIN_STATUS_ACTIVE_DESCRIPTION.value)
    def mark_active(self, request, queryset):
        updated = queryset.update(is_active=Status.STATUS_ACTIVE.value)
        self.message_user(
            request,
            ngettext(
                AdminAction.USER_ACTIVE_SUCCESS_MESSAGE.value,
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
