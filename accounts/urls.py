from django.urls import path
from .views import register_view,logout_view
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('register/',register_view,name='register'),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('refresh/',TokenRefreshView.as_view(),name='login'),
    path('logout/',logout_view,name="logout")
]
