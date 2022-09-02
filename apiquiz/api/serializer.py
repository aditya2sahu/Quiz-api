from rest_framework import  serializers
from.models import Quiz,Questions,Answer



class Ansserializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=["Option","righ",]

class Questionsserializer(serializers.ModelSerializer):
    options=Ansserializer(many=True,read_only=True)
    class Meta:
        model=Questions
        fields=["subquestions","options",]

class Quizserializer(serializers.ModelSerializer):
    questions=Questionsserializer(many=True,read_only=True)
    class Meta:
        model=Quiz
        fields=["Subject","StartTime","EndTime","questions",]


class createquiz(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ["Subject", "StartTime", "EndTime"]


class slugserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ["Subject", "StartTime", "EndTime"]
        lookip_field="slug"
        extra_kwargs={
            'url':{'lookip_field':"slug"}
        }




from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class registrationserializers(serializers.ModelSerializer):
     email = serializers.EmailField(
     required=True,
     validators=[UniqueValidator(queryset=User.objects.all())])
     password = serializers.CharField(
     write_only=True, required=True, validators=[validate_password])
     password2 = serializers.CharField(write_only=True, required=True)
     def validate(self, attrs):
          if  attrs["password"]!=  attrs["password2"] :
               raise serializers.ValidationError({"password": "Password fields didn't match."})
          return attrs

     def create(self, validated_data):
          user=User.objects.create(username=validated_data["username"],email=validated_data["email"])
          user.set_password(validated_data["password"])
          user.save()
          return user

class LoginSerializer(serializers.Serializer):
   
    username = serializers.CharField(
        label="Username",
        write_only=True,
        required=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True,
        required=True
    )

from django.contrib.auth.hashers import check_password
#Chaneg password
class chanegserializers(serializers.Serializer):
     old_password=serializers.CharField(max_length=200,required=True,write_only=True)
     password=serializers.CharField(max_length=200,required=True,write_only=True,validators=[validate_password])
     password2=serializers.CharField(max_length=200,required=True,write_only=True)

     def validated_old_password(self, value):
         user = self.context.get("user")
         if not user.check_password(value):
             raise serializers.ValidationError({"Old_Password": "Old_password Wrong."})
         return value

     def validate(self, attrs):
         user = self.context.get("user")
         if attrs["password"]!=  attrs["password2"] :
             raise serializers.ValidationError({"password": "Password fields didn't match."})
         user.set_password( attrs["password"])
         user.save()
         return attrs
