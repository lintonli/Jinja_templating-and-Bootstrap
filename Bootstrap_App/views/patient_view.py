from rest_framework import  viewsets
from ..models import  Patients
from ..serializers import PatientsSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer