from django.urls import path

from . import views

app_name = 'joke_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('return_punchline', views.return_punchline, name='return_punchline'),
]
