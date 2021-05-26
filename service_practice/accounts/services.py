from django.contrib.auth.models import User
from dataclasses import dataclass

from .models import account

@dataclass
class SignupDto():
    user_id: str
    user_pw: str
    user_pw_check: str
    member_name: str
    member_intro: str

ERROR_MSG = {
    'EXIST_ID': 'EXIST_ID',
    'MISSING_INPUT': 'MISSING_INPUT',
    'PASSWORD_CHECK': 'PASSWORD_CHECK',
}

class UserService():
    def signup(dto: SignupDto):
        print(dto)
        if (not dto.user_id or not dto.user_pw or not dto.user_pw_check):
            return {'error': {'state': True, 'msg': ERROR_MSG['MISSING_INPUT']}}
        user_check = User.objects.filter(username=dto.user_id)
        if len(user_check) > 0:
            return {'error': {'state': True, 'msg': ERROR_MSG['EXIST_ID']}}
        if dto.user_pw != dto.user_pw_check:
            return {'error': {'state': True, 'msg': ERROR_MSG['PASSWORD_CHECK']}}

        user = User.objects.create_user(username=dto.user_id, password=dto.user_pw)
        account.objects.create(user=user, name=dto.member_name, content=dto.member_intro)

        return {'error': {'state': False} ,'user': user}