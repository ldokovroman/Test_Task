from django.urls import path
from video_generator.views import scrolling_text

urlpatterns = [
    path("", scrolling_text, name="scrolling_text")
]