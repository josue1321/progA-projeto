from tkinter import Tk, Canvas, Frame, StringVar, ttk, W

class AppDesenhoView:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Desenho")

        # Chama a função que constrói a tela
        self.configurar_interface()

    def configurar_interface(self):
        self.frame = Frame(self.root)
        self.frame.pack()
        paddings = {"padx": 5, "pady": 5}

        ttk.Label(self.frame, text="Figura:").grid(
            column=0, row=0, sticky=W, **paddings
        )
        self.tipo_figura_var = StringVar(self.root)

        # Cria o menu para escolher a figura
        ttk.OptionMenu(
            self.frame,
            self.tipo_figura_var,
            "linha",
            "linha",
            "rabisco",
            "circulo",
            "retangulo",
            "oval",
            "poligono",
        ).grid(column=1, row=0, sticky=W, **paddings)

        # Cria o menu para selecionar a cor da borda
        ttk.Label(self.frame, text="Cor da Borda:").grid(
            column=0, row=1, sticky=W, **paddings
        )
        self.cor_lapis_var = StringVar(self.root)
        ttk.OptionMenu(
            self.frame, self.cor_lapis_var, "black", "black", "red", "blue"
        ).grid(column=1, row=1, sticky=W, **paddings)

        # Cria o menu de seleção da cor do preenchimento
        ttk.Label(self.frame, text="Cor para preencher:").grid(
            column=0, row=2, sticky=W, **paddings
        )
        self.cor_preenchimento_var = StringVar(self.root)
        ttk.OptionMenu(
            self.frame,
            self.cor_preenchimento_var,
            "white",
            "white",
            "black",
            "red",
            "blue",
        ).grid(column=1, row=2, sticky=W, **paddings)

        frame_botoes = Frame(self.frame)
        frame_botoes.grid(column=0, row=3, columnspan=2, sticky=W, **paddings)

        self.btn_salvar = ttk.Button(frame_botoes, text="Salvar Desenho")
        self.btn_salvar.pack(side="left", padx=5)

        self.btn_abrir = ttk.Button(frame_botoes, text="Abrir Desenho")
        self.btn_abrir.pack(side="left", padx=5)

        self.canvas = Canvas(self.frame, bg="white", width=600, height=600)
        self.canvas.grid(column=0, row=4, columnspan=2, sticky=W, **paddings)
