from rest_framework import viewsets,status
from rest_framework.response import Response

from . import appointment
from  ..models import Appointment
from ..serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()

    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def delete(self, request, *args, **kwargs):
        appointment=self.get_object()
        appointment.delete()
        return Response({"message": "Appointment deleted"})