from django.contrib.auth import login as log, authenticate
from django.shortcuts import render
from rest_framework import generics, status, exceptions, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from todoproject.settings import BASE_BACK_URL
from users.models import User
from users.serializers import RegistrationSerializer, LoginSerializer, LoginResponseSerializer, UserSerializer, \
    LogOutRefreshTokenSerializer, ResetPasswordEmailRequestSerializer, UpdatePasswordSerializer
from users.services import generate_random_password
from users.utils import Util


# Create your views here.

def get_login_response(user, request):
    refresh = RefreshToken.for_user(user)
    data = {
        "user": UserSerializer(instance=user, context={'request': request}).data,
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }
    return data


back_url = BASE_BACK_URL


class RegistrationAPIView(generics.GenericAPIView):
    """
        APIViews for signUp
    """

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        print(serializers)
        serializers.save()
        user_data = serializers.data
        user = User.objects.get(email=user_data['email'])
        user.save()
        return Response(data=get_login_response(user, request), status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    """
        LogIn with email and password
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = LoginSerializer

    #@swagger_auto_schema(responses={'200': LoginResponseSerializer()}, tags=['auth'])
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if not user:
            raise exceptions.AuthenticationFailed()
        log(request, user)
        return Response(data=get_login_response(user, request))


class UsersView(viewsets.ReadOnlyModelViewSet):
    """
        Just userView
    """

    permission_classes = ()
    authentication_classes = ()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(is_active=True)


class LogoutView(generics.GenericAPIView):
    """
        LogOUt wiht users refresh token
    """

    serializer_class = LogOutRefreshTokenSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        pass


class UserNotFound(BaseException):
    default_detail = 'user not found'
    status_code = status.HTTP_404_NOT_FOUND
    default_code = 'user_not_found'


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        email = request.data.get('email', '')
        try:
            user = User.objects.get(email=email)
            passoword = generate_random_password(16)
            user.set_password(passoword)
            user.save()
            email_body = f'Здраствуйте, {user.email}\nВот ваш новый пароль: ' + f'{passoword}'  # + '&access=' + str(access_token)
            data = {
                'email_body': email_body,
                'to_email': email,
                'email_subject': 'Восстановление пароля'
            }
            Util.send_email(data)
        except:
            raise UserNotFound()
        return Response({'success': 'We have  sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordView(generics.GenericAPIView):
    """
        Change password
    """

    serializer_class = UpdatePasswordSerializer

    # @swagger_auto_schema(responses={'200': ''}, tags=['auth'])
    # def post(self, request):
    #     serializer = UpdatePasswordSerializer(data=request.data, instance=request.user, context={'request': request})
    #     serializer.is_valid(True)
    #     serializer.save()
    #     return response.Response(status=200)

    #@swagger_auto_schema(responses={'200': LoginResponseSerializer()}, tags=['auth'])
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(True)
        password = serializer.validated_data['new_password']
        user = request.user
        if not isinstance(user, User):
            raise UserNotFound()
        user.set_password(password)
        user.save()
        return Response(data=get_login_response(user, request))