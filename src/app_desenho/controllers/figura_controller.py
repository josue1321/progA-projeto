class FiguraController:
    def __init__(self):



    def desenhar(self, canvas):
        pass

    def desenhar_nova(self, canvas):
        pass

    def incompleta(self) -> bool:
        return False

    
    # Linha
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

    # Rabisco
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

    # Retangulo
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
 
    # Oval
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

    # Circulo
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

    # Poligono
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