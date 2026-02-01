import customtkinter as ctk
from menu import MenuPage
from dots import DotsPage
from sudoku import SudokuPage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Connected-Dots")
        self.geometry("600x500")
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        self.resizable(False, False)

        self.pages = {}

        self._create_pages()
        self.show_page("menu")

    def _create_pages(self):
        self.pages["menu"] = MenuPage(self.container, self)
        self.pages["dots"] = DotsPage(self.container, self)
        self.pages["sudoku"] = SudokuPage(self.container, self)

        for page in self.pages.values():
            page.place(relwidth=1, relheight=1)

    def show_page(self, name):
        self.pages[name].tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()