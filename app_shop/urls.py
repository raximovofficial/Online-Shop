from django.urls import path
from .views import CategoryAPIView, ProductAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('categories/<int:pk>/', CategoryAPIView.as_view()),
    path('products/', ProductAPIView.as_view()),
    path('products/<int:pk>/', ProductAPIView.as_view()),
]