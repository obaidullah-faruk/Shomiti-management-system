from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from .serializers import InstalmentRateSerializer, InstalmentHistorySerializer
from .models import InstalmentRate
from .utils import next_month_date, today_date


class NewInstalmentRate(generics.CreateAPIView):
    """
    Allows admin to create a new instalment rate.

    - If a current active instalment exists, it is deactivated by setting its deactivated_at
      to the end of the current month.
    - The new instalment becomes active either from today or the next month, depending on the scenario.
    """
    permission_classes = [IsAdminUser]
    serializer_class = InstalmentRateSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            current_instalment_rate = InstalmentRate.get_instalment_rate()
            if current_instalment_rate:
                current_instalment_rate.deactivate_at_month_end()
                activation_date = next_month_date()
            else:
                activation_date = today_date()
            serializer.save(created_by=self.request.user, activation_date=activation_date)


class CurrentInstalment(APIView):
    """
    Returns the currently active instalment rate.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_instalment_rate = InstalmentRate.get_instalment_rate()
        serializer = InstalmentRateSerializer(current_instalment_rate)
        return Response(serializer.data)


class InstalmentHistory(generics.ListAPIView):
    """
    Returns the list of past and current instalment rates (history) up to today.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = InstalmentHistorySerializer
    queryset = InstalmentRate.objects.filter(activation_date__lte=today_date())

