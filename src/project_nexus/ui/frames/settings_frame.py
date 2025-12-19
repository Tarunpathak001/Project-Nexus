import customtkinter as ctk
from .modern_base_frame import ModernBaseFrame
from ...config import Config
from ...core.text_to_speech import tts_service
import os

class SettingsFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, None)
        
        self.label = ctk.CTkLabel(self.content_frame, text="⚙️ Settings", font=("Roboto Medium", 24))
        self.label.pack(pady=20)
        
        # Appearance Mode
        ctk.CTkLabel(self.content_frame, text="Appearance Mode:", font=("Roboto", 16)).pack(pady=5)
        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.content_frame, 
            values=["Dark", "Light", "System"],
            command=self.change_appearance_mode
        )
        self.appearance_mode_menu.pack(pady=5)
        self.appearance_mode_menu.set("Dark")
        
        # API Key Management (Visual primarily, environment variable handling is complex at runtime)
        ctk.CTkLabel(self.content_frame, text="OpenWeather API Key:", font=("Roboto", 16)).pack(pady=10)
        self.api_entry = ctk.CTkEntry(self.content_frame, width=300, placeholder_text=Config.API_KEY[:10] + "...")
        self.api_entry.pack(pady=5)
        ctk.CTkButton(self.content_frame, text="Update Key", command=self.update_key).pack(pady=5)
        
        # About
        ctk.CTkLabel(self.content_frame, text="Project Nexus v2.0\nModernized with CustomTkinter & SQLite", font=("Roboto", 12), text_color="gray").pack(pady=30, side="bottom")

        self.add_back_button()

    def change_appearance_mode(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)
        tts_service.speak(f"Appearance changed to {new_appearance_mode}")

    def update_key(self):
        # In a real app, we would write this to .env
        tts_service.speak("This feature is currently a placeholder for security reasons.")
