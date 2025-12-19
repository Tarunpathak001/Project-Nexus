import customtkinter as ctk
import random
from .modern_base_frame import ModernBaseFrame
from ...core.text_to_speech import tts_service

class RandomNumberFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "random.png")
        
        ctk.CTkLabel(self.content_frame, text="🎲 Random Number Generator", font=("Roboto Medium", 24)).pack(pady=10)
        
        input_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        input_frame.pack(pady=20)
        
        ctk.CTkLabel(input_frame, text="From:").grid(row=0, column=0, padx=10)
        self.rand_low = ctk.CTkEntry(input_frame, width=80)
        self.rand_low.grid(row=0, column=1, padx=10)
        self.rand_low.insert(0, "1")
        
        ctk.CTkLabel(input_frame, text="To:").grid(row=0, column=2, padx=10)
        self.rand_high = ctk.CTkEntry(input_frame, width=80)
        self.rand_high.grid(row=0, column=3, padx=10)
        self.rand_high.insert(0, "100")
        
        ctk.CTkButton(self.content_frame, text="Generate", command=self.generate).pack(pady=20)
        
        self.random_output = ctk.CTkLabel(self.content_frame, text="?", font=("Roboto Medium", 48))
        self.random_output.pack(pady=20)
        
        self.add_back_button()

    def generate(self):
        try:
            low = int(self.rand_low.get())
            high = int(self.rand_high.get())
            if low > high:
                low, high = high, low # Swap if user confused them
                
            random_num = random.randint(low, high)
            self.random_output.configure(text=str(random_num))
            tts_service.speak(f"Number is {random_num}")
                
        except ValueError:
            self.random_output.configure(text="NaN")
            tts_service.speak("Please enter valid numbers")