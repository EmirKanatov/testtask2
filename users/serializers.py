from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import PasswordField
from rest_framework_simplejwt.tokens import RefreshToken

from users import profile_exceptions
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
        serializer for putput users data to user self
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone', 'first_name', 'last_name',)


class RegistrationSerializer(serializers.ModelSerializer):
    """
        Serializer for registration user
    """

    password = PasswordField(required=True, allow_blank=False, allow_null=False, min_length=8)
    password2 = PasswordField(required=True, allow_blank=False, allow_null=False, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'password2']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        if self.validated_data.get('email') is None:
            raise serializers.ValidationError({"email": "email is required"})
        account = User(email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Password must much'}
            )
        account.set_password(password)
        account.save()
        return account


class LoginSerializer(serializers.Serializer):
    """
        Serializer for login user
    """

    email = serializers.EmailField(required=True, allow_blank=False, allow_null=False)
    password = PasswordField(required=True, allow_blank=False, allow_null=False)


class LoginResponseSerializer(serializers.Serializer):
    """
        Serializer for output after login user
    """

    refresh = serializers.CharField()
    access = serializers.CharField()


class LogOutRefreshTokenSerializer(serializers.Serializer):
    """
        Serializer for refresh toekn
    """

    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']


class GoalsPlayerSerializer(serializers.Serializer):
    results = serializers.ListField()


class UpdatePasswordSerializer(serializers.Serializer):
    """
        Serializer for update user passoword
    """

    old_password = PasswordField(required=True)
    new_password = PasswordField(required=True)
    new_password_confirm = PasswordField(required=True)

    def validate_old_password(self, value):
        if self.context['request'].user.password is None:
            raise profile_exceptions.ValidationError('your account do not have a password set up')
        if not self.context['request'].user.check_password(value):
            raise profile_exceptions.ValidationError('incorrect password')
        return value

    def update(self, instance, validated_data):
        new_password = self.validated_data['new_password']
        new_password_confirm = self.validated_data['new_password_confirm']

        if new_password != new_password_confirm:
            raise serializers.ValidationError(
                {'password': 'Password must much'}
            )
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance

