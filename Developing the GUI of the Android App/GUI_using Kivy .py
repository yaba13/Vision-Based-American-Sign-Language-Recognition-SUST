# Import kivy dependencies first
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Import kivy UX components
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label


from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from kivy.logger import Logger

# Import other dependencies
import cv2
import os
import numpy as np

Window.clearcolor=(0,0,0,0) 
Window.size = (400,600)

class Cam(App):
    def build(self):

        
        self.web_cam = Image(size_hint_y=None, height=400, allow_stretch=True, keep_ratio=False)
        self.button = Button(text="capture", size=(100, 50), size_hint=(1,.1))
        self.verification_label = Label(text="Detection Uninitiated", size_hint=(1,.1))
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.web_cam)
        layout.add_widget(self.button)
        layout.add_widget(self.verification_label)
        
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/33.0)
        

        return layout
    def update(self, *args):
        
        ret, frame = self.capture.read()
        frame = frame[:, :, :]
        buf = cv2.flip(frame, 0).tostring()
        img_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.web_cam.texture = img_texture

if __name__=='__main__':
    Cam().run()



