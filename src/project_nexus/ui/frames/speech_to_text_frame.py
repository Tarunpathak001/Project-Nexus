import customtkinter as ctk
from .modern_base_frame import ModernBaseFrame
from ...core.speech_to_text import stt_service
from ...core.text_to_speech import tts_service

class SpeechToTextFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "stt.png")
        
        ctk.CTkLabel(self.content_frame, text="🎤 Speech to Text", font=("Roboto Medium", 24)).pack(pady=10)
        
        self.stt_text = ctk.CTkTextbox(self.content_frame, height=200, width=500, font=("Roboto", 16))
        self.stt_text.pack(pady=20)
        self.stt_text.insert("0.0", "Press the button and start speaking...")
        
        self.listen_btn = ctk.CTkButton(self.content_frame, text="Start Listening", command=self.listen, width=200, height=50, font=("Roboto Medium", 16))
        self.listen_btn.pack(pady=20)
        
        self.status_label = ctk.CTkLabel(self.content_frame, text="", text_color="yellow")
        self.status_label.pack(pady=5)
        
        self.add_back_button() 

    def listen(self):
        self.status_label.configure(text="Listening... speak now")
        self.listen_btn.configure(state="disabled")
        self.update_idletasks()
        
        try:
            result = stt_service.listen()
            
            self.stt_text.delete("1.0", "end")
            if "error" in result:
                self.stt_text.insert("end", f"Error: {result['error']}")
                self.status_label.configure(text="Failed to hear audio", text_color="red")
                tts_service.speak("I couldn't hear that clearly")
            else:
                text = result.get("text", "")
                self.stt_text.insert("end", text)
                self.status_label.configure(text="Done", text_color="green")
                
        except Exception as e:
            self.status_label.configure(text=f"Error: {e}", text_color="red")
            
        self.listen_btn.configure(state="normal")