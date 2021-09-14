from django.urls import path
from .api import MenuListAPIView

urlpatterns = [
    path('', MenuListAPIView.as_view()),
]
