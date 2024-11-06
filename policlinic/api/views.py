from django.shortcuts import render
from rest_framework import generics

from app.models import *
from .serializers import *


def index(request):
    return render(request, "index.html")

class DoctorsView(generics.ListCreateAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer


class InstitutionView(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class RecordsView(generics.ListCreateAPIView):
    queryset = Records.objects.all()
    serializer_class = RecordSerializer


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilePDFView(generics.ListCreateAPIView):
    queryset = FilePDF.objects.all()
    serializer_class = FilePDFSerializer
