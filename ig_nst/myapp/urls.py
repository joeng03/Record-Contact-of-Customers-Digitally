from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('posted',views.result)
]