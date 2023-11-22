import customtkinter as ctk
import main
import CTkListbox
# Determina a raíz da nossa janela
root = ctk.CTk()


class Application:

    # Inicio da Aplicação
    def __init__(self):
        self.root = root
        self.janela()
        self.frames_da_tela()
        self.slider_da_tela()
        self.texto_na_tela()
        self.entry()
        self.button()
        self.colocar_list_box()
        self.contador = 0
        self.colocar_text_box()
        root.mainloop()
    # Mostra as caraceteristicas da janela

    def janela(self):
        # Determina o nome da nossa janela
        self.root.title("Weasel Program")
        # Determina o tamanho da janela
        self.root.geometry("1000x600")
        self.root.resizable(False, False)
        # Determina o tema da janela
        ctk.set_appearance_mode("Dark")

    def frames_da_tela(self):
        # Mostra o frame que esta a esquerda
        self.frame1 = ctk.CTkFrame(self.root)
        self.frame1.place(relx='0', rely='0', relheight='1', relwidth='0.3')
    # Mostra o Slider da tela

    def slider_da_tela(self):
        # Qual o valor Inicial do Slider
        self.scale_int = ctk.IntVar(value=100)
        self.slider_populacao = ctk.CTkSlider(self.frame1,
                                              from_=10,
                                              to=200,
                                              width=300,
                                              height=20,
                                              variable=self.scale_int,
                                              command=lambda value:
                                              self.mudar_texto())
        self.slider_populacao.place(relx='0', rely='0.7',)

    # Mostra os Textos que tem na tela
    def texto_na_tela(self):

        # Texto da quantidade de individuos por população
        (ctk.CTkLabel(self.frame1, text="Quantidade de Indíviduos "
                                        "\n por Geração", font=("Arial", 20))
         .place(relx='0.1', rely='0.75'))

        ctk.CTkLabel(self.frame1,
                     text='Weasel \n    Program',
                     font=("Arial", 50)).place(relx='0.01', rely='0.05')

        # Texto que muda conforme o SLider
        self.texto_geracoes = ctk.CTkLabel(self.frame1,
                                           text=self.scale_int.get(),
                                           font=("Arial", 20))

        self.texto_geracoes.place(relx='0.45', rely='0.6')

# Mostra a Entry da Tela
    def entry(self):
        self.string_entry = ctk.StringVar()
        self.entry = ctk.CTkEntry(self.root,
                                  placeholder_text=' '*45+'DIGITE SUA FRASE',
                                  width=530,
                                  height=30,
                                  font=("Arial", 17),
                                  textvariable=self.string_entry)

        self.entry.place(relx='0.32', rely='0.88')

# Mostra o Botão SEND
    def button(self):

        self.send_input_button = ctk.CTkButton(self.root,
                                               text='SEND',
                                               command=lambda:
                                               self.enviar_comandos())

        self.send_input_button.place(relx='0.855', rely='0.88')

    # Muda o texto com o slider
    def mudar_texto(self):
        self.texto_geracoes.configure(text=self.scale_int.get())

# Envia informaçoes pro main.py
    def enviar_comandos(self):
        # Se a Listbox Ja tiver elementos ele apaga
        if self.contador != 0:
            self.listbox.delete(0, "END")
            self.text_box.configure(state='normal')
            self.text_box.delete(0.0, "end")
            self.text_box.configure(state='disabled')

        self.dicionario, self.lista = main.monkeys(
                                            (self.string_entry.get()).upper(),
                                            self.scale_int.get())

        self.adicionar_elementos_listbox()
        self.contador += 1

# Adiociona ListBox na janela
    def colocar_list_box(self):
        self.listbox = CTkListbox.CTkListbox(self.root, height=390, width=640,)
        self.listbox.place(x=325, y=10)

# Adiciona elementos na Listbox
    def adicionar_elementos_listbox(self):
        for i in range(len(self.lista)):
            self.lista_da_list_box = self.lista[i][2]
            self.listbox.insert(i,
                                'Geração: '+str(self.lista[i][0])+''
                                '           Score: ' +
                                str(self.lista[i][1]) +
                                '           Melhor Palavra: ' +
                                self.lista_da_list_box[:40])
        self.lista.clear()
        self.mudar_text_box()

    def colocar_text_box(self):
        self.text_box = ctk.CTkTextbox(self.root, width=660, height=100)
        self.text_box.grid(row=0, column=0, sticky='nsew')
        self.text_box.place(x=325, y=420)
        self.text_box.configure(state='disabled')

    def mudar_text_box(self):
        self.text_box.configure(state='normal')

        self.text_box.insert("0.0", self.lista_da_list_box)
        self.text_box.configure(state='disabled')


Application()
