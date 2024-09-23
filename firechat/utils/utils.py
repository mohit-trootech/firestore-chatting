from turtle import update
from firechat.chat.models import Message
from firechat.accounts.models import User
from firechat.utils.firestore_config import db, firestore
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from firechat.utils.constants import Templates, TYPE_HTML, SECONDS_IN_ONE_DAY
from django.utils.timezone import now
from django.contrib.sessions.models import Session


def get_online_users():
    """
    get users whose status are online
    """
    return (
        User.objects.prefetch_related("following", "followers")
        .filter(status=True)
        .distinct()
    )


def update_user_streak(user):
    """
    update users streak of login
    """
    if (
        SECONDS_IN_ONE_DAY < (now() - user.last_streak_update).total_seconds()
        and (2 * SECONDS_IN_ONE_DAY) > (now() - user.last_streak_update).total_seconds()
    ):
        user.streak += 1
        user.last_streak_update = now()
        user.streak
        user.save(update_fields=["streak", "last_streak_update"])
        return
    elif (2 * SECONDS_IN_ONE_DAY) < (now() - user.last_streak_update).total_seconds():
        user.streak = 0
        user.last_streak_update = now()
        user.save(update_fields=["streak", "last_streak_update"])


def force_logout(request):
    """
    logout user from request
    """

    sessions = Session.objects.filter(expire_date__gt=now())

    for session in sessions:
        id = session.get_decoded().get("_auth_user_id")
        if id:
            if request.user.pk == int(id):
                session.delete()


def update_friends_list(request, user):
    """
    update friends list

    :param request:
    :param user: str
    """
    user = User.objects.prefetch_related("following").get(username=user)
    if user in request.user.following.all():
        request.user.following.remove(user.id)
        return
    request.user.following.add(user)
    return


def user_status_active(id):
    """
    Make User Online Status True
    """
    user = User.objects.get(id=id)
    user.status = True
    user.save()


def user_status_unactive(id):
    """
    Make User Online Status True
    """
    user = User.objects.get(id=id)
    user.status = False
    user.save()


def toggle_user_online_status(id: int):
    """
    toggle logged in user online address

    :param id: int
    """
    user = User.objects.get(id=id)
    user.status = not user.status
    user.save()


def get_all_messages():
    """
    get Complete Messages List
    """
    messages = Message.objects.select_related("sender").all()
    return messages


def create_new_message(sender, content):
    """
    create new message
    """
    return Message.objects.create(sender=sender, content=content)


def get_users_queryset_based_on_user_search_exclude_request_user(id, user):
    """
    Get Users Queryset Based on User Search for New Chat & Exclude Logged in User Object

    :param id: int
    :param user: str
    """
    return User.objects.exclude(id=id).filter(username__icontains=user).distinct()


def add_message(sender, content):
    """
    # Function to add a message to a chat

    :param chat_id:
    :param sender_id:
    :param content:
    :return:
    """
    db.collection("chats").add(
        {
            "sender": sender.username,
            "content": content,
            "sent_at": firestore.SERVER_TIMESTAMP,
        }
    )
    return


def send_mails(subject, sender, receiver, body, attachment):
    """
    send emails

    :param subject: str
    :param sender: str
    :param receiver: list
    :param body: str
    :param attachment:
    """
    mail = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email=sender,
        to=receiver,
    )
    html_message = render_to_string(Templates.NEWSLETTER.value)
    mail.attach_alternative(html_message, TYPE_HTML)
    if attachment:
        mail.attach("image.jpeg", attachment.read())
    mail.send()
