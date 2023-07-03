from django.urls import path
from video_generator.views import create_video

urlpatterns = [
    path("", scrolling_text, name="scrolling_text")
]