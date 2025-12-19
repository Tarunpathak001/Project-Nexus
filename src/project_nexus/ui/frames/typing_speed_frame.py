import customtkinter as ctk
import tkinter as tk
from .modern_base_frame import ModernBaseFrame
from ...core.text_to_speech import tts_service
import random
import time

class TypingSpeedFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "typing.png")
        
        self.sample_sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a powerful programming language.",
            "Artificial intelligence is the future of technology.",
            "Speed typing is a fun and educational challenge.",
            "The early bird catches the worm.",
            "She sells sea shells in the sea shore.",
            "Project Nexus is the multi functionality stop you always dreamed off."
        ]
        
        # State
        self.start_time = None
        self.current_sentence = ""
        self.is_game_over = False
        
        # UI
        ctk.CTkLabel(self.content_frame, text="⌨️ Typing Challenge", font=("Roboto Medium", 24)).pack(pady=10)
        
        self.sentence_label = ctk.CTkLabel(self.content_frame, text="Press Start...", font=("Roboto", 18), wraplength=500)
        self.sentence_label.pack(pady=20)
        
        self.user_input = ctk.CTkTextbox(self.content_frame, height=100, width=500, font=("Roboto", 16))
        self.user_input.pack(pady=10)
        self.user_input.bind("<KeyRelease>", self.track_typing)
        
        self.feedback_label = ctk.CTkLabel(self.content_frame, text="", font=("Roboto", 14), text_color="yellow")
        self.feedback_label.pack(pady=5)
        
        # Stats
        stats_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        stats_frame.pack(pady=10)
        
        self.time_label = ctk.CTkLabel(stats_frame, text="Time: 0s", font=("Roboto", 14))
        self.time_label.pack(side="left", padx=15)
        
        self.wpm_label = ctk.CTkLabel(stats_frame, text="WPM: 0", font=("Roboto", 14))
        self.wpm_label.pack(side="left", padx=15)
        
        self.accuracy_label = ctk.CTkLabel(stats_frame, text="Acc: 0%", font=("Roboto", 14))
        self.accuracy_label.pack(side="left", padx=15)
        
        # Buttons
        btn_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        btn_frame.pack(pady=10)
        
        self.start_button = ctk.CTkButton(btn_frame, text="Start Game", command=self.start_game)
        self.start_button.pack(side="left", padx=10)
        
        self.check_button = ctk.CTkButton(btn_frame, text="Check", command=self.check_speed, state="disabled")
        self.check_button.pack(side="left", padx=10)
        
        self.restart_button = ctk.CTkButton(btn_frame, text="Restart", command=self.restart_game, state="disabled")
        self.restart_button.pack(side="left", padx=10)
        
        self.add_back_button()

    def update_timer(self):
        if not self.is_game_over and self.winfo_viewable() and self.start_time:
            elapsed_time = int(time.time() - self.start_time)
            self.time_label.configure(text=f"Time: {elapsed_time}s")
            self.after(1000, self.update_timer)

    def start_game(self):
        self.is_game_over = False
        self.user_input.delete("1.0", "end")
        self.current_sentence = random.choice(self.sample_sentences)
        self.sentence_label.configure(text=self.current_sentence)
        self.feedback_label.configure(text="Go!")
        
        self.start_time = time.time()
        self.update_timer()
        
        self.start_button.configure(state="disabled")
        self.check_button.configure(state="normal")
        self.restart_button.configure(state="disabled")
        
        tts_service.speak("Start typing!")

    def track_typing(self, event):
        if self.start_time and not self.is_game_over:
            typed_text = self.user_input.get("1.0", "end").strip()
            if typed_text:
                elapsed_time = time.time() - self.start_time
                current_wpm = (len(typed_text.split()) / elapsed_time) * 60 if elapsed_time > 0 else 0
                self.wpm_label.configure(text=f"WPM: {current_wpm:.0f}")

    def check_speed(self):
        typed_text = self.user_input.get("1.0", "end").strip()
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        
        words = typed_text.split()
        total_words = len(words)
        
        typing_speed = (total_words / elapsed_time) * 60 if elapsed_time > 0 else 0
        
        target_words = self.current_sentence.split()
        correct_words = sum(1 for t, c in zip(words, target_words) if t == c)
        accuracy = (correct_words / max(len(target_words), 1)) * 100
        
        self.accuracy_label.configure(text=f"Acc: {accuracy:.1f}%")
        self.wpm_label.configure(text=f"WPM: {typing_speed:.1f}")
        
        if typed_text == self.current_sentence:
            self.feedback_label.configure(text="Perfect!", text_color="green")
            tts_service.speak(f"Perfect! Accuracy {accuracy:.1f} percent")
        else:
            self.feedback_label.configure(text="Done!", text_color="white")
            tts_service.speak(f"Done. Accuracy {accuracy:.1f} percent")
            
        self.is_game_over = True
        self.check_button.configure(state="disabled")
        self.restart_button.configure(state="normal")

    def restart_game(self):
        self.start_button.configure(state="normal")
        self.check_button.configure(state="disabled")
        self.restart_button.configure(state="disabled")
        
        self.sentence_label.configure(text="Press Start...")
        self.feedback_label.configure(text="")
        self.user_input.delete("1.0", "end")
        
        self.time_label.configure(text="Time: 0s")
        self.wpm_label.configure(text="WPM: 0")
        self.accuracy_label.configure(text="Acc: 0%")
        self.start_time = None