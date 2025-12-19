import customtkinter as ctk
from .modern_base_frame import ModernBaseFrame
from ...core.text_to_speech import tts_service

class TextToSpeechFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "tts.png")
        
        ctk.CTkLabel(self.content_frame, text="🗣️ Text to Speech", font=("Roboto Medium", 24)).pack(pady=10)
        
        self.tts_text = ctk.CTkTextbox(self.content_frame, height=150, width=500, font=("Roboto", 16))
        self.tts_text.pack(pady=20)
        self.tts_text.insert("0.0", "Enter text here and I will speak it for you.")
        
        ctk.CTkButton(self.content_frame, text="Speak", command=self.speak, width=200, height=40).pack(pady=10)
        
        self.add_back_button()

    def speak(self):
        text = self.tts_text.get("1.0", "end").strip()
        if text:
            tts_service.speak(text)
        else:
            tts_service.speak("Please enter some text")