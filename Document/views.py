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


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def edit_comment(request):
    comment_id = request.data.get("commentId")
    new_content = request.data.get("newContent")

    user, _ = JWTAuthentication(request)
    if not user:
        return Response(
            {"error": "your JWT is not ok"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not all([comment_id, new_content]):
        return Response(
            {"error": "all fields are required"}, status=status.HTTP_400_BAD_REQUEST
        )

    if Comment.objects.filter(id=comment_id).exist():
        comment = Comment.objects.get(id=comment_id)
        if comment.owner != user:
            return Response(
                {"error": "you are not allowed"}, status=status.HTTP_403_FORBIDDEN
            )
        comment.content = new_content
        comment.save()
        return Response(
            {"comment": CommentSerializer(comment).data}, status=status.HTTP_200_OK
        )

    else:
        return Response(
            {"error": f"there is not comment by id: {comment_id}"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def remove_comment(request):
    comment_id = request.data.get("comentId")

    if not comment_id:
        return Response(
            {"error": "comment_id is required field"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not Comment.objects.filter(id=comment_id).exists():
        return Response(
            {"error": f"there is no comment by id: {comment_id}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    comment = Comment.objects.get(id=comment_id)
    try:
        comment.delete()
        return Response({}, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response({"error": f"{e}"}, status=status.HTTP_403_FORBIDDEN)
