# from .views import login
from django.urls import path
from .views import post_collection, post_object

urlpatterns = [
    path('post/', post_collection),
    path('post/<int:id>/', post_object)
]