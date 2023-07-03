import cv2 as cv
import numpy as np
import math as m

class VideoCreater:
    width = 100
    height = 100
    size_video = (width, height)
    fps = 30
    duration = 3
    n_frames = fps * duration
    fourcc = cv.VideoWriter_fourcc("m", "p", "4", "v")
    font = cv.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_color = (0, 0, 255)
    thickness = 1

    @classmethod
    def create_video(cls, text):
        video = cv.VideoWriter("/videos/output.mp4", cls.fourcc, cls.fps, cls.size_video)
        text_size = cv.getTextSize(text, cls.font, cls.font_scale, cls.thickness)[0]
        text_x = cls.width
        text_y = int((cls.height + text_size[1]) / 2)
        text_distance = cls.width + text_size[0]
        dx = m.ceil(text_distance / cls.n_frames)
        background = np.array([0, 255, 255] * (cls.width * cls.height), dtype=np.uint8)
        background = background.reshape((cls.height, cls.width, 3))

        for _ in range(cls.n_frames):
            frame = np.array(background)
            cv.putText(frame, text, (text_x, text_y), font, font_scale, font_color, thickness, cv.LINE_AA)
            video.write(frame)
            text_x -= dx

        video.release()
