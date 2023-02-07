from todoproject.exceptions import BaseException
from rest_framework import status


class UserAlreadyExist(BaseException):
    default_code = 'user_exists'
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "user already exists"


class UserNotFound(BaseException):
    default_detail = 'user not found'
    status_code = status.HTTP_404_NOT_FOUND
    default_code = 'user_not_found'


class UserNotVerified(BaseException):
    default_detail = 'user not verified'
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_code = 'user_not_virified'


class ChnageTeamDenied(BaseException):
    status_code = status.HTTP_423_LOCKED
    default_detail = ('Команду можно менять только в определенное время.')
    default_code = 'fuck u'
