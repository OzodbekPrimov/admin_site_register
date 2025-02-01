from django.urls import path
from .views import home_page, login_page, logout_page, SignUpView

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('signup/', SignUpView.as_view(), name='signup'),
]