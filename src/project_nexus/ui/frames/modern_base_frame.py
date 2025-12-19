import customtkinter as ctk
from tkinter import PhotoImage
import os
from ...config import Config
from ...core.logger import logger

class ModernBaseFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, bg_image_name=None):
        super().__init__(parent)
        self.controller = controller
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Center Content
        
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center")

    def add_back_button(self):
        btn = ctk.CTkButton(
            self, 
            text="← Back", 
            command=lambda: self.controller.show_frame("DashboardFrame", "Going Back"),
            width=100,
            fg_color="#444444", 
            hover_color="#333333"
        )
        btn.place(relx=0.05, rely=0.05, anchor="nw")
