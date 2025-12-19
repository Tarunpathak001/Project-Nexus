import customtkinter as ctk
import string
import random
from .modern_base_frame import ModernBaseFrame
from ...core.text_to_speech import tts_service

class PasswordGeneratorFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "password.png")
        
        self.password_length = ctk.IntVar(value=12)
        self.include_uppercase = ctk.BooleanVar(value=True)
        self.include_lowercase = ctk.BooleanVar(value=True)
        self.include_numbers = ctk.BooleanVar(value=True)
        self.include_symbols = ctk.BooleanVar(value=True)
        
        ctk.CTkLabel(self.content_frame, text="🔒 Password Generator", font=("Roboto Medium", 24)).pack(pady=10)
        
        opts_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        opts_frame.pack(pady=10, fill="x", padx=50)
        
        ctk.CTkLabel(opts_frame, text="Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        # Slider for length
        slider = ctk.CTkSlider(opts_frame, from_=4, to=32, variable=self.password_length, number_of_steps=28)
        slider.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
        
        self.len_label = ctk.CTkLabel(opts_frame, textvariable=self.password_length)
        self.len_label.grid(row=0, column=2, padx=10, pady=5)
        
        ctk.CTkCheckBox(opts_frame, text="Uppercase (A-Z)", variable=self.include_uppercase).grid(row=1, column=0, columnspan=3, sticky="w", padx=10, pady=5)
        ctk.CTkCheckBox(opts_frame, text="Lowercase (a-z)", variable=self.include_lowercase).grid(row=2, column=0, columnspan=3, sticky="w", padx=10, pady=5)
        ctk.CTkCheckBox(opts_frame, text="Numbers (0-9)", variable=self.include_numbers).grid(row=3, column=0, columnspan=3, sticky="w", padx=10, pady=5)
        ctk.CTkCheckBox(opts_frame, text="Symbols (!@#)", variable=self.include_symbols).grid(row=4, column=0, columnspan=3, sticky="w", padx=10, pady=5)
        
        ctk.CTkButton(self.content_frame, text="Generate Password", command=self.generate).pack(pady=20)
        
        self.password_output = ctk.CTkEntry(self.content_frame, width=300, font=("Roboto", 16), justify="center")
        self.password_output.pack(pady=5)
        
        self.msg_label = ctk.CTkLabel(self.content_frame, text="", text_color="gray")
        self.msg_label.pack(pady=5)
        
        self.add_back_button()

    def generate(self):
        characters = ""
        selected_options = 0
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
            selected_options+=1
        if self.include_lowercase.get():
            characters += string.ascii_lowercase
            selected_options+=1
        if self.include_numbers.get():
            characters += string.digits
            selected_options+=1
        if self.include_symbols.get():
            characters += string.punctuation
            selected_options+=1
            
        if not characters:
            self.msg_label.configure(text="Select at least one character type.")
            return
            
        if self.password_length.get() < selected_options:
             # Should be rare with slider min 4
            self.msg_label.configure(text="Length too short for selected options")
            return

        password = ''.join(random.choice(characters) for _ in range(self.password_length.get()))
        
        self.password_output.delete(0, "end")
        self.password_output.insert(0, password)
        self.msg_label.configure(text="Password generated! Copy to clipboard.")
        tts_service.speak("Password Generated")