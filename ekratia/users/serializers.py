from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    """
    avatar = serializers.CharField(source='get_avatar', read_only=True)
    full_name = serializers.CharField(source='get_full_name_or_username', read_only=True)
    rank = serializers.CharField(source='get_pagerank', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'avatar', 'full_name', 'rank')
