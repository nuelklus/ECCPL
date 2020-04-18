from django.urls import path
from .views import ContactFormView
# from .views import HomeView

app_name = 'mainapp'
urlpatterns = [
    path('', ContactFormView.as_view(), name='homepage')
]
