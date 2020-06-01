from django.contrib.auth.views import login, logout
from django.urls import path
from account.views import signup

app_name = 'account'

urlpatterns = [
    path("login/", login, {'template_name' : 'account/login.html'}, name ="login"),
    path("logout/", logout, {'next_page' : '/'}, name ="logout"),
    path("signup/", signup, name ="signup")
]
