from rest_framework import serializers
from .models import Setting


class SettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Setting
        fields = ['terms', 'evaluation_days']
