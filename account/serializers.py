from .models import Account #import member model
from django.contrib.auth.models import User # import user model
from rest_framework import serializers


# Create member serializer
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'