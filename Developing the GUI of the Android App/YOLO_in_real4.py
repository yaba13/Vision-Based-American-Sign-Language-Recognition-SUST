import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from kivy.uix.label import Label

import torch
import numpy as np
import cv2

Window.clearcolor = (0, 0, 0, 0)
Window.size = (400, 600)
class ASL_Translator(App):
    def build(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/mohamed alameen/Desktop/ASL project/yolov5-master/bestv5x.pt', force_reload=True)
        self.image = Image(size_hint_y=None, height=400, allow_stretch=True, keep_ratio=False)
        self.button =Button(text='Start Translation',
                        font_size=14,
                        background_color=(0.5, 0.25, 0.5, 1),
                        bold=True,
                        size=(200, 50),    
                        size_hint=(1,.1),
                        background_normal='',
                        color=(1, 1, 1, 1))
        self.verification_label = Label(text="Detection Uninitiated", size_hint=(1,.1))#the translated text should apper here btw 
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.image)
        layout.add_widget(self.button)
        layout.add_widget(self.verification_label)
        self.cap = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/30.0)

        return layout

    def update(self, dt):
    
        ret, frame = self.cap.read()
        
        results = self.model(frame)
        buf = cv2.flip(np.squeeze(results.render()), 0).tostring()
        image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = image_texture

if __name__ == '__main__':
    ASL_Translator().run()
