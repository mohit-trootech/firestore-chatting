from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.messages import info
from firechat.utils.utils import update_user_streak


class UpdateStreakMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            update_user_streak(user=request.user)
        return response
