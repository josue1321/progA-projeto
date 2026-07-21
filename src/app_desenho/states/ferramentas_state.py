from abc import ABC, abstractmethod

from states.figuras_state import CirculoState, PoligonoState, RabiscoState


class FerramentaState(ABC):
    @abstractmethod
    def tratar_clique(self, event, controller):
        pass

    @abstractmethod
    def tratar_arrasto(self, event, controller):
        pass

    def tratar_soltar(self, event, controller):
        self._validar_e_salvar(controller)

    def finalizar_poligono(self, event, controller):
        pass

    def _validar_e_salvar(self, controller):
        if controller.model.figura_nova is not None:
            validador = controller.figura_controller(controller.model.figura_nova)

            if not validador.incompleta():
                controller.model.adicionar_figura()
            else:
                controller.model.limpar_estado()

            controller.atualizar_tela()


class FerramentaDoisPontos(FerramentaState):
    def __init__(self, classe):
        self.classe = classe

    def tratar_clique(self, event, controller):
        cor_borda = controller.model.cor_borda_atual
        cor_preench = controller.model.cor_preenchimento_atual

        controller.model.figura_nova = self.classe(
            cor_borda, cor_preench, event.x, event.y, event.x, event.y
        )
        controller.atualizar_tela()

    def tratar_arrasto(self, event, controller):
        if controller.model.figura_nova:
            controller.model.figura_nova.fin_x = event.x
            controller.model.figura_nova.fin_y = event.y
            controller.atualizar_tela()


class FerramentaCirculo(FerramentaState):
    def tratar_clique(self, event, controller):
        cor_borda = controller.model.cor_borda_atual
        cor_preench = controller.model.cor_preenchimento_atual

        controller.model.figura_nova = CirculoState(
            cor_borda, cor_preench, event.x, event.y, raio=0
        )
        controller.atualizar_tela()

    def tratar_arrasto(self, event, controller):
        if controller.model.figura_nova:
            figura = controller.model.figura_nova
            distancia = (figura.ini_x - event.x) ** 2 + (figura.ini_y - event.y) ** 2
            figura.raio = distancia**0.5
            controller.atualizar_tela()


class FerramentaRabisco(FerramentaState):
    def tratar_clique(self, event, controller):
        cor_borda = controller.model.cor_borda_atual
        cor_preench = controller.model.cor_preenchimento_atual

        controller.model.figura_nova = RabiscoState(
            cor_borda, cor_preench, event.x, event.y, pontos=[(event.x, event.y)]
        )
        controller.atualizar_tela()

    def tratar_arrasto(self, event, controller):
        # Adiciona novos pontos à medida que o mouse se move
        if controller.model.figura_nova:
            controller.model.figura_nova.pontos.append((event.x, event.y))
            controller.atualizar_tela()


class FerramentaPoligono(FerramentaState):
    def __init__(self):
        self.pontos_atuais = []

    def tratar_clique(self, event, controller):
        cor_borda = controller.model.cor_borda_atual
        cor_preench = controller.model.cor_preenchimento_atual

        self.pontos_atuais.append((event.x, event.y))

        controller.model.figura_nova = PoligonoState(
            cor_borda=cor_borda,
            cor_preenchimento=cor_preench,
            ini_x=event.x,
            ini_y=event.y,
            pontos=list(self.pontos_atuais),
        )
        controller.atualizar_tela()

    def tratar_arrasto(self, event, controller):
        pass

    def tratar_soltar(self, event, controller):
        pass

    def finalizar_poligono(self, event, controller):
        self._validar_e_salvar(controller)
        self.pontos_atuais = []
