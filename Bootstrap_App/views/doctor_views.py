from rest_framework import viewsets
from django.shortcuts import render
from DjangoBootstrap.wsgi import application
from ..models import Doctors, Appointment
from ..serializers import DoctorsSerializer, AppointmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
    @action(detail=True, methods=['GET'])
    def docappointments(self, request):
        doctor = self.get_object()
        appointments = Appointment.objects.filter(doctor=doctor)
        serializer = AppointmentSerializer(appointments, many=True)
        return  Response(serializer.data)
    def doctor_dashboard(request):
        return render(request, 'doctor_dashboard.html')
