import customtkinter as ctk
from .modern_base_frame import ModernBaseFrame
from ...core.database import db
from ...core.text_to_speech import tts_service
from ...core.logger import logger

class NotesFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "notes.png")
        
        self.label = ctk.CTkLabel(self.content_frame, text="📓 Quick Notes", font=("Roboto Medium", 24))
        self.label.pack(pady=10)
        
        self.note_text = ctk.CTkTextbox(self.content_frame, width=400, height=100)
        self.note_text.pack(pady=10)
        
        btn_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        btn_frame.pack(pady=5)
        
        ctk.CTkButton(btn_frame, text="Save Note", command=self.save_note).pack(side="left", padx=5)
        
        self.notes_container = ctk.CTkScrollableFrame(self.content_frame, width=450, height=300, label_text="My Notes")
        self.notes_container.pack(pady=10, fill="both", expand=True)

        self.load_notes()
        self.add_back_button()

    def load_notes(self):
        for widget in self.notes_container.winfo_children():
            widget.destroy()
            
        notes = db.fetch_all("SELECT * FROM notes ORDER BY created_at DESC")
        
        if not notes:
            ctk.CTkLabel(self.notes_container, text="No notes saved.").pack(pady=20)
            return

        for note in notes:
            self.create_note_widget(note)

    def create_note_widget(self, note):
        note_id = note['id']
        content = note['content']
        timestamp = note['created_at']

        row_frame = ctk.CTkFrame(self.notes_container)
        row_frame.pack(fill="x", pady=5, padx=5)
        
        display_text = content[:50] + "..." if len(content) > 50 else content
        ctk.CTkLabel(row_frame, text=display_text, anchor="w", justify="left").pack(side="left", padx=10, fill="x", expand=True)
        
        ctk.CTkButton(
            row_frame, 
            text="🗑️", 
            width=30, 
            fg_color="transparent", 
            text_color="red", 
            hover_color="#330000",
            command=lambda: self.delete_note(note_id)
        ).pack(side="right", padx=5, pady=5)

    def save_note(self):
        content = self.note_text.get("1.0", "end").strip()
        if content:
            db.execute_query("INSERT INTO notes (content) VALUES (?)", (content,))
            self.note_text.delete("1.0", "end")
            tts_service.speak("Note saved")
            self.load_notes()
        else:
            tts_service.speak("Please write something first")

    def delete_note(self, note_id):
        db.execute_query("DELETE FROM notes WHERE id = ?", (note_id,))
        tts_service.speak("Note Deleted")
        self.load_notes()