from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth


from .services import SignupDto, UserService
# Create your views here.
class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html')
    
    def post(self, request, *args, **kwargs):
        signup_dto = self._build_signup_dto(request.POST)
        result = UserService.signup(signup_dto)
        if result['error']['state']:
            return render(request, 'signup.html', result)
        auth.login(request, result['user'])
        return redirect('index')

    @staticmethod
    def _build_signup_dto(post_data):
        return SignupDto(
            user_id=post_data['user_id'],
            user_pw=post_data['user_pw'],
            user_pw_check=post_data['user_pw_check'],
            member_name=post_data['member_name'],
            member_intro=post_data['member_intro']
        )

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')