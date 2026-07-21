import pickle
from tkinter import filedialog, messagebox

from states.ferramentas_state import (
    FerramentaCirculo,
    FerramentaDoisPontos,
    FerramentaPoligono,
    FerramentaRabisco,
)
from states.figuras_state import LinhaState, OvalState, RetanguloState


class CanvaController:
    def __init__(self, model, view, figura_controller):
        self.model = model
        self.view = view

        self.figura_controller = figura_controller

        # Ferramentas disponíveis no select de figuras
        self.ferramentas = {
            "linha": FerramentaDoisPontos(LinhaState),
            "retangulo": FerramentaDoisPontos(RetanguloState),
            "oval": FerramentaDoisPontos(OvalState),
            "circulo": FerramentaCirculo(),
            "rabisco": FerramentaRabisco(),
            "poligono": FerramentaPoligono(),
        }

        self.ferramenta_atual = None
        self.estado_atual = None

        self.vincular_eventos()

    def vincular_eventos(self):
        self.view.canvas.bind("<ButtonPress-1>", self.tratar_clique)
        self.view.canvas.bind("<B1-Motion>", self.tratar_arrasto)
        self.view.canvas.bind("<ButtonRelease-1>", self.tratar_soltar)
        self.view.canvas.bind("<Double-Button-1>", self.finalizar_poligono)
        self.view.canvas.bind("<ButtonPress-3>", self.reset)
        self.view.btn_salvar.config(command=self.salvar_arquivo)
        self.view.btn_abrir.config(command=self.abrir_arquivo)

    def salvar_arquivo(self):
        caminho_arquivo = filedialog.asksaveasfilename(
            defaultextension=".drw",
            filetypes=[
                ("Arquivos de Desenho", "*.drw"),
                ("Todos os Arquivos", "*.*"),
            ],
            title="Salvar Desenho",
        )

        # verifica se a janela esta aberta
        if caminho_arquivo:
            try:
                # Escreve no arquivo
                with open(caminho_arquivo, "wb") as arquivo:
                    pickle.dump(self.model.figuras, arquivo)

                messagebox.showinfo("Sucesso", "Desenho salvo com sucesso!")
            except Exception as e:
                messagebox.showerror(
                    "Erro", f"Ocorreu um erro ao salvar o desenho:\n{e}"
                )

    def abrir_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename(
            defaultextension=".drw",
            filetypes=[
                ("Arquivos de Desenho", "*.drw"),
                ("Todos os Arquivos", "*.*"),
            ],
            title="Abrir Desenho",
        )

        if caminho_arquivo:
            try:
                # Salva no arquivo
                with open(caminho_arquivo, "rb") as arquivo:
                    figuras_carregadas = pickle.load(arquivo)

                # Substitui as figuras do Model pelas figuras do arquivo
                self.model.figuras = figuras_carregadas
                self.model.limpar_estado()
                self.atualizar_tela()

            except Exception as e:
                messagebox.showerror(
                    "Erro", f"Ocorreu um erro ao abrir o desenho:\n{e}"
                )

    # Atualiza o estado para a ferramenta que esta selecionada atualmente
    def _sincronizar_estado(self):
        self.model.cor_borda_atual = self.view.cor_lapis_var.get()
        self.model.cor_preenchimento_atual = self.view.cor_preenchimento_var.get()

        novo_tipo = self.view.tipo_figura_var.get()

        if self.ferramenta_atual != novo_tipo:
            self.ferramenta_atual = novo_tipo
            self.estado_atual = self.ferramentas.get(novo_tipo)

            if isinstance(self.estado_atual, FerramentaPoligono):
                self.estado_atual.pontos_atuais = []

            self.model.limpar_estado()

    def tratar_clique(self, event):
        self._sincronizar_estado()
        if self.estado_atual:
            self.estado_atual.tratar_clique(event, self)

    def tratar_arrasto(self, event):
        if self.estado_atual:
            self.estado_atual.tratar_arrasto(event, self)

    def tratar_soltar(self, event):
        if self.estado_atual:
            self.estado_atual.tratar_soltar(event, self)

    def finalizar_poligono(self, event):
        if self.estado_atual:
            self.estado_atual.finalizar_poligono(event, self)

    def reset(self, event):
        self.model.resetar_canva()
        self.atualizar_tela()

    def atualizar_tela(self):
        self.view.canvas.delete("all")

        for figura_model in self.model.figuras:
            controller_figura = self.figura_controller(figura_model)
            controller_figura.desenhar(self.view.canvas)

        if self.model.figura_nova is not None:
            controller_nova = self.figura_controller(self.model.figura_nova)
            controller_nova.desenhar_nova(self.view.canvas)
