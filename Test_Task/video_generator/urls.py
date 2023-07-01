from django.urls import path
from video_generator.views import create_video

urlpatterns = [
    path("", create_video, name="create_video")
]