import customtkinter as ctk
from datetime import datetime
from .modern_base_frame import ModernBaseFrame
from ...core.logger import logger

class DashboardFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "main.png")
        
        header_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=(10, 20))
        
        self.param_label = ctk.CTkLabel(
            header_frame, 
            text="PROJECT NEXUS", 
            font=("Roboto Medium", 40),
            text_color="#3B8ED0"
        )
        self.param_label.pack()
        
        self.subtitle = ctk.CTkLabel(
            header_frame, 
            text="Your Personal AI Assistant", 
            font=("Roboto", 16),
            text_color="gray"
        )
        self.subtitle.pack()
        
        self.scrollable = ctk.CTkScrollableFrame(
            self.content_frame, 
            width=900, 
            height=600, 
            fg_color="transparent" 
        )
        self.scrollable.pack(fill="both", expand=True, padx=20, pady=10)
        
        categories = [
            {
                "title": "🚀 Productivity",
                "color": "#2CC985",
                "items": [
                    ("✅ To-Do List", "ToDoFrame"),
                    ("📓 Quick Notes", "NotesFrame"),
                    ("📝 Sticky Notes", "StickyNotesFrame"),
                    ("💰 Expense Tracker", "ExpenseTrackerFrame"),
                ]
            },
            {
                "title": "🛠️ Utilities",
                "color": "#EFA43D",
                "items": [
                    ("🌤️ Weather", "WeatherFrame"),
                    ("🧮 Calculator", "CalculatorFrame"),
                    ("🌐 Translator", "TranslatorFrame"),
                    ("⏱️ Stopwatch", "StopWatchFrame"),
                    ("🎲 Random Num", "RandomNumberFrame"),
                ]
            },
            {
                "title": "🔒 Security & System",
                "color": "#E54D49",
                "items": [
                    ("🔐 Encrypt/Decrypt", "EncryptDecryptFrame"),
                    ("🔑 Password Gen", "PasswordGeneratorFrame"),
                    ("⚙️ Settings", "SettingsFrame"),
                ]
            },
            {
                "title": "🎭 Media & Fun",
                "color": "#9E5FD3",
                "items": [
                    ("📹 YouTube", "YoutubeFrame"),
                    ("🐍 Snake Game", "SnakeGameFrame"),
                    ("⌨️ Typing Speed", "TypingSpeedFrame"),
                    ("🗣️ Text to Speech", "TextToSpeechFrame"),
                    ("🎤 Speech to Text", "SpeechToTextFrame"),
                ]
            }
        ]
        
        for cat in categories:
            self.create_category_section(cat["title"], cat["color"], cat["items"])

    def create_category_section(self, title, color, items):
        sec_label = ctk.CTkLabel(
            self.scrollable, 
            text=title, 
            font=("Roboto Medium", 20), 
            text_color=color, 
            anchor="w"
        )
        sec_label.pack(fill="x", pady=(20, 10), padx=10)
        
        grid_frame = ctk.CTkFrame(self.scrollable, fg_color="transparent")
        grid_frame.pack(fill="x", padx=10)
        
        for i in range(4):
            grid_frame.grid_columnconfigure(i, weight=1)
            
        for i, (btn_text, frame_name) in enumerate(items):
            btn = ctk.CTkButton(
                grid_frame,
                text=btn_text,
                font=("Roboto", 14),
                height=60,
                fg_color="#2B2B2B",  
                hover_color=color,   
                border_width=2,
                border_color="#3A3A3A",
                corner_radius=10,
                command=lambda f=frame_name, t=btn_text: self.navigate(f, t)
            )
            btn.grid(row=i//4, column=i%4, padx=8, pady=8, sticky="ew")

    def navigate(self, frame_name, text_desc):
        try:
            self.controller.show_frame(frame_name, f"{text_desc}")
        except Exception as e:
            logger.error(f"Navigation error: {e}")
            print(e)