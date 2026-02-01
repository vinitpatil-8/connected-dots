import customtkinter as ctk

class MenuPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        def show_toast():
            toast = ctk.CTkToplevel(self)
            toast.overrideredirect(True)  # no title bar
            toast.geometry("250x80+20+220")

            label = ctk.CTkLabel(
                toast,
                text="Coming Soon....",
                font=ctk.CTkFont(size=14)
            )
            label.pack(expand=True, padx=20, pady=20)

            toast.after(3000, toast.destroy)

            # need to fix the toast

        def soon():
            show_toast()
        def connect():
            controller.show_page("dots")
        def soduko():
            controller.show_page("sudoku")

        h1 = ctk.CTkLabel(self, text="Connected-Dots", font=("Arial", 32, "bold"))
        h2 = ctk.CTkLabel(self, text="Vision Based Puzzle Solver", font=("Arial", 16))
        h3 = ctk.CTkLabel(self, text="Menu",text_color="#E6E6FA", font=("Roboto", 28, "bold"))
        h1.pack(pady=(15, 2))
        h2.pack(pady=(2, 20))
        h3.pack(pady=(20, 5))

        btn1 = ctk.CTkButton(self, height=50, width=180, font=("Roboto", 16, "bold"), text="Connect The Dots", fg_color="black", hover_color="grey",text_color="white", command=connect)
        btn2 = ctk.CTkButton(self, height=50, width=180, font=("Roboto", 16, "bold"), text="Soduko", fg_color="black", hover_color="grey",text_color="white", command=soduko)
        btn3 = ctk.CTkButton(self, height=50, width=180, font=("Roboto", 16, "bold"), text="Coming Soon...", fg_color="black", hover_color="grey",text_color="white", command=soon)


        btn1.pack(padx=25, pady=(40,10))
        btn2.pack(padx=25, pady=10)
        btn3.pack(padx=25, pady=10)


        







