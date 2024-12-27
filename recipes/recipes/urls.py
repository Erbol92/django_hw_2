from django.urls import path, include

urlpatterns = [
    # здесь зарегистрируйте вашу view-функцию
    path('', include('calculator.urls')),
]
