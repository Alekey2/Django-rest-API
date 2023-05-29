from rest_framework import serializers
from Carros import models

class CarrosSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Carros
        fields = '__all__'