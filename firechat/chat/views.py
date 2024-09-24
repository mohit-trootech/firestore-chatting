from typing import Any
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView, View
from firechat.utils.constants import (
    Templates,
    RequestKey,
    Status,
    UTF_8,
    EmailConstants,
    Success,
    ContextNames,
)
from django.http import JsonResponse
from django.shortcuts import render
from firechat.utils.utils import (
    add_message,
    get_all_messages,
    create_new_message,
    toggle_user_online_status,
    send_mails,
    update_friends_list,
    get_online_users,
)
from django.core.paginator import Paginator


class HomeView(TemplateView):
    template_name = Templates.HOME.value

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        paginator = Paginator(get_all_messages(), 10)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        page_obj.object_list.reverse()
        context[ContextNames.MESSAGES.value] = page_obj
        return context

    def get_template_names(self):
        """
        get template update using htmx

        :return:
        """
        if (
            self.request.GET.get(RequestKey.REQUEST_TYPE.value)
            == RequestKey.LOAD_CHATS.value
        ):
            return Templates.CHAT_LIST.value
        return self.template_name


home_view = HomeView.as_view()


class AboutView(TemplateView):
    template_name = Templates.ABOUT.value


about_view = AboutView.as_view()


class ChatDataView(View):

    def get(self, request):
        request_type = request.GET.get(RequestKey.REQUEST_TYPE.value)
        if request_type == RequestKey.UPDATE_STATUS.value:
            toggle_user_online_status(id=request.user.id)
            return HttpResponse(status=Status.STATUS_204.value)
        elif request_type == RequestKey.UPDATE_FRIENDS_LIST.value:
            user = request.GET.get(RequestKey.USER.value)
            update_friends_list(request=request, user=user)
            return HttpResponse(status=Status.STATUS_204.value)
        elif request_type == RequestKey.ONLINE_USERS.value:
            online = get_online_users()
            page = render(
                self.request, Templates.ONLINE_USERS_LIST.value, {"online": online}
            )
            return JsonResponse(
                {
                    "page": page.content.decode(UTF_8),
                },
                status=Status.STATUS_200.value,
            )

    def post(self, request):
        user_text = request.POST.get(RequestKey.USER_TEXT.value)
        message = create_new_message(sender=request.user, content=user_text)
        add_message(sender=message.sender, content=message.content)
        return HttpResponse(status=Status.STATUS_204.value)

    def put(self, request):
        pass


chat_data_view = ChatDataView.as_view()


class NewsletterView(View):

    def post(self, request):
        email = request.POST.get("email")
        send_mails(
            subject=EmailConstants.NEWSLETTER.value,
            sender=EmailConstants.HOST.value,
            receiver=[email],
            body="",
            attachment=None,
        )
        return JsonResponse({"message": Success.NEWSLETTER_SUCCESS.value})


newsletter = NewsletterView.as_view()
