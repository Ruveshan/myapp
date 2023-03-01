from rest_framework import generics

from .models import album,song,awards
from .serializers import albumSerializers,songSerializers,awardsSerializers

class albumList(generics.ListCreateAPIView):
    serializer_class = albumSerializers

    def get_queryset(self):
        querysey = album.objects.all()
        return querysey

class albumDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = albumSerializers
    queryset = album.objects.all()

class songList(generics.ListCreateAPIView):
    serializer_class = songSerializers
    queryset = song.objects.all()

class songDetail(generics.RetrieveUpdateAPIView):
    serializer_class = songSerializers
    queryset = song.objects.all()

class awardList(generics.ListCreateAPIView):
    serializer_class = awardsSerializers
    queryset = awards.objects.all()

class awardDetail(generics.RetrieveUpdateAPIView):
    serializer_class = awardsSerializers
    queryset = awards.objects.all()

