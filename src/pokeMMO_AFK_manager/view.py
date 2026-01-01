import tkinter as tk
from tkinter import ttk

class AppView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PokeMMO AFK Manager")
        self.geometry("640x480")

        self.style = ttk.Style(self)
        self._configure_styles()

        self.setup_ui()
    
    def _configure_styles(self):
        self.style.theme_use('alt')

        self.style.configure("Main.TFrame", background="#2C3E50")

        self.style.configure("Header.TLabel", 
                             font=("Helvetica", 18, "bold"), 
                             foreground="#fff", 
                             background="#2C3E50")

        self.style.configure("Action.TButton", 
                             font=("Helvetica", 10, "bold"), 
                             foreground="#F5F5DC", 
                             background="#000",
                             padding=10)
        
        self.style.map("Action.TButton",
                       background=[('active', '#E6E6C3')],
                       foreground=[('active', '#000')])

    def setup_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        container = ttk.Frame(self, style="Main.TFrame", padding="10")
        container.grid(row=0, column=0, sticky="nsew")
        
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=0)
        container.rowconfigure(1, weight=1)

        self.label = ttk.Label(container, text="PokeMMO AFK Farm", style="Header.TLabel")
        self.label.grid(row=0, column=0, pady=10, sticky="n")

        controls_frame = ttk.Frame(container, style="Main.TFrame")
        controls_frame.grid(row=1, column=0, pady=40)
        controls_frame.columnconfigure(0, weight=1)

        self.btn_accion = ttk.Button(controls_frame, text="Iniciar Script", style="Action.TButton", command=self.on_button_click, width=40)
        self.btn_accion.grid(row=0, column=0, pady=15)
        
        self.btn_salir = ttk.Button(controls_frame, text="Configuración", style="Action.TButton", command=self.on_button_click, width=40)
        self.btn_salir.grid(row=1, column=0, pady=15)

    def on_button_click(self):
        print("Evento capturado: Botón presionado")

    def run(self):
        self.mainloop()