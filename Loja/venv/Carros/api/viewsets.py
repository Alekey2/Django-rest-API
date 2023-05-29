from rest_framework import viewsets
from Carros.api import serializers
from Carros import models


class CarroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CarrosSerializers
    queryset = models.Carros.objects.all()