import tkinter as tk
from tkinter import PhotoImage, Label, Button
import os
from ...config import Config
class BaseFrame(tk.Frame):
    def __init__(self, parent, controller, bg_image_name=None):
        super().__init__(parent)
        self.controller = controller
        if bg_image_name:
            try:
                self.bg_image = PhotoImage(file=os.path.join(Config.IMAGES_DIR, bg_image_name))
                bg_label = Label(self, image=self.bg_image)
                bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            except Exception as e:
                print(f"Error loading background {bg_image_name}: {e}")
                self.configure(bg="#f0f0f0")
    def add_back_button(self):
        Button(self, text="Back", command=lambda: self.controller.show_frame("DashboardFrame", "Going Back to main page")).pack(pady=5)