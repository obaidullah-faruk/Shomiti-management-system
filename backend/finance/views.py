from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from .serializers import InstalmentRateSerializer, InstalmentHistorySerializer
from .models import InstalmentRate
from .utils import next_month_date, today_date


class NewInstalmentRate(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = InstalmentRateSerializer

    def perform_create(self, serializer):
        # Atomic
        with transaction.atomic():
            current_instalment_rate = InstalmentRate.get_instalment_rate()
            # If current rate available
            if current_instalment_rate:
                # Set a deactivate date for that at the end of this month
                current_instalment_rate.deactivate_at_month_end()
                activation_date = next_month_date()
            else:
                activation_date = today_date()
            serializer.save(created_by=self.request.user, activation_date=activation_date)


# Get current instalment
class CurrentInstalment(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_instalment_rate = InstalmentRate.get_instalment_rate()
        serializer = InstalmentRateSerializer(current_instalment_rate)
        return Response(serializer.data)


# Installment history
class InstalmentHistory(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InstalmentHistorySerializer
    queryset = InstalmentRate.objects.filter(activation_date__lte=today_date())

