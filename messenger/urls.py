from django.urls import path
from .views import InboxView, MessageCreateView

urlpatterns = [
    path("", InboxView.as_view(), name="inbox"),
    path("new/", MessageCreateView.as_view(), name="message_new"),
]
