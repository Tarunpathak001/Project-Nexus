import customtkinter as ctk
from .modern_base_frame import ModernBaseFrame
from ...core.translator import translator_service

class TranslatorFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "translator.png")
        
        ctk.CTkLabel(self.content_frame, text="🌐 Language Translator", font=("Roboto Medium", 24)).pack(pady=10)
        
        # Languages
        langs = list(translator_service.languages.values())
        
        combo_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        combo_frame.pack(pady=10, fill="x")
        
        # Source (Auto or English default) - googletrans usually detects, but we can set explicit
        # For simplicity, we create "Auto" or just let user pick.
        # Check if 'english' is in langs.
        
        self.src_lang = ctk.StringVar(value="english")
        self.dest_lang = ctk.StringVar(value="french")
        
        ctk.CTkLabel(combo_frame, text="From:").pack(side="left", padx=5)
        self.src_menu = ctk.CTkComboBox(combo_frame, values=langs, variable=self.src_lang, width=150)
        self.src_menu.pack(side="left", padx=5)
        
        ctk.CTkLabel(combo_frame, text="To:").pack(side="left", padx=5)
        self.dest_menu = ctk.CTkComboBox(combo_frame, values=langs, variable=self.dest_lang, width=150)
        self.dest_menu.pack(side="left", padx=5)
        
        # Input
        self.input_text = ctk.CTkTextbox(self.content_frame, height=100, width=500)
        self.input_text.pack(pady=10)
        self.input_text.insert("0.0", "Type text to translate here...")
        
        # Controls
        btn_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        btn_frame.pack(pady=10)
        
        ctk.CTkButton(btn_frame, text="Translate", command=self.translate_text).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Clear", command=self.reset_translator, fg_color="gray").pack(side="left", padx=10)
        
        # Output
        self.output_text = ctk.CTkTextbox(self.content_frame, height=100, width=500)
        self.output_text.pack(pady=10)
        self.output_text.configure(state="disabled") # Read-only initially
        
        self.add_back_button()

    def translate_text(self):
        src = self.src_lang.get()
        dest = self.dest_lang.get()
        text = self.input_text.get("1.0", "end").strip()
        
        if not text or text == "Type text to translate here...":
            return

        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("0.0", "Translating...")
        self.output_text.update()
        
        result = translator_service.translate(text, src, dest)
        
        self.output_text.delete("1.0", "end")
        if "error" in result:
             self.output_text.insert("0.0", f"Error: {result['error']}")
        else:
             self.output_text.insert("0.0", result["text"])
             if result.get("pronunciation"):
                 self.output_text.insert("end", f"\n\nPronunciation: {result['pronunciation']}")
        
        self.output_text.configure(state="disabled")

    def reset_translator(self):
        self.input_text.delete("1.0", "end")
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.configure(state="disabled")