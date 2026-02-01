import customtkinter as ctk

class SolutionPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        h1 = ctk.CTkLabel(self, text="Solved Image", font=("Arial", 32, "bold"))
        h1.pack(pady=(15, 2))