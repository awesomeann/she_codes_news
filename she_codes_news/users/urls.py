from django.urls import path
from .views import CreateAccountView, ViewAccount

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='create-account'),
    path('<int:pk>/', ViewAccount.as_view(), name='account'),
]