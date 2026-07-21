class CanvaModel:
    def __init__(self):
        self.figuras = []
        self.figura_nova = None

        self.cor_borda_atual = "black"
        self.cor_preenchimento_atual = "white"

    def adicionar_figura(self):
        if self.figura_nova is not None:
            self.figuras.append(self.figura_nova)
            self.limpar_estado()

    def limpar_estado(self):
        self.figura_nova = None

    def resetar_canva(self):
        self.figuras.clear()
        self.limpar_estado()