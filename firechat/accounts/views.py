from django.views.generic import View, UpdateView, FormView
from firechat.utils.constants import Templates, Urls, Success, Errors
from firechat.accounts.forms import UserLoginForm, UserCreationForm, UserUpdateForm
from django.contrib.auth import login, logout, authenticate, models
from django.contrib.messages import info
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy


class LogoutView(View):

    def get(self, request):
        """
        logout user from request
        """
        logout(request)
        info(request, Success.LOGGED_OUT.value)
        return reverse_lazy(Urls.LOGIN_REVERSE.value)


logout_view = LogoutView.as_view()


class ProfileView(UpdateView):
    form_class = UserUpdateForm
    template_name = Templates.PROFILE.value
    success_url = Urls.PROFILE_UPDATE_SUCCESS_URL.value

    def get_object(self):
        """
        get logged in user object for profile
        """
        return models.User.objects.get(pk=self.request.user.pk)

    def get_success_url(self) -> str:
        """
        get success url based on login user details
        """
        return self.success_url.format(pk=self.request.user.pk)


profile_view = ProfileView.as_view()


class LoginView(FormView):
    template_name = Templates.LOGIN.value
    form_class = UserLoginForm
    success_url = reverse_lazy(Urls.HOME_REVERSE.value)

    def form_valid(self, form):
        """
        login form handle, user will log in if details form is valid else if user not exist return form_invalid

        :param form: _description_
        :return: _description_
        """
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if not user:
            form.add_error(None, Errors.LOGIN_ERROR.value)
            return super().form_invalid(form)
        login(self.request, user)
        info(self.request, Success.LOGGED_IN.value)
        return super().form_valid(form)


login_view = LoginView.as_view()


class RegistrationView(FormView):
    template_name = Templates.SIGNUP.value
    form_class = UserCreationForm
    success_url = reverse_lazy(Urls.LOGIN_REVERSE.value)

    def form_valid(self, form):
        """
        registration form handle, user signed up if form_valid else if password not match user already exist or password valiadtion return form_invalid
        """
        try:
            password1 = self.request.POST.get("password1")
            password2 = self.request.POST.get("password2")
            validate_password(password1)
            if not password1 == password2:
                form.add_error(None, Errors.PASSWORD_NOT_MATCH.value)
                return super().form_invalid(form)
            user = form.save(commit=False)
            user.set_password(password1)
            user.save()
            info(self.request, Success.SIGNED_UP.value)
            return super().form_valid(form)
        except ValidationError as ve:
            form.add_error(None, ve)
            return super().form_invalid(form)


registration_view = RegistrationView.as_view()
