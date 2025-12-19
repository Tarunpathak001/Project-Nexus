import customtkinter as ctk
import tkinter as tk
from .modern_base_frame import ModernBaseFrame
import random
from ...core.logger import logger

class SnakeGameFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "snake.png")
        
        self.label = ctk.CTkLabel(self.content_frame, text="🐍 Dual Player Snake Game", font=("Roboto Medium", 24))
        self.label.pack(pady=10)
        
        # Game Board
        # Using tk.Canvas because drawing primitives are robust there
        self.canvas_bg = "#2b2b2b"
        self.canvas = tk.Canvas(self.content_frame, width=400, height=400, bg=self.canvas_bg, highlightthickness=0)
        self.canvas.pack(pady=10)
        
        # Controls Info
        info_label = ctk.CTkLabel(self.content_frame, text="P1 (Green): Arrows | P2 (Blue): WASD", font=("Roboto", 12))
        info_label.pack(pady=5)
        
        self.restart_button = ctk.CTkButton(self.content_frame, text="Start / Restart", command=self.restart)
        self.restart_button.pack(pady=10)
        
        self.add_back_button()
        
        # State
        self.game_over = True
        self.snake1 = []
        self.snake2 = []
        self.setup_game()
        
        # Bindings
        # We need to ensure unit has focus to receive keys.
        self.canvas.bind("<Enter>", lambda e: self.canvas.focus_set())
        # Bind to the toplevel window or specific widget? Better to bind to controller root if possible, 
        # but let's try binding to the frame event.
        # Actually in the original code, it bound to 'all'. We can try binding to the main application window.
        self.controller.bind("<KeyPress>", self.change_direction)

    def setup_game(self):
        self.snake1 = [(200, 200), (190, 200), (180, 200)] 
        self.direction1 = 'Right'
        self.score1 = 0
        
        self.snake2 = [(100, 100), (110, 100), (120, 100)]
        self.direction2 = 'Left'
        self.score2 = 0
        
        self.food = self.generate_food()
        self.game_over = False

    def generate_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return (x, y)

    def update_game(self):
        if self.game_over:
            self.canvas.create_text(200, 200, text='Game Over!', font=('Arial', 24), fill='red')
            return
        
        if not self.winfo_viewable():
            return # Pause if we navigated away

        self.canvas.delete('all')
        
        # Draw Sn 1
        for x, y in self.snake1:
            self.canvas.create_rectangle(x, y, x+10, y+10, fill='#00ff00', outline="") # Bright Green
            
        # Draw Sn 2
        for x, y in self.snake2:
            self.canvas.create_rectangle(x, y, x+10, y+10, fill='#00ccff', outline="") # Bright Blue
            
        # Draw Food
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0]+10, self.food[1]+10, fill='#ff0000', outline="")
        
        # Scores
        self.canvas.create_text(10, 10, anchor='nw', text=f'P1: {self.score1}', font=('Arial', 12), fill='#00ff00')
        self.canvas.create_text(390, 10, anchor='ne', text=f'P2: {self.score2}', font=('Arial', 12), fill='#00ccff')
        
        self.move_snake()
        self.check_collision()
        
        if not self.game_over:
            self.after(100, self.update_game)

    def move_snake(self):
        # Snake 1
        head_x1, head_y1 = self.snake1[0]
        if self.direction1 == 'Right': new_head1 = (head_x1 + 10, head_y1)
        elif self.direction1 == 'Left': new_head1 = (head_x1 - 10, head_y1)
        elif self.direction1 == 'Up': new_head1 = (head_x1, head_y1 - 10)
        elif self.direction1 == 'Down': new_head1 = (head_x1, head_y1 + 10)
        else: new_head1 = (head_x1, head_y1) # Should not happen

        self.snake1.insert(0, new_head1)
        if self.snake1[0] == self.food:
            self.score1 += 1
            self.food = self.generate_food()
        else:
            self.snake1.pop()

        # Snake 2
        head_x2, head_y2 = self.snake2[0]
        if self.direction2 == 'Right': new_head2 = (head_x2 + 10, head_y2)
        elif self.direction2 == 'Left': new_head2 = (head_x2 - 10, head_y2)
        elif self.direction2 == 'Up': new_head2 = (head_x2, head_y2 - 10)
        elif self.direction2 == 'Down': new_head2 = (head_x2, head_y2 + 10)
        else: new_head2 = (head_x2, head_y2)

        self.snake2.insert(0, new_head2)
        if self.snake2[0] == self.food:
            self.score2 += 1
            self.food = self.generate_food()
        else:
            self.snake2.pop()

    def check_collision(self):
        head_x1, head_y1 = self.snake1[0]
        head_x2, head_y2 = self.snake2[0]
        
        # Wall Collision
        if head_x1 < 0 or head_x1 >= 400 or head_y1 < 0 or head_y1 >= 400: self.game_over = True
        if head_x2 < 0 or head_x2 >= 400 or head_y2 < 0 or head_y2 >= 400: self.game_over = True
        
        # Self Collision
        if self.snake1[0] in self.snake1[1:]: self.game_over = True
        if self.snake2[0] in self.snake2[1:]: self.game_over = True

    def change_direction(self, event):
        # P1
        if event.keysym == 'Up' and self.direction1 != 'Down': self.direction1 = 'Up'
        elif event.keysym == 'Down' and self.direction1 != 'Up': self.direction1 = 'Down'
        elif event.keysym == 'Left' and self.direction1 != 'Right': self.direction1 = 'Left'
        elif event.keysym == 'Right' and self.direction1 != 'Left': self.direction1 = 'Right'
        
        # P2
        if event.keysym == 'w' and self.direction2 != 'Down': self.direction2 = 'Up'
        elif event.keysym == 's' and self.direction2 != 'Up': self.direction2 = 'Down'
        elif event.keysym == 'a' and self.direction2 != 'Right': self.direction2 = 'Left'
        elif event.keysym == 'd' and self.direction2 != 'Left': self.direction2 = 'Right'

    def restart(self):
        self.setup_game()
        self.canvas.focus_set()
        self.update_game()