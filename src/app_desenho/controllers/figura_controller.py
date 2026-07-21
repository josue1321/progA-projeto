class FiguraController:
    def __init__(self, model):
        self.model = model

    def desenhar(self, canvas):
        self.model.desenhar(canvas)

    def desenhar_nova(self, canvas):
        self.model.desenhar_nova(canvas)

    def incompleta(self):
        return self.model.incompleta()
