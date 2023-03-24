from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='authz'
urlpatterns = [
    path("login", views.ProtectView.as_view(), name='protect'),
]
