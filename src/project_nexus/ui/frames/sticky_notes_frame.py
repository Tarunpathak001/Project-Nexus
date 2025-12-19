import customtkinter as ctk
import webbrowser
import os
from .modern_base_frame import ModernBaseFrame
from ...core.text_to_speech import tts_service
from ...config import Config

class StickyNotesFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "stick.png")
        
        ctk.CTkLabel(self.content_frame, text="📝 Sticky Notes App", font=("Roboto Medium", 24)).pack(pady=10)
        
        ctk.CTkLabel(self.content_frame, text="This will launch a standalone Sticky Notes web interface.", font=("Roboto", 14)).pack(pady=20)
        
        ctk.CTkButton(self.content_frame, text="Launch Sticky Notes", command=self.open_note, width=200, height=50).pack(pady=10)
        
        self.add_back_button()

    def open_note(self):
        tts_service.speak("Opening Sticky Notes")
        path = Config.STICKY_NOTE_PATH
        if os.path.exists(path):
            webbrowser.open(f"file://{path}")
        else:
            # Fallback for dev environment or if config is just relative
            # If path ends with index.html, check if it exists relative to cwd
            if not os.path.isabs(path):
                 path = os.path.abspath(path)
            
            if os.path.exists(path):
                 webbrowser.open(f"file://{path}")
            else:
                 # Try to find it in assets
                 # Expected: assets/sticky_note/index.html
                 webbrowser.open(f"file://{os.path.abspath('assets/sticky_note/index.html')}")