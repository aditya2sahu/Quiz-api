from django.shortcuts import render,HttpResponse
from .models import Quiz,Questions,Answer
from .serializer import Quizserializer,Questionsserializer,createquiz,slugserializer,LoginSerializer,registrationserializers
from rest_framework import  serializers
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly,IsAuthenticated,DjangoModelPermissions


class Home(APIView):
    def get(self,request):
        quiz=Quiz.objects.all()
        permission_classes = [DjangoModelPermissions]
        ser=Quizserializer(quiz,many=True)
        return Response(ser.data)

class LoginView(APIView):
    def post(self, request,):
        serializer =LoginSerializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            name=serializer.validated_data['username']
            passs = serializer.validated_data['password']
            user =authenticate(request=self.request,username=name,password=passs)
            if user is not None:
                login(request,user)
                return Response({"Sucsses":[name]})
            else:
                return Response({"Errors": "There is no user"})
        else:
            return Response({"Errors": [serializer.errors]})

class register(APIView):
    def post(self,request):
        info=request.data
        serializers=registrationserializers(data=info)
        if serializers.is_valid():
            serializers.save()
            return Response({"succeess":[info]})
        return Response({"Errors":[serializers.errors]})

class changepassword(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated]
    def post(self,request,format=None):
        serializers=chanegserializers(data=self.request.data,context={"user":request.user})
        if serializers.is_valid():
            return Response({"MSG":"Jio done dona done"})
        return Response({"Errors":serializers.errors})