from rest_framework import serializers
from .models import InstalmentRate


class InstalmentRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstalmentRate
        fields = ['amount']

    def validate_amount(self, attrs):
        if attrs <= 0:
            raise serializers.ValidationError('Amount must be greater than 0')
        return attrs


class InstalmentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InstalmentRate
        exclude = ['created_by']
