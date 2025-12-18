from django.urls import path
from .views import main_page,register_view,login_view,profile_page



urlpatterns = [
    path('', main_page, name="main_page"),
    path('login/', login_view, name="login_view"),
    path('register/', register_view, name="register_view"),
    path('profile/', profile_page, name="profile_view")

]