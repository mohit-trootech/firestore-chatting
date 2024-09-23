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
from firechat.utils.constants import (
    FORM_LABELS,
    FORM_CLASS,
    FORM_CLASS_FILE,
)


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            "username": TextInput(
                attrs={"class": FORM_CLASS, "placeholder": "Enter Username"}
            )
        }
        labels = {
            "username": FORM_LABELS.get("username"),
        }


class UserLoginForm(Form):
    username = CharField(
        required=True,
        max_length=30,
        widget=TextInput(
            attrs={
                "class": FORM_CLASS,
                "placeholder": "Enter Login Username",
                "required": True,
            }
        ),
        label=FORM_LABELS.get("username"),
    )
    password = CharField(
        required=True,
        widget=PasswordInput(
            attrs={
                "class": FORM_CLASS,
                "placeholder": "Enter Login Password",
                "required": True,
            }
        ),
        label=FORM_LABELS.get("password"),
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
        labels = {}
        for field in fields:
            if field == "profile":
                input_option = ClearableFileInput
            elif field == "age" or field == "phone":
                input_option = NumberInput
            elif field == "email":
                input_option = EmailInput
            else:
                input_option = TextInput
            widgets[field] = (
                input_option(attrs={"class": FORM_CLASS})
                if field != "profile"
                else input_option(attrs={"class": FORM_CLASS_FILE})
            )
            labels[field] = FORM_LABELS.get(field)
