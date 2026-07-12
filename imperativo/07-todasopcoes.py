from tkinter import Tk, Canvas, Frame, StringVar, ttk, W


# Quando mouse é pressionado
def iniciar_figura_nova(event):
    global figura_nova
    tipo = tipo_figura_var.get()
    cor_borda = cor_lapis_var.get()
    cor_preenchimento = cor_preenchimento_var.get()

    if tipo in ("linha", "retangulo", "oval"):
        figura_nova = (
            tipo,
            (event.x, event.y, event.x, event.y),
            cor_borda,
            cor_preenchimento,
        )
    elif tipo == "circulo":
        figura_nova = ("circulo", (event.x, event.y, 0), cor_borda, cor_preenchimento)
    else:
        figura_nova = ("rabisco", [(event.x, event.y)], cor_borda, cor_preenchimento)


# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    fig, valores, cor_borda, cor_preenchimento = figura_nova

    if fig == "rabisco":
        valores.append((event.x, event.y))
        figura_nova = (fig, valores, cor_borda, cor_preenchimento)
    elif fig == "circulo":
        x, y, _ = valores
        raio = ((x - event.x) ** 2 + (y - event.y) ** 2) ** 0.5
        figura_nova = (fig, (x, y, raio), cor_borda, cor_preenchimento)
    else:  # "linha", "retângulo", "oval"
        figura_nova = (
            fig,
            (valores[0], valores[1], event.x, event.y),
            cor_borda,
            cor_preenchimento,
        )

    desenhar_figuras()
    desenhar_figura_nova()


def desenhar_figuras():
    canvas.delete("all")
    for fig, valores, cor_borda, cor_preenchimento in figuras:
        if fig == "linha":
            canvas.create_line(
                valores[0], valores[1], valores[2], valores[3], fill=cor_borda
            )
        elif fig == "rabisco":
            canvas.create_line(valores, fill=cor_borda)
        elif fig == "retangulo":
            canvas.create_rectangle(
                valores[0],
                valores[1],
                valores[2],
                valores[3],
                outline=cor_borda,
                fill=cor_preenchimento,
            )
        elif fig == "oval":
            canvas.create_oval(
                valores[0],
                valores[1],
                valores[2],
                valores[3],
                outline=cor_borda,
                fill=cor_preenchimento,
            )
        elif fig == "circulo":
            x, y, r = valores
            canvas.create_oval(
                x - r,
                y - r,
                x + r,
                y + r,
                outline=cor_borda,
                fill=cor_preenchimento,
            )


def desenhar_figura_nova():
    fig, valores, cor_borda, cor_preenchimento = figura_nova

    if fig == "linha":
        canvas.create_line(
            valores[0], valores[1], valores[2], valores[3], fill=cor_borda, dash=(4, 2)
        )
    elif fig == "rabisco":
        canvas.create_line(valores, fill=cor_borda, dash=(4, 2))
    elif fig == "retangulo":
        canvas.create_rectangle(
            valores[0],
            valores[1],
            valores[2],
            valores[3],
            outline=cor_borda,
            fill=cor_preenchimento,
            dash=(4, 2),
        )
    elif fig == "oval":
        canvas.create_oval(
            valores[0],
            valores[1],
            valores[2],
            valores[3],
            outline=cor_borda,
            fill=cor_preenchimento,
            dash=(4, 2),
        )
    elif fig == "circulo":
        x, y, r = valores
        canvas.create_oval(
            x - r,
            y - r,
            x + r,
            y + r,
            outline=cor_borda,
            fill=cor_preenchimento,
            dash=(4, 2),
        )


# Quando mouse é solto
def incluir_figura_nova(event):
    # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
    if not incompleta(figura_nova):
        figuras.append(figura_nova)
    desenhar_figuras()


def incompleta(figura):
    fig, values, _, _ = figura
    if fig in ["linha", "retangulo", "oval"]:
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "circulo":
        return values[2] == 0
    else:  # fig == "rabisco"
        return len(values) <= 1


def reset(event):
    figuras.clear()
    canvas.delete("all")


# ******* MAIN *******#

figuras = []  # Todas as figuras desenhadas
figura_nova = (
    None  # Figura que está sendo desenhada, mas ainda não foi incluída em figuras
)

root = Tk()
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {"padx": 5, "pady": 5}

# label
label = ttk.Label(frame, text="Figura:")
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root)
# Guarda o tipo de figura selecionado no option menu
option_menu = ttk.OptionMenu(
    frame, tipo_figura_var, "linha", "linha", "rabisco", "circulo", "retangulo", "oval"
)
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# COR DA BORDA
label = ttk.Label(frame, text="Cor da Borda:")
label.grid(column=0, row=1, sticky=W, **paddings)

cor_lapis_var = StringVar(root)
# Guarda a cor da borda da figura selecionado no option menu
option_menu_borda = ttk.OptionMenu(
    frame, cor_lapis_var, "black", "black", "red", "blue"
)
option_menu_borda.grid(column=1, row=1, sticky=W, **paddings)

# COR DE PREENCHIMENTO
label = ttk.Label(frame, text="Cor para preencher:")
label.grid(column=0, row=2, sticky=W, **paddings)

cor_preenchimento_var = StringVar(root)
# Guarda a cor de dentro da figura selecionado no option menu
option_menu_preench = ttk.OptionMenu(
    frame, cor_preenchimento_var, "white", "white", "black", "red", "blue"
)
option_menu_preench.grid(column=1, row=2, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg="white", width=600, height=600)
canvas.grid(column=0, row=3, columnspan=2, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind("<ButtonPress-1>", iniciar_figura_nova)
canvas.bind("<B1-Motion>", atualizar_figura_nova)
canvas.bind("<ButtonRelease-1>", incluir_figura_nova)
canvas.bind("<ButtonPress-3>", reset)

root.mainloop()
