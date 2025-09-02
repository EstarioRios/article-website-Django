from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

# --------------------


from .models import Blog, Comment
from .serializers import BlogFullSerializer, BlogListSerializer, CommentSerializer

# --------------------


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog(request):
    try:
        user_auth = JWTAuthentication().authenticate(request)
        if not user_auth:
            return Response(
                {"msg": "your JWT isn't fine"}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            owner, _ = user_auth

    except AuthenticationFailed:
        return Response(
            {"msg": "your JWT isn't fine"}, status=status.HTTP_400_BAD_REQUEST
        )

    blog_title = request.data.get("title")
    blog_description = request.data.get("description")
    blog_tags = request.data.get("tags")
    blog_content = request.data.get("content")

    if not blog_title:
        return Response(
            {"msg": "title is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    if not blog_description:
        return Response(
            {"msg": "description is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not blog_content:
        return Response(
            {"msg": "content is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        blog = Blog.objects.create(
            title=blog_title, description=blog_description, tags=blog_tags, owner=owner
        )
        return Response(
            {"blog": BlogFullSerializer(blog).data}, status=status.HTTP_201_CREATED
        )
    except ValueError as ve:
        return Response({"msg": f"{ve}"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def sub_comment(request):
    content = request.data.get("content")
    blog_id = request.data.get("blog_id")

    if not content:
        return Response(
            {"msg": "content is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    if not blog_id:
        return Response(
            {"msg": "blog_id is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        blog = Blog.objects.filter(id=blog_id)
    except Blog.DoesNotExist:
        return Response(
            {"msg": f"there is no blog with {blog_id} id"},
            status=status.HTTP_404_NOT_FOUND,
        )
    try:
        comment = Comment.objects.create(content=content, blog=blog)
        return Response(
            {"comment": CommentSerializer(comment).data}, status=status.HTTP_201_CREATED
        )

    except ValueError as ve:
        return Response({"msg": f"{ve}"}, status=status.HTTP_400_BAD_REQUEST)
