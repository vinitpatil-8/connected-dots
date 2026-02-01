import customtkinter as ctk

class DotsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        

        h1 = ctk.CTkLabel(self, text="Connect The Dots", font=("Arial", 32, "bold"))
        h2 = ctk.CTkLabel(self, text="Select A Grid Size", font=("Arial", 16))
        h1.pack(pady=(15, 2))
        h2.pack(pady=(2, 20))

        def back():
            controller.show_page("menu")
            
        bottom_bar = ctk.CTkFrame(self, height=25)
        bottom_bar.pack(side="bottom", fill="x")

        btn1 = ctk.CTkButton(bottom_bar, width=20, font=("Roboto", 16, "bold"), text="Back", fg_color="black", hover_color="grey",text_color="white", command=back)
        btn1.pack(side="left", padx=15, pady=(40,10))