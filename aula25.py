from tkinter import *


class Principal:  # Cria a classe princiapl
    def __init__(self, master=None):  # cria o método inical e que será filho da classe Principal
        self.fontePadrão = ("Arial", "10")
        # definimos o container pai com um frame
        self.Container1 = Frame(master)
        # Posiciona o container na tela a partir do top e bottom
        self.Container1["pady"] = 10
        self.Container1["bg"] = "light green"  # define uma cor de fundo
        self.Container1.pack()  # para exibir o widgets do container

        # Cria um container para label e text field nome
        self.Container2 = Frame(master)
        # posiciona o container na tela a partir de left e right
        self.Container2["padx"] = 20
        self.Container2["bg"] = "light green"
        self.Container2.pack()

        # Cria um container para label e text filed senha
        self.Container3 = Frame(master)
        self.Container3["padx"] = 20
        self.Container3["bg"] = "light green"
        self.Container3.pack()

        # Cria um container para o botão AUTENTICAR e a label MENSAGEM
        self.Container4 = Frame(master)
        self.Container4["pady"] = 20
        self.Container4["bg"] = "light green"
        self.Container4.pack()

        self.titulo = Label(self.Container1, text="Dados do usuário:")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo["bg"] = "light green"
        self.titulo.pack()

        self.nomeLabel = Label(
            self.Container2, text="Nome", font=self.fontePadrão)
        self.nomeLabel["bg"] = "light green"
        self.nomeLabel.pack(side=LEFT)  # Define o lado da exibição

        # Utiliza o método Entry (input) para receber dados via teclado
        self.nome = Entry(self.Container2)
        self.nome.focus()  # Determina a posição do cursor na caixa de texto
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrão
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(
            self.Container3, text="senha", font=self.fontePadrão)
        self.senhaLabel["bg"] = "light green"
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.Container3)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrão
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.Container4)
        self.autenticar["text"] = "AUTENTICAR"
        self.autenticar["font"] = ("Calibri", "10", "bold")
        self.autenticar["width"] = 12
        self.autenticar["bg"] = "white"
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.sair = Button()
        self.sair["text"] = "SAIR"
        self.sair["font"] = ("Calibri", "10", "bold")
        self.sair["width"] = 5
        self.sair["command"] = quit
        self.sair.pack(side=TOP)

        self.mensagem = Label(self.Container4, text="", font=self.fontePadrão)
        self.mensagem["bg"] = "light green"
        self.mensagem.pack()
# Método para verificar a senha

    def verificaSenha(self):
        usuario = self.nome.get()  # Apanha os dados digitados pelo usuário no text field 'nome'
        senha = self.senha.get()
        if usuario == "Marcus" and senha == "qwe789":
            self.mensagem["text"] = "Autenticado!"
            self.nome["fg"] = "gray"
            self.senha["fg"] = "gray"
            self.sair.focus_force()
        else:
            self.mensagem["text"] = "Usuário e/ou senha incorretos!"
            self.senha.delete(0, END)
            self.nome.delete(0, END)
            self.nome.focus()


tela = Tk()  # Instancia a classe 'TK()' ATRAVÉS DA VARIÁVEL 'tela'
tela.title("TELA DE LOGIN")
tela["bg"] = "light green"
# define o tamanho da tela width(largura) x height (altura)
tela.geometry("400x250")
# Instância da classe Principal, passasmos a varável tela como parâmetro
Principal(tela)
tela.mainloop()  # metodo obrigatório para carregar a tela e para que os eventos ocorram
