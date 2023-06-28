from django.urls import path
from views import create_video

urlpatterns = [
    path("<str:text>/", create_video, name="create_video")
]