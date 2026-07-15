class FiguraModel:
    def __init__(
        self,
        tipo,
        cor_borda,
        cor_preenchimento,
        ini_x,
        ini_y,
        fin_x=None,
        fin_y=None,
        raio=None,
        pontos=None,
    ):

        # Dados que todas as figuras tem
        self.tipo = tipo          
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.ini_x = ini_x
        self.ini_y = ini_y

        # Dados específicos para cada tipo de figura
        self.fin_x = fin_x
        self.fin_y = fin_y
        self.raio = raio
        self.pontos = pontos if pontos is not None else []
