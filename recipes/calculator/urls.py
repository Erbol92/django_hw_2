from django.urls import path
from .views import recipet

urlpatterns = [
    # здесь зарегистрируйте вашу view-функцию
    path('<str:dish>/', recipet, name='recipet'),
]
