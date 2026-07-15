# Importa as ferramentas gráficas do Tkinter
import tkinter as Tk


# Código que abre a janela do Tkinter
if __name__ == "__main__":
    janela = Tk()
    app = AppDesenho(janela)
    janela.mainloop()
