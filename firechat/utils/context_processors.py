from django import conf
from firechat.forms import Themes, NewsLetter
from firechat.accounts.models import User
from dotenv import dotenv_values

from firechat.utils import firestore_config

config = dotenv_values(".env")


def theme_form(request):
    theme_form = Themes()
    return {"theme_form": theme_form}


def newsletter_form(request):
    newsletter_form = NewsLetter()
    return {"newsletter_form": newsletter_form}


def get_all_online_users(request):
    return {"online": User.objects.filter(status=True)}


def get_firestore_configuration(request):
    firestore_config = {
        "API_KEY": config.get("API_KEY"),
        "AUTH_DOMAIN": config.get("AUTH_DOMAIN"),
        "DATABASE_URL": config.get("DATABASE_URL"),
        "PROJECT_ID": config.get("PROJECT_ID"),
        "STORAGE_BUCKET": config.get("STORAGE_BUCKET"),
        "MESSAGING_SENDER_ID": config.get("MESSAGING_SENDER_ID"),
        "APP_ID": config.get("APP_ID"),
        "measurementId": config.get("measurementId"),
    }
    return firestore_config
