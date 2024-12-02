from django.contrib.auth import login,authenticate
from django.shortcuts import  redirect
from rest_framework.views import APIView
from rest_framework.response import Response


class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.user_type == 'doctor':
                return redirect('/doctor-dashboard')
            elif user.user_type == 'patient':
                return redirect('/home')
        return  Response({'error':'Invalid credentials'}, status=401)