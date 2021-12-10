from rest_framework import status
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from user.serializers.user import UserSerializer
from user.permissions import IsOwner
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

# fbv
@api_view(['GET'])
@parser_classes([JSONParser])
@permission_classes([IsAuthenticated])
def get_user(request, id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET'])
@parser_classes([JSONParser])
@permission_classes([IsOwner])
def get_user2(request, id):
    """
    method has_object_permission not working in FBV
    """
    #user = User.objects.get(id=id)
    user = get_object_or_404(User, pk=id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status.HTTP_200_OK)


# cbv
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (JSONParser,)
    permission_classes = (IsOwner,)
