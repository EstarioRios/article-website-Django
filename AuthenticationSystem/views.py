from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

# ---------------------

from .models import CustomUser
from .serializers import ListCustomUserSerializer, FullCustomUserSerializer

# ---------------------


@api_view(["POST"])
@permission_classes([AllowAny])
def singin(request):
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    user_name = request.data.get("user_name")
    user_type = request.data.get("user_type")
    password = request.data.get("password")

    if not all([first_name, last_name, user_name, user_type, password]):
        return Response(
            {"error": "all fields are required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if CustomUser.objects.filter(user_name=user_name).exists():
        return Response(
            {"error": f"user_name: {user_name} is already exitst"},
            status=status.HTTP_403_FORBIDDEN,
        )

    if user_type == "normal":
        try:
            user = CustomUser.objects.create_normal(
                first_name=first_name,
                last_name=last_name,
                user_name=user_name,
                password=password,
            )
            return Response(
                {"user": FullCustomUserSerializer(user).data},
                status=status.HTTP_201_CREATED,
            )
        except ValueError as e:
            return Response(
                {"error": f"{e}"},
                status=status.HTTP_403_FORBIDDEN,
            )
