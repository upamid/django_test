from djoser.serializers import UserSerializer
from users.models import CustomUser


class UserSerializer(UserSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'id',
            'email',)
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            }
