# -*- coding: utf-8 -*-
from django.forms import (
    Form,
    ModelForm,
    TextInput,
    CharField,
    PasswordInput,
    NumberInput,
    EmailInput,
    ClearableFileInput,
)
from firechat.accounts.models import User
from firechat.utils.constants import FORM_LABELS, FORM_HELP_TEXTS


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
        widgets = {}
        labels = {}
        help_texts = {}
        for field in fields:
            if field == "email":
                input_option = EmailInput
            elif field == "password":
                input_option = PasswordInput
            else:
                input_option = TextInput
            widgets[field] = input_option(
                attrs={
                    "class": "form-control",
                    "required": False if field != "username" else True,
                    "placeholder": field,
                }
            )
            labels[field] = FORM_LABELS[field]
            help_texts[field] = FORM_HELP_TEXTS[field]


class UserLoginForm(Form):
    username = CharField(
        required=True,
        max_length=30,
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Login Username",
                "required": True,
            }
        ),
        label=FORM_LABELS.get("username"),
        help_text=FORM_HELP_TEXTS.get("username"),
    )
    password = CharField(
        required=True,
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Login Password",
                "required": True,
            }
        ),
        label=FORM_LABELS.get("password"),
        help_text=FORM_HELP_TEXTS.get("password"),
    )


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "profile",
            "first_name",
            "last_name",
            "email",
            "age",
            "phone",
            "address",
        ]
        widgets = {}
        for field in fields:
            if field == "profile":
                input_option = ClearableFileInput
            elif field == "age" or field == "phone":
                input_option = NumberInput
            elif field == "email":
                input_option = EmailInput
            else:
                input_option = TextInput
            widgets[field] = input_option(attrs={"class": "form-control"})
