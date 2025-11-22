# dashboard.py
from tkinter import *
from menu import create_menu_page
from compra import create_compra_page

class Dashboard(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema com Menu e Comanda")
        self.geometry("1000x700")
        self.configure(bg="#1A1512")
        self.sidebar_expand = True

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # sidebar
        self.sidebar = Frame(self, bg="#1A1512", width=220)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # toggle
        self.toggle_btn = Button(self.sidebar, text="X", bg="#1A1512", fg="#F4D465",
                                 font=("Georgia", 16), relief="flat", command=self.toggle_sidebar)
        self.toggle_btn.pack(pady=12, padx=12, fill="x")

        # menu buttons
        Button(self.sidebar, text="Menu", bg="#2A2218", fg="#F4D465", font=("Georgia", 14),
               relief="flat", command=self.open_menu).pack(fill="x", padx=12, pady=6)
        Button(self.sidebar, text="Perfil", bg="#2A2218", fg="#F4D465", font=("Georgia", 14),
               relief="flat", command=lambda: self.update_content("Perfil")).pack(fill="x", padx=12, pady=6)
        Button(self.sidebar, text="Reserva", bg="#2A2218", fg="#F4D465", font=("Georgia", 14),
               relief="flat", command=lambda: self.update_content("Reserva")).pack(fill="x", padx=12, pady=6)
        Button(self.sidebar, text="Compra (Comanda)", bg="#2A2218", fg="#F4D465", font=("Georgia", 14),
               relief="flat", command=self.open_compra).pack(fill="x", padx=12, pady=6)

        # content area
        self.content = Frame(self, bg="#1A1512")
        self.content.grid(row=0, column=1, sticky="nsew")

        # inicial
        self.update_content("Bem-vindo! Use o Menu para adicionar itens.")

    def open_menu(self):
        create_menu_page(self.content)

    def open_compra(self):
        create_compra_page(self.content)

    def update_content(self, text):
        for w in self.content.winfo_children():
            w.destroy()
        Label(self.content, text=text, font=("Georgia", 20), fg="white", bg="#1A1512").pack(expand=True)

    def toggle_sidebar(self):
        if self.sidebar_expand:
            self.sidebar.config(width=60)
            self.sidebar_expand = False
            self.toggle_btn.config(text="☰", font=("Georgia", 12))
        else:
            self.sidebar.config(width=220)
            self.sidebar_expand = True
            self.toggle_btn.config(text="X", font=("Georgia", 16))

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
