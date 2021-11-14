from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.get_products, name='products'),
    path('products/<str:pk>/', views.get_product, name='product'),

    path('users/', views.get_users, name='users'),
    path('users/profile/', views.get_user_profile, name='users-profile'),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
