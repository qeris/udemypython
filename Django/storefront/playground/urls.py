from django.urls import URLPattern, path
from . import views

# URL Config
urlpatterns = [
    path('hello/', views.say_hello)
]