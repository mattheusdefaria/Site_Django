from django.urls import path
from meu_blog.views import resposta

urlpatterns = [
    path('', resposta)
]
