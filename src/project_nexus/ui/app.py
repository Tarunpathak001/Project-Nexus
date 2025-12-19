import customtkinter as ctk
import tkinter as tk
from ..config import Config
from ..core.text_to_speech import tts_service
from ..core.logger import logger
from .frames.snake_game_frame import SnakeGameFrame
from .frames.typing_speed_frame import TypingSpeedFrame
from .frames.dashboard import DashboardFrame

from .frames.encrypt_decrypt_frame import EncryptDecryptFrame
from .frames.settings_frame import SettingsFrame
from .frames.weather_frame import WeatherFrame
from .frames.calculator_frame import CalculatorFrame
from .frames.notes_frame import NotesFrame
from .frames.expense_tracker_frame import ExpenseTrackerFrame
from .frames.todo_frame import ToDoFrame
from .frames.youtube_frame import YoutubeFrame
from .frames.sticky_notes_frame import StickyNotesFrame
from .frames.random_number_frame import RandomNumberFrame
from .frames.password_generator_frame import PasswordGeneratorFrame
from .frames.stopwatch_frame import StopWatchFrame
from .frames.translator_frame import TranslatorFrame
from .frames.speech_to_text_frame import SpeechToTextFrame
from .frames.text_to_speech_frame import TextToSpeechFrame

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class ProjectNexusApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PROJECT NEXUS - AI Dashboard")
        self.geometry("1600x900")
        
        logger.info("Starting Project Nexus...")
        
        # Main container
        self.container = ctk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        # Initialize frames
        frame_classes = (
            DashboardFrame,
            ToDoFrame,
            NotesFrame,
            ExpenseTrackerFrame,
            EncryptDecryptFrame,
            WeatherFrame,
            CalculatorFrame,
            SettingsFrame,
            SnakeGameFrame,
            TypingSpeedFrame,
            YoutubeFrame,
            StickyNotesFrame,
            RandomNumberFrame,
            PasswordGeneratorFrame,
            StopWatchFrame,
            TranslatorFrame,
            SpeechToTextFrame,
            TextToSpeechFrame,
        ) 
        
        for F in frame_classes:
            frame_name = F.__name__
            try:
                frame = F(parent=self.container, controller=self)
                self.frames[frame_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")
            except Exception as e:
                logger.error(f"Failed to load frame {frame_name}: {e}")
            
        self.show_frame("DashboardFrame", "Welcome to Project Nexus")

    def show_frame(self, frame_name, speech_text=""):
        frame = self.frames.get(frame_name)
        if frame:
            if speech_text:
                tts_service.speak(speech_text)
            frame.tkraise()
            logger.info(f"Switched to frame: {frame_name}")
        else:
            logger.warning(f"Frame {frame_name} not found.")

    def add_frame(self, frame_class, frame_name):
         frame = frame_class(parent=self.container, controller=self)
         self.frames[frame_name] = frame
         frame.grid(row=0, column=0, sticky="nsew")
