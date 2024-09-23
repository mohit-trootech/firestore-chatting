# -*- coding: utf-8 -*-
from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField
from firechat.utils.constants import (
    ModelMediaUrl,
    EMPTY_STR,
    INACTIVE_STATUS,
    STATUS_CHOICES,
)


def _upload_to(self, file):
    return ModelMediaUrl.USER.value.format(id=self.id, name=file)


class CustomUserManager(UserManager):
    def get(self, *args, **kwargs):
        return super().prefetch_related("following", "followers").get(*args, **kwargs)


class User(AbstractUser):
    profile = models.ImageField(upload_to=_upload_to, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    phone = PhoneNumberField(region="IN", blank=True, null=True)
    streak = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=INACTIVE_STATUS)
    last_streak_update = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )
    objects = CustomUserManager()

    def get_mutual_friends(self, other_user):
        self_following = set(self.following.all())
        other_following = set(other_user.following.all())
        mutual_friends = self_following.intersection(other_following)
        return len(mutual_friends)

    def is_following(self, user):

        if user in self.following.all():
            return "following"
        return "follow"

    # @property
    # def thumbnail_preview(self):
    #     if self.profile:
    #         return format_html(THUMBNAIL_PREVIEW_TAG.format(img=self.profile.url))
    #     return format_html(THUMBNAIL_PREVIEW_HTML)

    def __str__(self):
        return self.username

    def __str__(self):
        return self.username


class SocialMediaLink(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="social_links"
    )
    facebook = models.URLField(null=True, blank=True, default=EMPTY_STR)
    github = models.URLField(null=True, blank=True, default=EMPTY_STR)
    instagram = models.URLField(null=True, blank=True, default=EMPTY_STR)
    youtube = models.URLField(null=True, blank=True, default=EMPTY_STR)

    def __str__(self):
        return "{user} Social Media Links".format(user=self.user.username)
