import customtkinter as ctk
from .modern_base_frame import ModernBaseFrame
from ...core.text_to_speech import tts_service

class CalculatorFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "calc.png")
        
        self.current_expr = ""
        
        # Display
        self.display = ctk.CTkEntry(self.content_frame, width=300, font=("Roboto Medium", 24), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
        self.display.insert(0, "0")
        
        # Buttons Configuration
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for button in buttons:
            cmd = lambda x=button: self.on_button_click(x)
            
            # Specific styling for operators
            fg_color = "#1f6aa5" if button not in ['=', 'C', '/', '*', '-', '+'] else "#ff9800"
            if button == 'C': fg_color = "#f44336"
            
            ctk.CTkButton(
                self.content_frame, 
                text=button, 
                width=60, 
                height=60,
                font=("Roboto Medium", 20),
                fg_color=fg_color,
                command=cmd
            ).grid(row=row_val, column=col_val, padx=5, pady=5)
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        self.add_back_button()

    def on_button_click(self, char):
        if char == 'C':
            self.current_expr = ""
            self.update_display()
        elif char == '=':
            try:
                result = str(eval(self.current_expr))
                self.current_expr = result
                tts_service.speak(f"Equals {result}")
            except Exception:
                self.current_expr = "Error"
                tts_service.speak("Error")
            self.update_display()
        else:
            self.current_expr += char
            self.update_display()

    def update_display(self):
        self.display.delete(0, "end")
        self.display.insert(0, self.current_expr if self.current_expr else "0")