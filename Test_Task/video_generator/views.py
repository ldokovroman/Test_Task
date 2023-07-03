#from django.shortcuts import render
from wsgiref.util import FileWrapper
from django.http import Http404, HttpResponse, HttpResponseServerError
from django.views.decorators.http import require_GET
from video_generator.models import Request
from video_generator.src.video_creater import VideoCreater

@require_GET
def create_video(request):
    text = request.GET.get("text", 0)
    if not text:
        raise Http404
    req = Request(text=text)
    req.save()
    VideoCreater.create_video(text)
    try:
        file = FileWrapper(open("videos/output.mp4", "rb"))
        response = HttpResponse(content=file,
                                status=200,
                                content_type="video/mp4")
        response["Content-Disposition"] = "attachment; filename=output.mp4"
    except FileNotFoundError:
        return HttpResponseServerError()
    return response