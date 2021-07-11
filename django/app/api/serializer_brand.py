from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Brand, User, SubscribeBrand


# 수정 필요
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandSubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeBrand
        fields = '__all__'