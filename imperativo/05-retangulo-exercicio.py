from tkinter import W, Frame, StringVar, Tk, Canvas, ttk


# Quando mouse é pressionado
def inicia_linha(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y


# Quando mouse é movido com o botão pressionado
def atualiza_linha(event):
    global fim_x, fim_y
    fim_x = event.x
    fim_y = event.y
    desenhar()
    cor_borda = cor_lapis_var.get()
    cor_preenchimento = cor_preenchimento_var.get()
    canvas.create_rectangle(
        ini_x,
        ini_y,
        fim_x,
        fim_y,
        outline=cor_borda,
        fill=cor_preenchimento,
    )


# Quando mouse é solto
def incluir_linha(event):
    cor_borda = cor_lapis_var.get()
    cor_preenchimento = cor_preenchimento_var.get()
    retangulos.append((ini_x, ini_y, fim_x, fim_y, cor_borda, cor_preenchimento))


def desenhar():
    canvas.delete("all")
    for retangulo in retangulos:
        *coords, cor_borda, cor_preenchimento = retangulo
        canvas.create_rectangle(
            coords[0],
            coords[1],
            coords[2],
            coords[3],
            outline=cor_borda,
            fill=cor_preenchimento,
        )


# ******* MAIN *******#

# Todos os retangulos desenhados são armazenados aqui
retangulos = []

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

ini_x = 0
ini_y = 0
fim_x = None
fim_y = None

canvas.bind("<ButtonPress-1>", inicia_linha)
canvas.bind("<B1-Motion>", atualiza_linha)
canvas.bind("<ButtonRelease-1>", incluir_linha)

root.mainloop()
