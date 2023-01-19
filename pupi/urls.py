from django.urls import path
from pupi.views import home
from pupi.views import contacts
from pupi.apps import PupiConfig

app_name = PupiConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
]