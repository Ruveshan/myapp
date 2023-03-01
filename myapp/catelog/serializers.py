from rest_framework import serializers
from .models import album, song, awards

class songSerializers(serializers.ModelSerializer):
    class Meta:
        model = song
        fields = '__all__'

class awardsSerializers(serializers.ModelSerializer):
    class Meta:
        model = awards
        fields = '__all__'

class albumSerializers(serializers.ModelSerializer):
    song = songSerializers(many=True)
    awards = awardsSerializers(many=True)

    class Meta:
        model = album
        fields = '__all__'
