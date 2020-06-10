from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostAPIView(generics.APIView):

    def get(self, request):
        print("get")
        print("This is Django View")
        return Response({'code':'1'}, status=status.HTTP_200_OK)
        

