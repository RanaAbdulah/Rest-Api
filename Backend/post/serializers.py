from rest_framework import serializers
from .models import Registration, RegistrationAdmin

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"

class RegistrationAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationAdmin
        fields = "__all__"




        # fields = ('first_name', 'last_name', 'email', 'password')
        # extra_kwargs = {'first_name': {'required': False,
        #                           'allow_blank': False},
        #                 'last_name': {'required': False,
        #                           'allow_blank': False},
        #                 'email': {'required': False,
        #                           'allow_blank': False},
        #                 'password': {'required': False,
        #                           'allow_blank': False}}







        