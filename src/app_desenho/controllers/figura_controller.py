class FiguraController:
    def __init__(self, model):
        self.model = model

    def desenhar(self, canvas):
        tipo = self.model.tipo

        match tipo:
            case "linha":
                canvas.create_line(
                    self.model.ini_x,
                    self.model.ini_y,
                    self.model.fin_x,
                    self.model.fin_y,
                    fill=self.model.cor_borda,
                )

            case "rabisco":
                if len(self.model.pontos) > 1:
                    canvas.create_line(self.model.pontos, fill=self.model.cor_borda)

            case "retangulo":
                canvas.create_rectangle(
                    self.model.ini_x,
                    self.model.ini_y,
                    self.model.fin_x,
                    self.model.fin_y,
                    outline=self.model.cor_borda,
                    fill=self.model.cor_preenchimento,
                )

            case "oval":
                canvas.create_oval(
                    self.model.ini_x,
                    self.model.ini_y,
                    self.model.fin_x,
                    self.model.fin_y,
                    outline=self.model.cor_borda,
                    fill=self.model.cor_preenchimento,
                )

            case "circulo":
                if self.model.raio is not None:
                    canvas.create_oval(
                        self.model.ini_x - self.model.raio,
                        self.model.ini_y - self.model.raio,
                        self.model.ini_x + self.model.raio,
                        self.model.ini_y + self.model.raio,
                        outline=self.model.cor_borda,
                        fill=self.model.cor_preenchimento,
                    )

            case "poligono":
                if len(self.model.pontos) >= 3:
                    # Transforma a lista de tuplas numa lista plana [x1, y1, x2, y2...]
                    pontos_planos = [coord for pt in self.model.pontos for coord in pt]
                    canvas.create_polygon(
                        pontos_planos,
                        outline=self.model.cor_borda,
                        fill=self.model.cor_preenchimento,
                    )

    def desenhar_nova(self, canvas):
        tipo = self.model.tipo

        match tipo:
            case "linha":
                canvas.create_line(
                    self.model.ini_x,
                    self.model.ini_y,
                    self.model.fin_x,
                    self.model.fin_y,
                    fill=self.model.cor_borda,
                    dash=(4, 2),
                )

            case "rabisco":
                if len(self.model.pontos) > 1:
                    canvas.create_line(
                        self.model.pontos, fill=self.model.cor_borda, dash=(4, 2)
                    )

            case "retangulo":
                canvas.create_rectangle(
                    self.model.ini_x,
                    self.model.ini_y,
                    self.model.fin_x,
                    self.model.fin_y,
                    outline=self.model.cor_borda,
                    fill=self.model.cor_preenchimento,
                    dash=(4, 2),
                )

            case "oval":
                canvas.create_oval(
                    self.model.ini_x,
                    self.model.ini_y,
                    self.model.fin_x,
                    self.model.fin_y,
                    outline=self.model.cor_borda,
                    fill=self.model.cor_preenchimento,
                    dash=(4, 2),
                )

            case "circulo":
                if self.model.raio is not None:
                    canvas.create_oval(
                        self.model.ini_x - self.model.raio,
                        self.model.ini_y - self.model.raio,
                        self.model.ini_x + self.model.raio,
                        self.model.ini_y + self.model.raio,
                        outline=self.model.cor_borda,
                        fill=self.model.cor_preenchimento,
                        dash=(4, 2),
                    )

            case "poligono":
                if len(self.model.pontos) >= 1:
                    pontos_planos = [coord for pt in self.model.pontos for coord in pt]
                    if len(pontos_planos) >= 4:
                        canvas.create_line(
                            pontos_planos, fill=self.model.cor_borda, dash=(4, 2)
                        )

    def incompleta(self) -> bool:
        tipo = self.model.tipo

        match tipo:
            case "linha" | "retangulo" | "oval":
                # Verifica se os pontos finais existem e se não são iguais aos iniciais
                if self.model.fin_x is None or self.model.fin_y is None:
                    return True
                return (self.model.ini_x, self.model.ini_y) == (
                    self.model.fin_x,
                    self.model.fin_y,
                )

            case "rabisco":
                return len(self.model.pontos) <= 1

            case "circulo":
                return self.model.raio == 0 or self.model.raio is None

            case "poligono":
                return len(self.model.pontos) < 3

            case _:
                return False
