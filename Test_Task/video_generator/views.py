#from django.shortcuts import render
from wsgiref.util import FileWrapper

from django.http import Http404, HttpResponse, HttpResponseServerError
from django.views.decorators.http import require_GET
import cv2 as cv
import numpy as np
import math as m

@require_GET
def create_video(request, text):
    if not text:
        return Http404
    width = 100
    height = 100
    size_video = (width, height)
    fps = 30
    duration = 3
    fourcc = cv.VideoWriter_fourcc("m", "p", "4", "v")
    video = cv.VideoWriter("output.mp4", fourcc, fps, size_video)

    font = cv.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_color = (0, 0, 255)
    thickness = 1
    text_size = cv.getTextSize(text, font, font_scale, thickness)[0]
    text_x = width
    text_y = int((height + text_size[1]) / 2)
    text_distance = width + text_size[0]
    dx = m.ceil(text_distance / (fps * duration))
    background = np.array([0, 255, 255] * (width * height), dtype=np.uint8)
    background = background.reshape((height, width, 3))

    for i in range(fps * duration):
        frame = np.array(background)
        cv.putText(frame, text, (text_x, text_y), font, font_scale, font_color, thickness, cv.LINE_AA)
        video.write(frame)
        text_x -= dx
    video.release()
    try:
        file = FileWrapper(open("video.mp4", "rb"))
        response = HttpResponse(content=file,
                                status=200,
                                content_type="video/mp4")
        response["Content-Disposition"] = "attachment; filename=output.mp4"
    except FileNotFoundError:
        return HttpResponseServerError()
    return response