from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserLoginForm, UserRegisterForm, ProfileForm
from products_app.models import Basket
from .models import Users


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm


class UserRegisterView(SuccessMessageMixin ,CreateView):
    model = Users
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")
    success_message = "Siz ro'yxatdan o'tdingiz"

class UserProfileView(SuccessMessageMixin, UpdateView):
    model = Users
    template_name = "users/profile.html"
    form_class = ProfileForm
    success_message = "Ma'lumotlar yangilandi"
    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id, ))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context["baskets"] = Basket.objects.filter(user=self.object)
        return context
