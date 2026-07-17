class CanvaController:
    def __init__(self, model, view, figura_model, figura_controller):
        self.model = model
        self.view = view
        self.figura_model = figura_model
        self.figura_controller = figura_controller

        self.vincular_eventos()

    def vincular_eventos(self):
        self.view.canvas.bind("<ButtonPress-1>", self.tratar_clique)
        self.view.canvas.bind("<B1-Motion>", self.tratar_arrasto)
        self.view.canvas.bind("<ButtonRelease-1>", self.tratar_soltar)
        self.view.canvas.bind("<Double-Button-1>", self.finalizar_poligono)
        self.view.canvas.bind("<ButtonPress-3>", self.reset)

    def tratar_clique(self, event):
        # pega o que esta nos menus da view e coloca no model
        self.model.ferramenta_atual = self.view.tipo_figura_var.get()
        self.model.cor_borda_atual = self.view.cor_lapis_var.get()
        self.model.cor_preenchimento_atual = self.view.cor_preenchimento_var.get()

        tipo = self.model.ferramenta_atual
        cor_borda = self.model.cor_borda_atual
        cor_preench = self.model.cor_preenchimento_atual

        # cria o model da figura dependendo da ferramenta escolhida
        if tipo == "poligono":
            self.model.pontos_poligono_atual.append((event.x, event.y))
            novo_modelo = self.figura_model(
                tipo=tipo, cor_borda=cor_borda, cor_preenchimento=cor_preench,
                ini_x=event.x, ini_y=event.y,
                pontos=list(self.model.pontos_poligono_atual)
            )
            self.model.figura_nova = novo_modelo
        else:
            self.model.pontos_poligono_atual = []

            if tipo in ["linha", "retangulo", "oval"]:
                novo_modelo = self.figura_model(
                    tipo=tipo, cor_borda=cor_borda, cor_preenchimento=cor_preench,
                    ini_x=event.x, ini_y=event.y, fin_x=event.x, fin_y=event.y
                )
            elif tipo == "circulo":
                novo_modelo = self.figura_model(
                    tipo=tipo, cor_borda=cor_borda, cor_preenchimento=cor_preench,
                    ini_x=event.x, ini_y=event.y, raio=0
                )
            elif tipo == "rabisco":
                novo_modelo = self.figura_model(
                    tipo=tipo, cor_borda=cor_borda, cor_preenchimento=cor_preench,
                    ini_x=event.x, ini_y=event.y, pontos=[(event.x, event.y)]
                )
            
            self.model.figura_nova = novo_modelo

        self.atualizar_tela()

    def tratar_arrasto(self, event):
        if self.model.figura_nova is None or self.model.ferramenta_atual == "poligono":
            return

        figura = self.model.figura_nova

        if self.model.ferramenta_atual == "rabisco":
            figura.pontos.append((event.x, event.y))

        elif self.model.ferramenta_atual == "circulo":
            distancia = (figura.ini_x - event.x) ** 2 + (figura.ini_y - event.y) ** 2
            figura.raio = distancia ** 0.5

        elif self.model.ferramenta_atual in ["linha", "retangulo", "oval"]:
            figura.fin_x = event.x
            figura.fin_y = event.y

        self.atualizar_tela()

    def tratar_soltar(self, event):
        if self.model.ferramenta_atual == "poligono":
            return

        if self.model.figura_nova is not None:
            validador = self.figura_controller(self.model.figura_nova)
            if not validador.incompleta():
                self.model.adicionar_figura() 
            else:
                self.model.limpar_estado_temporario()

        self.atualizar_tela()

    def finalizar_poligono(self, event):
        if self.model.ferramenta_atual == "poligono" and self.model.figura_nova is not None:
            validador = self.figura_controller(self.model.figura_nova)
            if not validador.incompleta():
                self.model.adicionar_figura()
            else:
                self.model.limpar_estado_temporario()
        
        self.atualizar_tela()

    def atualizar_tela(self):
        self.view.canvas.delete("all")

        for figura_model in self.model.figuras:
            controller_figura = self.figura_controller(figura_model)
            controller_figura.desenhar(self.view.canvas)

        if self.model.figura_nova is not None:
            controller_nova = self.figura_controller(self.model.figura_nova)
            controller_nova.desenhar_nova(self.view.canvas)

    def reset(self, event):
        self.model.resetar_quadro()
        self.atualizar_tela()