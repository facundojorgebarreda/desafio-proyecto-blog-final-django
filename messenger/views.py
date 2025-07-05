from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Message

class InboxView(LoginRequiredMixin, ListView):
    template_name = "messenger/inbox.html"

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user).order_by("-sent_at")

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ["receiver", "body"]
    template_name = "messenger/message_form.html"
    success_url = reverse_lazy("inbox")

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
