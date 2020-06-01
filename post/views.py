from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'post/home.html'

class DetailView(TemplateView):
    template_name = 'post/detail.html'
