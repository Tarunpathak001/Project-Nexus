import customtkinter as ctk
import time
from .modern_base_frame import ModernBaseFrame

class StopWatchFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "watch.png")
        
        self.running = False
        self.counter = 0
        self.laps = []
        
        ctk.CTkLabel(self.content_frame, text="⏱️ Stopwatch", font=("Roboto Medium", 24)).pack(pady=10)
        
        self.time_display_label = ctk.CTkLabel(self.content_frame, text="00:00:00", font=("Roboto Medium", 48))
        self.time_display_label.pack(pady=20)
        
        button_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        button_frame.pack(pady=10)
        
        ctk.CTkButton(button_frame, text="Start", command=self.start_stopwatch, width=80).grid(row=0, column=0, padx=5)
        ctk.CTkButton(button_frame, text="Stop", command=self.stop_stopwatch, width=80, fg_color="red", hover_color="darkred").grid(row=0, column=1, padx=5)
        ctk.CTkButton(button_frame, text="Reset", command=self.reset_stopwatch, width=80).grid(row=0, column=2, padx=5)
        ctk.CTkButton(button_frame, text="Lap", command=self.lap_stopwatch, width=80).grid(row=0, column=3, padx=5)
        
        self.laps_container = ctk.CTkScrollableFrame(self.content_frame, width=300, height=150, label_text="Laps")
        self.laps_container.pack(pady=10)
        
        self.add_back_button()

    def update_display(self):
        minutes, seconds = divmod(self.counter, 60)
        hours, minutes = divmod(minutes, 60)
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        self.time_display_label.configure(text=time_str)

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.run_timer()

    def run_timer(self):
        if self.running and self.winfo_viewable():
            self.counter += 1
            self.update_display()
            self.after(1000, self.run_timer) 

    def stop_stopwatch(self):
        self.running = False

    def reset_stopwatch(self):
        self.running = False
        self.counter = 0
        self.laps = []
        self.update_display()
        for widget in self.laps_container.winfo_children():
            widget.destroy()

    def lap_stopwatch(self):
        if self.running:
            minutes, seconds = divmod(self.counter, 60)
            hours, minutes = divmod(minutes, 60)
            lap_time = f"Lap {len(self.laps)+1}: {hours:02}:{minutes:02}:{seconds:02}"
            self.laps.append(lap_time)
            ctk.CTkLabel(self.laps_container, text=lap_time).pack()