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
