from tkinter import Tk

from controllers.canva_controller import CanvaController
from controllers.figura_controller import FiguraController
from models.canva_model import CanvaModel
from views.app_view import AppDesenhoView

if __name__ == "__main__":
    root = Tk()
    model = CanvaModel()
    view = AppDesenhoView(root)
    CanvaController(model, view, FiguraController)
    root.mainloop()
