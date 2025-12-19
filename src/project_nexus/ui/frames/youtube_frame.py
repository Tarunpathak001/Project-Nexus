import customtkinter as ctk
import webbrowser
from .modern_base_frame import ModernBaseFrame
from ...core.text_to_speech import tts_service

class YoutubeFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "youtube.png")
        
        ctk.CTkLabel(self.content_frame, text="📺 YouTube Search", font=("Roboto Medium", 24)).pack(pady=10)
        
        ctk.CTkLabel(self.content_frame, text="Enter Video Name/Topic:", font=("Roboto", 14)).pack(pady=5)
        
        self.youtube_name = ctk.CTkEntry(self.content_frame, width=400, font=("Roboto", 16))
        self.youtube_name.pack(pady=10)
        self.youtube_name.bind("<Return>", lambda e: self.search())
        
        ctk.CTkButton(self.content_frame, text="Search on YouTube", command=self.search, width=200).pack(pady=10)
        
        self.status_label = ctk.CTkLabel(self.content_frame, text="")
        self.status_label.pack(pady=5)
        
        self.add_back_button()

    def search(self):
        video_name = self.youtube_name.get().strip()
        if not video_name:
            self.status_label.configure(text="Please enter a video name", text_color="red")
            return
            
        try:
            search_url = f"https://www.youtube.com/results?search_query={video_name}"
            self.status_label.configure(text=f"Opening search for: {video_name}", text_color="green")
            tts_service.speak(f"Searching for {video_name} on YouTube")
            webbrowser.open(search_url)
        except Exception as e:
             self.status_label.configure(text=f"Error: {e}", text_color="red")