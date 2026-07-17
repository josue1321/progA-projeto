from tkinter import Tk

from controllers.canva_controller import CanvaController
from models.canva_model import CanvaModel
from views.app_view import AppDesenhoView
from models.figuras_model import FiguraModel
from controllers.figura_controller import FiguraController

# código que abre a janela do Tkinter
if __name__ == "__main__":
    janela = Tk()
    
    # cria as instâncias principais do quadro
    model = CanvaModel()
    view = AppDesenhoView(janela)
    
    # inicia o controller passando todas as dependências
    CanvaController(
        model=model, 
        view=view, 
        figura_model=FiguraModel, 
        figura_controller=FiguraController
    )
    
    janela.mainloop()
