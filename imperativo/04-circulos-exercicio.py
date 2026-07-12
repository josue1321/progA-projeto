# Exercício: desenhar círculos.
#  O centro é a posição onde o mouse foi clicado
#  O raio é definido pela distância entre o centro e a posição atual do mouse
from tkinter import W, Frame, StringVar, Tk, Canvas, ttk


# Quando mouse é pressionado
def inicia_linha(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y


# Quando mouse é movido com o botão pressionado
def atualiza_linha(event):
    global fim_x, fim_y, raio
    fim_x = event.x
    fim_y = event.y
    raio = ((ini_x - fim_x) ** 2 + (ini_y - fim_y) ** 2) ** 0.5
    desenhar()
    cor_borda = cor_lapis_var.get()
    cor_preenchimento = cor_preenchimento_var.get()
    canvas.create_oval(
        ini_x - raio,
        ini_y - raio,
        ini_x + raio,
        ini_y + raio,
        outline=cor_borda,
        fill=cor_preenchimento,
    )


# Quando mouse é solto
def incluir_linha(event):
    cor_borda = cor_lapis_var.get()
    cor_preenchimento = cor_preenchimento_var.get()
    circulos.append((ini_x, ini_y, raio, cor_borda, cor_preenchimento))


def desenhar():
    canvas.delete("all")
    for circulo in circulos:
        x, y, r, cor_borda, cor_preenchimento = circulo
        canvas.create_oval(
            x - r, y - r, x + r, y + r, outline=cor_borda, fill=cor_preenchimento
        )


# ******* MAIN *******#

# Todos os círculos desenhados são armazenados aqui
circulos = []
raio = None

root = Tk()
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {"padx": 5, "pady": 5}

# COR DA BORDA
label = ttk.Label(frame, text="Cor da Borda:")
label.grid(column=0, row=0, sticky=W, **paddings)

cor_lapis_var = StringVar(root)
# Guarda a cor da borda da figura selecionado no option menu
option_menu_borda = ttk.OptionMenu(
    frame, cor_lapis_var, "black", "black", "red", "blue"
)
option_menu_borda.grid(column=1, row=0, sticky=W, **paddings)

# COR DE PREENCHIMENTO
label = ttk.Label(frame, text="Cor para preencher:")
label.grid(column=0, row=1, sticky=W, **paddings)

cor_preenchimento_var = StringVar(root)
# Guarda a cor de dentro da figura selecionado no option menu
option_menu_preench = ttk.OptionMenu(
    frame, cor_preenchimento_var, "white", "white", "black", "red", "blue"
)
option_menu_preench.grid(column=1, row=1, sticky=W, **paddings)

canvas = Canvas(frame, bg="white", width=600, height=600)
canvas.grid(column=0, row=2, columnspan=2, sticky=W, **paddings)


frame.pack()

ini_x = None
ini_y = None
fim_x = None
fim_y = None

canvas.bind("<ButtonPress-1>", inicia_linha)
canvas.bind("<B1-Motion>", atualiza_linha)
canvas.bind("<ButtonRelease-1>", incluir_linha)

root.mainloop()
