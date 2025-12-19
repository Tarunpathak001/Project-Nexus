import customtkinter as ctk
from .modern_base_frame import ModernBaseFrame
from ...core.encryption import encryption_service
from ...core.logger import logger

class EncryptDecryptFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "ende.png")
        
        self.label = ctk.CTkLabel(self.content_frame, text="LOCK & KEY - Encryption", font=("Roboto Medium", 24))
        self.label.pack(pady=10)
        
        self.mode_var = ctk.StringVar(value="Encrypt")
        mode_seg = ctk.CTkSegmentedButton(self.content_frame, values=["Encrypt", "Decrypt"], variable=self.mode_var)
        mode_seg.pack(pady=10)

        self.input_text = ctk.CTkTextbox(self.content_frame, height=100, width=500)
        self.input_text.pack(pady=10)
        self.input_text.insert("0.0", "Enter text here...")
        
        ctk.CTkButton(self.content_frame, text="Process", command=self.process).pack(pady=10)
        
        ctk.CTkLabel(self.content_frame, text="Output Result:", font=("Roboto Medium", 14)).pack(pady=5)
        self.output_text = ctk.CTkTextbox(self.content_frame, height=100, width=500)
        self.output_text.pack(pady=5)
        self.output_text.configure(state="disabled") # Read-only initially
        
        self.add_back_button()

    def process(self):
        text = self.input_text.get("0.0", "end").strip()
        mode = self.mode_var.get()
        
        if not text or text == "Enter text here...":
            self.show_output("Please enter valid text.")
            return

        try:
            if mode == "Encrypt":
                result = encryption_service.encrypt(text)
            else:
                result = encryption_service.decrypt(text)
            self.show_output(result)
        except Exception as e:
            self.show_output(f"Error: {e}")
            logger.error(f"Encryption error: {e}")

    def show_output(self, text):
        self.output_text.configure(state="normal")
        self.output_text.delete("0.0", "end")
        self.output_text.insert("0.0", text)
        self.output_text.configure(state="disabled")