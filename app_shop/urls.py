from django.urls import path
from .views import CategoryAPIView, ProductAPIView
from .views import *
urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('categories/<int:pk>/', CategoryAPIView.as_view()),
    path('products/', ProductAPIView.as_view()),
    path('products/<int:pk>/', ProductAPIView.as_view()),

    path('updateProducts/<int:pk>/', APIProductUpdateView.as_view()),
    path('createProducts/', APIProductCreateAPIView.as_view()),
    path('deleteProducts/<int:pk>', APIProductDeleteAPIView.as_view()),

    path('updateCategory/<int:pk>/', APICategoryUpdateView.as_view()),
    path('createCategory/', APICategoryCreateAPIView.as_view()),
    path('deleteCategory/<int:pk>', APICategoryDeleteAPIView.as_view()),

    path('searchList/<str:txt>/', SearchView.as_view()),
]