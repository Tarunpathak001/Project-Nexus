import customtkinter as ctk
from .modern_base_frame import ModernBaseFrame
from ...core.database import db
from ...core.text_to_speech import tts_service
from ...core.logger import logger

class ExpenseTrackerFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "expense.png")
        
        self.label = ctk.CTkLabel(self.content_frame, text="💰 Expense Tracker", font=("Roboto Medium", 24))
        self.label.pack(pady=10)
        
        input_frame = ctk.CTkFrame(self.content_frame)
        input_frame.pack(pady=10, padx=20, fill="x")
        
        self.desc_entry = ctk.CTkEntry(input_frame, placeholder_text="Description (e.g. Lunch)", width=200)
        self.desc_entry.pack(side="left", padx=5, pady=10)
        
        self.amount_entry = ctk.CTkEntry(input_frame, placeholder_text="Amount ($$)", width=100)
        self.amount_entry.pack(side="left", padx=5, pady=10)
        
        ctk.CTkButton(input_frame, text="Add", width=80, command=self.add_expense).pack(side="left", padx=5)

        self.total_label = ctk.CTkLabel(self.content_frame, text="Total: Rs 0.00", font=("Roboto Medium", 18))
        self.total_label.pack(pady=5)

        self.expenses_container = ctk.CTkScrollableFrame(self.content_frame, width=500, height=350, label_text="History")
        self.expenses_container.pack(pady=10, fill="both", expand=True)

        self.load_expenses()
        self.add_back_button()

    def load_expenses(self):
        for widget in self.expenses_container.winfo_children():
            widget.destroy()
            
        expenses = db.fetch_all("SELECT * FROM expenses ORDER BY date DESC")
        
        total = 0
        for exp in expenses:
            self.create_expense_widget(exp)
            total += exp['amount']
            
        self.total_label.configure(text=f"Total: Rs {total:.2f}")

    def create_expense_widget(self, expense):
        exp_id = expense['id']
        desc = expense['description']
        amount = expense['amount']
        date = expense['date']

        row_frame = ctk.CTkFrame(self.expenses_container)
        row_frame.pack(fill="x", pady=2, padx=5)
        
        ctk.CTkLabel(row_frame, text=desc, width=200, anchor="w").pack(side="left", padx=10)
        ctk.CTkLabel(row_frame, text=f"Rs {amount:.2f}", width=100, anchor="e").pack(side="left", padx=10)
        
        ctk.CTkButton(
            row_frame, 
            text="✖", 
            width=30, 
            fg_color="transparent", 
            text_color="red", 
            hover_color="#330000",
            command=lambda: self.delete_expense(exp_id)
        ).pack(side="right", padx=5, pady=5)

    def add_expense(self):
        desc = self.desc_entry.get().strip()
        amount_str = self.amount_entry.get().strip()
        
        if desc and amount_str:
            try:
                amount = float(amount_str)
                db.execute_query("INSERT INTO expenses (description, amount) VALUES (?, ?)", (desc, amount))
                self.desc_entry.delete(0, 'end')
                self.amount_entry.delete(0, 'end')
                tts_service.speak("Expense Added")
                self.load_expenses()
            except ValueError:
                tts_service.speak("Invalid mount")
        else:
            tts_service.speak("Enter details")

    def delete_expense(self, exp_id):
        db.execute_query("DELETE FROM expenses WHERE id = ?", (exp_id,))
        self.load_expenses()