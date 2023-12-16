from rest_framework import serializers
from .models import *


class todoserializer(serializers.ModelSerializer):
    class Meta:
        model=todos
        fields='__all__'

#
# class movieserializer(serializers.ModelSerializer):
#     class Meta:
#         model= movies
#         fields='__all__'