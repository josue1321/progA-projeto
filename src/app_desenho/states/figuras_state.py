from abc import ABC, abstractmethod


class FiguraState(ABC):
    def __init__(self, cor_borda, cor_preenchimento, ini_x, ini_y):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.ini_x = ini_x
        self.ini_y = ini_y

    @abstractmethod
    def desenhar(self, canvas):
        pass

    @abstractmethod
    def desenhar_nova(self, canvas):
        pass

    @abstractmethod
    def incompleta(self) -> bool:
        pass


class LinhaState(FiguraState):
    def __init__(
        self, cor_borda, cor_preenchimento, ini_x, ini_y, fin_x=None, fin_y=None
    ):
        super().__init__(cor_borda, cor_preenchimento, ini_x, ini_y)
        self.fin_x = fin_x
        self.fin_y = fin_y

    def desenhar(self, canvas):
        canvas.create_line(
            self.ini_x, self.ini_y, self.fin_x, self.fin_y, fill=self.cor_borda
        )

    def desenhar_nova(self, canvas):
        canvas.create_line(
            self.ini_x,
            self.ini_y,
            self.fin_x,
            self.fin_y,
            fill=self.cor_borda,
            dash=(4, 2),
        )

    def incompleta(self) -> bool:
        if self.fin_x is None or self.fin_y is None:
            return True
        return (self.ini_x, self.ini_y) == (self.fin_x, self.fin_y)


class RetanguloState(FiguraState):
    def __init__(
        self, cor_borda, cor_preenchimento, ini_x, ini_y, fin_x=None, fin_y=None
    ):
        super().__init__(cor_borda, cor_preenchimento, ini_x, ini_y)
        self.fin_x = fin_x
        self.fin_y = fin_y

    def desenhar(self, canvas):
        canvas.create_rectangle(
            self.ini_x,
            self.ini_y,
            self.fin_x,
            self.fin_y,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
        )

    def desenhar_nova(self, canvas):
        canvas.create_rectangle(
            self.ini_x,
            self.ini_y,
            self.fin_x,
            self.fin_y,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
            dash=(4, 2),
        )

    def incompleta(self) -> bool:
        if self.fin_x is None or self.fin_y is None:
            return True
        return (self.ini_x, self.ini_y) == (self.fin_x, self.fin_y)


class OvalState(FiguraState):
    def __init__(
        self, cor_borda, cor_preenchimento, ini_x, ini_y, fin_x=None, fin_y=None
    ):
        super().__init__(cor_borda, cor_preenchimento, ini_x, ini_y)
        self.fin_x = fin_x
        self.fin_y = fin_y

    def desenhar(self, canvas):
        canvas.create_oval(
            self.ini_x,
            self.ini_y,
            self.fin_x,
            self.fin_y,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
        )

    def desenhar_nova(self, canvas):
        canvas.create_oval(
            self.ini_x,
            self.ini_y,
            self.fin_x,
            self.fin_y,
            outline=self.cor_borda,
            fill=self.cor_preenchimento,
            dash=(4, 2),
        )

    def incompleta(self) -> bool:
        if self.fin_x is None or self.fin_y is None:
            return True
        return (self.ini_x, self.ini_y) == (self.fin_x, self.fin_y)


class CirculoState(FiguraState):
    def __init__(self, cor_borda, cor_preenchimento, ini_x, ini_y, raio=None):
        super().__init__(cor_borda, cor_preenchimento, ini_x, ini_y)
        self.raio = raio

    def desenhar(self, canvas):
        if self.raio is not None:
            canvas.create_oval(
                self.ini_x - self.raio,
                self.ini_y - self.raio,
                self.ini_x + self.raio,
                self.ini_y + self.raio,
                outline=self.cor_borda,
                fill=self.cor_preenchimento,
            )

    def desenhar_nova(self, canvas):
        if self.raio is not None:
            canvas.create_oval(
                self.ini_x - self.raio,
                self.ini_y - self.raio,
                self.ini_x + self.raio,
                self.ini_y + self.raio,
                outline=self.cor_borda,
                fill=self.cor_preenchimento,
                dash=(4, 2),
            )

    def incompleta(self) -> bool:
        return self.raio == 0 or self.raio is None


class RabiscoState(FiguraState):
    def __init__(self, cor_borda, cor_preenchimento, ini_x, ini_y, pontos=None):
        super().__init__(cor_borda, cor_preenchimento, ini_x, ini_y)
        self.pontos = pontos if pontos is not None else []

    def desenhar(self, canvas):
        if len(self.pontos) > 1:
            canvas.create_line(self.pontos, fill=self.cor_borda)

    def desenhar_nova(self, canvas):
        if len(self.pontos) > 1:
            canvas.create_line(self.pontos, fill=self.cor_borda, dash=(4, 2))

    def incompleta(self) -> bool:
        return len(self.pontos) <= 1


class PoligonoState(FiguraState):
    def __init__(self, cor_borda, cor_preenchimento, ini_x, ini_y, pontos=None):
        super().__init__(cor_borda, cor_preenchimento, ini_x, ini_y)
        self.pontos = pontos if pontos is not None else []

    def _get_pontos_planos(self):
        return [coord for pt in self.pontos for coord in pt]

    def desenhar(self, canvas):
        if len(self.pontos) >= 3:
            canvas.create_polygon(
                self._get_pontos_planos(),
                outline=self.cor_borda,
                fill=self.cor_preenchimento,
            )

    def desenhar_nova(self, canvas):
        if len(self.pontos) >= 1:
            pontos_planos = self._get_pontos_planos()
            if (
                len(pontos_planos) >= 4
            ):  # Precisa de pelo menos 2 pontos (4 coordenadas) para fazer uma linha
                canvas.create_line(pontos_planos, fill=self.cor_borda, dash=(4, 2))

    def incompleta(self) -> bool:
        return len(self.pontos) < 3
