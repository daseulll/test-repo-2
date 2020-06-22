from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from .serializers import PostSerializer
from .models import Post

@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def post_collection(request):
    if request.method == 'GET':
        post = Post.objects.get(id=2)
        Post.get_objects()

        serializer = PostSerializer(post)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        post.published()
        if serializer.is_valid():
            serializer.save()
            return Response({'code':'1', "data": serializer.data})

    if request.method == 'PATCH':
        post_id = request.data.get('id')
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response({'code':'1', "data": serializer.data})

    if request.method == 'PUT':
        post_id = request.data.get('id')
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'code':'1', "data": serializer.data})

    if request.method == 'DELETE':
        post_id = request.data.get('id')
        post = Post.objects.get(id=post_id)  
        post.delete()
        
        post.view_count = 3
        post.save()

        return Response({'code':'1'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def post_object(request, id):
    post = Post.objects.get(id=id)
    serializer = PostSerializer(post)
    
    return Response({'code':'1', "data": serializer.data})


class PostListView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

