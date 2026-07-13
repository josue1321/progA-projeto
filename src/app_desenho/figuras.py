class Figura:

    # Cria a base para o desenho das figuras 


    def __init__(self, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def desenhar(self, canvas):
        pass
    
    def desenhar_nova(self, canvas):
        pass

    def incompleta(self):
        return False


class Linha(Figura):

    #Define a logica que gera as linhas

    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def desenhar(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda)

    def desenhar_nova(self, canvas):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda, dash=(4, 2)
        )

    def incompleta(self):
        if (self.x1, self.y1) == (self.x2, self.y2):
            return True
        return False
