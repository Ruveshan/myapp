from rest_framework import serializers
from .models import album, song, awards

class albumSerializers(serializers.ModelSerializer):
    class Meta:
        model = album
        fields = ('__all__')

class songSerializers(serializers.ModelSerializer):
    class Meta:
        model = song
        fields = ('__all__')

class awardsSerializers(serializers.ModelSerializer):
    class Meta:
        model = awards
        fields = ('__all__')