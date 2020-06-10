# from .views import login
from django.urls import path
from .views import PostAPIView
# path('/v2/post/', login)
urlpatterns = [
    path('posts/', PostAPIView.as_view())
]