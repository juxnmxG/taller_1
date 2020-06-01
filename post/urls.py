from django.urls import path
from post.views import HomeView
from account.views import signup
from post.views import DetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("detail/", DetailView.as_view(), name = "detail"),
]
