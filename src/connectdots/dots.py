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
        def six():
            controller.show_page("six")
        def seven():
            controller.show_page("seven")
        def eight():
            controller.show_page("eight")

        btn1 = ctk.CTkButton(self, height=50, width=180, font=("Roboto", 16, "bold"), text="6x6", fg_color="black", hover_color="grey",text_color="white", command=six)
        btn2 = ctk.CTkButton(self, height=50, width=180, font=("Roboto", 16, "bold"), text="7x7", fg_color="black", hover_color="grey",text_color="white", command=seven)
        btn3 = ctk.CTkButton(self, height=50, width=180, font=("Roboto", 16, "bold"), text="8x8", fg_color="black", hover_color="grey",text_color="white", command=eight)


        btn1.pack(padx=25, pady=(40,10))
        btn2.pack(padx=25, pady=10)
        btn3.pack(padx=25, pady=10)
            
        bottom_bar = ctk.CTkFrame(self, height=25)
        bottom_bar.pack(side="bottom", fill="x")

        btnback = ctk.CTkButton(bottom_bar, width=20, font=("Roboto", 16, "bold"), text="Back", fg_color="black", hover_color="grey",text_color="white", command=back)
        btnback.pack(side="left", padx=15, pady=(40,10))