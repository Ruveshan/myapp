from django.urls import path
from .views import albumList, albumDetail, songList, songDetail, awardList, awardDetail

urlpatterns = [
    path('album/',albumList.as_view()),
    path('album/<int:pk>/',albumDetail.as_view()),
    path('song/',songList.as_view()),
    path('song/<int:pk>/',songDetail.as_view()),
    path('award/',awardList.as_view()),
    path('award/<int:pk>/',awardDetail.as_view()),
]