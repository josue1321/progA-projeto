# Importa as ferramentas gráficas do Tkinter
from tkinter import Tk, Canvas, Frame, StringVar, ttk, W

# Importa as classes de desenho do arquivo figuras.py
from figuras import Linha, Rabisco, Retangulo, Oval, Circulo, Poligono


# Classe principal que controla o programa
class AppDesenho:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Desenho")

        self.figuras = []
        self.figura_nova = None
        self.pontos_poligono_atual = []
        self.ferramenta_atual = ""

        self.configurar_interface()
        self.vincular_eventos()

    # Função que cria os botões, menus de cores e a área branca de desenho
    def configurar_interface(self):
        self.frame = Frame(self.root)
        self.frame.pack()
        paddings = {"padx": 5, "pady": 5}

        ttk.Label(self.frame, text="Figura:").grid(
            column=0, row=0, sticky=W, **paddings
        )
        self.tipo_figura_var = StringVar(self.root)

        # Cria o menu para escolher a figura
        option_menu = ttk.OptionMenu(
            self.frame,
            self.tipo_figura_var,
            "linha",
            "linha",
            "rabisco",
            "circulo",
            "retangulo",
            "oval",
            "poligono",
        )
        option_menu.grid(column=1, row=0, sticky=W, **paddings)

        # Cria o menu para selecionr a cor da borda
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

        # Cria o quadro branco que os desenhos serão feitos
        self.canvas = Canvas(self.frame, bg="white", width=600, height=600)
        self.canvas.grid(column=0, row=3, columnspan=2, sticky=W, **paddings)

    # Função que liga os cliques do mouse às funções do código
    def vincular_eventos(self):

        self.canvas.bind("<ButtonPress-1>", self.tratar_clique)
        self.canvas.bind("<B1-Motion>", self.tratar_arrasto)
        self.canvas.bind("<ButtonRelease-1>", self.tratar_soltar)
        self.canvas.bind("<Double-Button-1>", self.finalizar_poligono)
        self.canvas.bind("<ButtonPress-3>", self.reset)

    # Função que roda assim que o usuário clica no Canvas
    def tratar_clique(self, event):
        # Pega o que está selecionado nos menus do Tkinter
        tipo = self.tipo_figura_var.get()
        cor_borda = self.cor_lapis_var.get()
        cor_preench_ = self.cor_preenchimento_var.get()
        self.ferramenta_atual = tipo

        # Implementa a lógica do polígono, ele funciona unindo cliques em locais diferentes da forma, tratando esses pontos como vértices
        if tipo == "poligono":
            self.pontos_poligono_atual.append((event.x, event.y))
            self.figura_nova = Poligono(
                list(self.pontos_poligono_atual), cor_borda, cor_preench_
            )
            self.desenhar_figuras()
            self.figura_nova.desenhar_nova(self.canvas)
        else:
            self.pontos_poligono_atual = []

            if tipo == "linha":
                self.figura_nova = Linha(
                    event.x, event.y, event.x, event.y, cor_borda, cor_preench_
                )
            elif tipo == "retangulo":
                self.figura_nova = Retangulo(
                    event.x, event.y, event.x, event.y, cor_borda, cor_preench_
                )
            elif tipo == "oval":
                self.figura_nova = Oval(
                    event.x, event.y, event.x, event.y, cor_borda, cor_preench_
                )
            elif tipo == "circulo":
                self.figura_nova = Circulo(event.x, event.y, 0, cor_borda, cor_preench_)
            elif tipo == "rabisco":
                self.figura_nova = Rabisco(
                    [(event.x, event.y)], cor_borda, cor_preench_
                )

    # Função que roda enquanto o usuário arrasta o mouse pela tela
    def tratar_arrasto(self, event):
        if self.figura_nova == None or self.ferramenta_atual == "poligono":
            return

        if self.ferramenta_atual == "rabisco":
            self.figura_nova.pontos.append((event.x, event.y))

        elif self.ferramenta_atual == "circulo":
            distancia = (self.figura_nova.x - event.x) ** 2 + (
                self.figura_nova.y - event.y
            ) ** 2
            raio = distancia**0.5
            self.figura_nova.raio = raio

        elif (
            self.ferramenta_atual == "linha"
            or self.ferramenta_atual == "retangulo"
            or self.ferramenta_atual == "oval"
        ):
            self.figura_nova.x2 = event.x
            self.figura_nova.y2 = event.y

        self.desenhar_figuras()
        self.figura_nova.desenhar_nova(self.canvas)

    # Função que roda quando o usuário solta o botão do mouse
    def tratar_soltar(self, event):
        if self.ferramenta_atual == "poligono":
            return

        if self.figura_nova != None:
            if self.figura_nova.incompleta() == False:
                self.figuras.append(self.figura_nova)

        self.figura_nova = None
        self.desenhar_figuras()

    # Função que finaliza o poligono com dois cliques na tela
    def finalizar_poligono(self, event):
        if self.ferramenta_atual == "poligono" and self.figura_nova != None:
            if self.figura_nova.incompleta() == False:
                self.figuras.append(self.figura_nova)

            self.figura_nova = None
            self.pontos_poligono_atual = []
            self.desenhar_figuras()

    def desenhar_figuras(self):
        self.canvas.delete("all")

        for f in self.figuras:
            f.desenhar(self.canvas)

    # Funçõa que reinicia todo o programa
    def reset(self, event):
        self.figuras.clear()
        self.figura_nova = None
        self.pontos_poligono_atual = []
        self.canvas.delete("all")


# Código que abre a janela do Tkinter
if __name__ == "__main__":
    janela = Tk()
    app = AppDesenho(janela)
    janela.mainloop()
