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

class Rabisco(Figura):

    #Define a logica para o desenho dos rabiscos

    def __init__(self, pontos, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.pontos = pontos

    def desenhar(self, canvas):
        if len(self.pontos) > 1:
            canvas.create_line(self.pontos, fill=self.cor_borda)

    def desenhar_nova(self, canvas):
        if len(self.pontos) > 1:
            canvas.create_line(self.pontos, fill=self.cor_borda, dash=(4, 2))

    def incompleta(self):
        if len(self.pontos) <= 1:
            return True
        return False


class Retangulo(Figura):

    # Define a lógica para o desenhos dos retangulos

    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def desenhar(self, canvas):
        canvas.create_rectangle(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
        )

    def desenhar_nova(self, canvas):
        canvas.create_rectangle(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
            dash=(4, 2),
        )

    def incompleta(self):
        if (self.x1, self.y1) == (self.x2, self.y2):
            return True
        return False


class Oval(Figura):

    # Define a lógica para o desenhos ovais

    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def desenhar(self, canvas):
        canvas.create_oval(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
        )

    def desenhar_nova(self, canvas):
        canvas.create_oval(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
            dash=(4, 2),
        )

    def incompleta(self):
        if (self.x1, self.y1) == (self.x2, self.y2):
            return True
        return False


class Circulo(Figura):

    # Define a lógica para o desenhos circulares

    def __init__(self, x, y, raio, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.x = x
        self.y = y
        self.raio = raio

    def desenhar(self, canvas):
        canvas.create_oval(
            self.x - self.raio,
            self.y - self.raio,
            self.x + self.raio,
            self.y + self.raio,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
        )

    def desenhar_nova(self, canvas):
        canvas.create_oval(
            self.x - self.raio,
            self.y - self.raio,
            self.x + self.raio,
            self.y + self.raio,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
            dash=(4, 2),
        )

    def incompleta(self):
        if self.raio == 0:
            return True
        return False

class Poligono(Figura):

    # Define a lógica para o desenhos dos poligonos
    # O polinomio vai funcinar baseado em cliques na tela, onde cada clique é um vertice do poligono


    def __init__(self, pontos, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.pontos = pontos

    def desenhar(self, canvas):
        if len(self.pontos) >= 3:
            pontos_planos = []
            for pt in self.pontos:
                pontos_planos.append(pt[0])
                pontos_planos.append(pt[1])

            canvas.create_polygon(
                pontos_planos,
                outline=self.cor_borda,
                fill=self.cor_preenchimento,
            )

    def desenhar_nova(self, canvas):
        if len(self.pontos) >= 1:
            pontos_planos = []
            for pt in self.pontos:
                pontos_planos.append(pt[0])
                pontos_planos.append(pt[1])

            if len(pontos_planos) >= 4:
                canvas.create_line(pontos_planos, fill=self.cor_borda, dash=(4, 2))

    def incompleta(self):
        if len(self.pontos) < 3:
            return True
        return False