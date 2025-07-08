from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .models import User
from .serializers import MemberCreateSerializer, MemberSerializer, PasswordUpdateSerializer


class MemberCreateView(generics.CreateAPIView):
    """
    To create a new member account (Only by admin user)
    """
    serializer_class = MemberCreateSerializer
    permission_classes = [IsAdminUser]


# List Of Members
class MemberList(generics.ListAPIView):
    """
    List of all members (Only by admin user).
    """
    serializer_class = MemberSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.filter(is_member=True)


class PasswordChangeView(generics.UpdateAPIView):
    """
    Update individuals own password.
    """
    serializer_class = PasswordUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Password updated successfully."},
            status=status.HTTP_200_OK
        )
