from django.utils.translation import gettext_noop as _
from enum import Enum


# Settings Constants
# =====================================================
class Settings(Enum):
    ROOT_URL = "firechat.urls"
    TEMPLATE = "templates/"
    STATIC_URL = "static/"
    STATICFILES_DIRS = "templates/static/"
    STATIC_ROOT = "assets/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media/"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    DEBUG_TOOLBAR_IP = "127.0.0.1"
    CACHE_TABLE_NAME = "cache_table"


# Status
# =====================================================
class Status(Enum):
    STATUS_INACTIVE = False
    STATUS_ACTIVE = True
    STATUS_200 = 200
    STATUS_202 = 202
    STATUS_400 = 400
    STATUS_404 = 404
    STATUS_500 = 500


# Admin Action Description
# =====================================================
class AdminAction(Enum):
    USER_ADMIN_STATUS_UNACTIVE_DESCRIPTION = _("Mark Selected Items Unactive")
    USER_ADMIN_STATUS_ACTIVE_DESCRIPTION = _("Mark Selected Items Active")
    USER_INACTIVE_SUCCESS_MESSAGE = _("%d users were successfully been inactive.")
    USER_ACTIVE_SUCCESS_MESSAGE = _("%d users were successfully been active.")


# Error Messages
# =====================================================
class Errors(Enum):
    INVALID_JSON = _("Invalid JSON data")
    LOGIN_ERROR = _("Failed to Login Try Again with Correct Credentials")
    PASSWORD_NOT_MATCH = _("Please Check Passwords are Not Matching")
    UNIQUE_USER_ERROR = _("User with Same Username or Password Already Exists")


# Success Messages
# =====================================================
class Success(Enum):
    REGISTERED = _("User Added Successfully")
    USER_404 = _("User Does Not Exists")
    USER_UPDATED = _("User updated successfully")
    LOGGED_IN = _("Logged in Successfully")
    SIGNED_UP = _("User Registered Successfully")
    LOGGED_OUT = _("User Logged Out Successfully")


# Templates Name
# =====================================================
class Templates(Enum):
    LOGIN = "accounts/login.html"
    SIGNUP = "accounts/signup.html"
    PROFILE = "polls/profile.html"
    HOME = "chat/index.html"
    ABOUT = "firechat/about.html"


# Urls Path & Reverse
# =====================================================
class Urls(Enum):
    HOME = "/chat/"
    ABOUT = "/chat/about/"
    LOGIN = "/accounts/login"
    REGISTER = "accounts/signup"
    LOGOUT = "accounts/logout"
    PROFILE = "accounts/profile"
    HOME_REVERSE = "home"
    ABOUT_REVERSE = "about"
    LOGIN_REVERSE = "login"
    REGISTER_REVERSE = "signup"
    LOGOUT_REVERSE = "logout"
    PROFILE_REVERSE = "profile"
    INDEX_REVERSE = "index"
    PROFILE_UPDATE_SUCCESS_URL = "/profile/{pk}"


# Forms Constants Dictionary
# =====================================================
FORM_LABELS = {
    "first_name": "Enter First Name",
    "last_name": "Enter Last Name",
    "username": "Enter Username",
    "email": "Enter Email",
    "password": "Enter Password",
}

FORM_HELP_TEXTS = {
    "first_name": "Please Enter First Name",
    "last_name": "Please Enter Last Name",
    "username": "Please Enter Username",
    "email": "Please Enter Email",
    "password": "Please Choose Password",
}


# Model Media Urls
# =====================================================
class ModelMediaUrl(Enum):
    USER = "profile/{id}"


# Email Configurations
# =====================================================
class EmailConfig(Enum):
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    PORT_465 = 465
    PORT_587 = 587
