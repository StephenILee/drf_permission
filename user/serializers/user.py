from rest_framework import serializers as s


class UserSerializer(s.Serializer):
    id = s.IntegerField(read_only=True)
    username = s.CharField()
    password = s.CharField(write_only=True, required=False)
    email = s.CharField()
    is_superuser = s.BooleanField()
    is_active = s.BooleanField()
    date_joined = s.DateTimeField()