import customtkinter as ctk
from .modern_base_frame import ModernBaseFrame
from ...core.database import db
from ...core.text_to_speech import tts_service
from ...core.logger import logger

class ToDoFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "todo.png")
        
        self.label = ctk.CTkLabel(self.content_frame, text="✅ To-Do List", font=("Roboto Medium", 24))
        self.label.pack(pady=10)
        
        input_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        input_frame.pack(pady=10, fill="x")
        
        self.task_entry = ctk.CTkEntry(input_frame, placeholder_text="Enter new task...", width=300)
        self.task_entry.pack(side="left", padx=10)
        self.task_entry.bind("<Return>", lambda event: self.add_task())
        
        add_btn = ctk.CTkButton(input_frame, text="Add", width=80, command=self.add_task)
        add_btn.pack(side="left")
        
        self.tasks_container = ctk.CTkScrollableFrame(self.content_frame, width=450, height=400, label_text="My Tasks")
        self.tasks_container.pack(pady=10, fill="both", expand=True)
        
        self.load_tasks()

        self.add_back_button()

    def load_tasks(self):
        for widget in self.tasks_container.winfo_children():
            widget.destroy()
            
        tasks = db.fetch_all("SELECT * FROM tasks ORDER BY status ASC, created_at DESC")
        
        if not tasks:
            ctk.CTkLabel(self.tasks_container, text="No tasks yet!").pack(pady=20)
            return

        for task in tasks:
            self.create_task_widget(task)

    def create_task_widget(self, task):
        task_id = task['id']
        title = task['title']
        status = task['status']
        
        row_frame = ctk.CTkFrame(self.tasks_container)
        row_frame.pack(fill="x", pady=2, padx=5)
        
        is_done = status == 'Done'
        
        text_color = "gray" if is_done else "white"
        
        check_var = ctk.BooleanVar(value=is_done)
        checkbox = ctk.CTkCheckBox(
            row_frame, 
            text=title, 
            variable=check_var, 
            text_color=text_color,
            command=lambda: self.toggle_task(task_id, check_var.get())
        )
        checkbox.pack(side="left", padx=10, pady=10)
        
        del_btn = ctk.CTkButton(
            row_frame, 
            text="🗑️", 
            width=30, 
            fg_color="transparent", 
            text_color="red", 
            hover_color="#330000",
            command=lambda: self.delete_task(task_id)
        )
        del_btn.pack(side="right", padx=5)

    def add_task(self):
        title = self.task_entry.get().strip()
        if title:
            db.execute_query("INSERT INTO tasks (title) VALUES (?)", (title,))
            self.task_entry.delete(0, 'end')
            tts_service.speak("Task Added")
            self.load_tasks()
        else:
            tts_service.speak("Please enter a task")

    def toggle_task(self, task_id, is_checked):
        new_status = 'Done' if is_checked else 'Pending'
        db.execute_query("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
        if is_checked: tts_service.speak("Task Completed")
        self.load_tasks()

    def delete_task(self, task_id):
        db.execute_query("DELETE FROM tasks WHERE id = ?", (task_id,))
        tts_service.speak("Task Deleted")
        self.load_tasks()