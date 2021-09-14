from django.urls import path
from .api import NewOrderCreateAPIView, OrderViewAPIView, CancelOrderAPIView, UpdateOrderAPIView

urlpatterns = [
    path('new/', NewOrderCreateAPIView.as_view()),
    path('<int:pk>/view/', OrderViewAPIView.as_view()),
    path('<int:pk>/cancel/', CancelOrderAPIView.as_view()),
    path('<int:pk>/update/', UpdateOrderAPIView.as_view()),
]
