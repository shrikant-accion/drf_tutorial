from django.urls import path, include
from .views import LoginView, ListSongsView, RegisterUsers


urlpatterns = [
	path('auth/register/', RegisterUsers.as_view(), name="auth-register"),
	path('auth/login/', LoginView.as_view(), name="auth-login"),

	path('songs/', ListSongsView.as_view(), name="songs-all"),
]