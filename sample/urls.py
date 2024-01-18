from django.urls import path
from sample.views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
