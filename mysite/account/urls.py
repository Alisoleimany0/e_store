from django.urls import path
from account.views import home , login_view , register_view

app_name = 'account'

urlpatterns = [
    path('', home, name='home'),
    path('login/' , login_view , name='login'),
    path('register/', register_view, name = 'register')
]
