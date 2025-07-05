from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page

class PageListView(ListView):
    model = Page            # lista

class PageDetailView(DetailView):
    model = Page            # detalle

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ["title", "subtitle", "body", "image"]

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ["title", "subtitle", "body", "image"]

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy("page_list")
