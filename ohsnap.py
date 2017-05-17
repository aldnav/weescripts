#!/usr/bin/env python
import os
from datetime import datetime
import pygame
import pygame.camera

pygame.camera.init()
cameras = pygame.camera.list_cameras()
assert len(cameras) > 0
cam = pygame.camera.Camera(cameras[0], (640, 480))
cam.start()
img = cam.get_image()
now = datetime.now().strftime('%Y%d%m-%H:%M:%S')
path = os.path.join(os.environ.get('SNAPS_DIR'), '{}.png'.format(now))
pygame.image.save(img, path)
cam.stop()
