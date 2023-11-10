from Model import Produto
import tkinter as tk
import sys
produtos =[]

class View():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro de Produtos")


        self.container = tk.Frame (self.root)
        self.container.pack()

        self.createFrame1()
        self.createFrame2()

        self.frame1.grid(row=0, column=0, sticky='nsew')
        self.frame2.grid(row=0, column=0, sticky='nsew')

        #Primeiro frame a ser exibido
        self.show_frame1()

        self.root.bind('<Escape>', self.close)

        self.root.mainloop()
    

    def close(self, evento=None):
        sys.exit()

    def show_frame1(self):
        #exibi frame1
        self.frame1.tkraise()

    def show_Frame2(self):
        #exibi frame2

         for produto in produtos:
            self.texto_produtos.insert(tk.END, f"Nome: {produto.nome}\n")
            self.texto_produtos.insert(tk.END, f"Descrição: {produto.descricao}\n")
            self.texto_produtos.insert(tk.END, f"Valor: {produto.valor}\n")
            self.texto_produtos.insert(tk.END, f"Status: {produto.status}\n")
                

            self.frame2.tkraise()

    def createFrame1(self):
        self.frame1 = tk.Frame (self.container)

        self.label_nome = tk.Label(self.frame1, text="Nome:")
        self.label_nome.grid(row=0, column=0)

        self.entry_nome = tk.Entry(self.frame1)
        self.entry_nome.grid(row=0, column=1)

        self.label_descricao = tk.Label(self.frame1, text= "Descrição: ")
        self.label_descricao.grid(row=1, column=0)
        
        self.entry_descricao = tk.Entry(self.frame1)
        self.entry_descricao.grid(row=1, column=1)

        self.label_preco = tk.Label(self.frame1, text="Valor")
        self.label_preco.grid(row=2, column=0)

        self.entry_preco = tk.Entry(self.frame1)
        self.entry_preco.grid(row=2, column=1)

        self.label_status = tk.Label(self.frame1, text = "Status (sim/não): ")
        self.label_status.grid(row=3, column=0)

        self.entry_status = tk.Entry(self.frame1)
        self.entry_status.grid(row=3, column=1)

        button_Salvar = tk.Button(self.frame1, text="Salvar", command=self.salvar_produto)
        button_Salvar.grid(row=4, column=1, pady=(0,10))

        buttonTela2 = tk.Button(self.frame1, text="Próxima tela", command=self.show_Frame2)
        buttonTela2.grid(row=4, column=2, pady=(0, 11))

    

    def atualizar_preco(self):
        #irá atualizar o valor do entry_preco

        #pega o valor que o user inseriu
        preco = float(self.entry_preco.get())

        #atribui novo valor
        self.preco_var.set(str(preco))

    def salvar_produto(self):
        nome = self.entry_nome.get()
        descricao = self.entry_descricao.get()
        valor = self.entry_preco.get()
        status = self.entry_status.get()

        novo_produto = Produto(nome, descricao, valor, status)

        #armazena os produtos que foram inseridos pelo usuário na lista produtos
        produtos.append(novo_produto)


        #limpar os campos após o user salvar o produto
        self.entry_nome.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_status.delete(0, tk.END)
        

    def createFrame2(self):
        self.frame2 = tk.Frame(self.container)

        self.texto_produtos = tk.Text(self.frame2, wrap=tk.WORD, width=30, height=5)
        self.texto_produtos.grid(row=0, column=0, padx=10, pady=10)


        buttonVoltar = tk.Button(self.frame2,text= "Voltar", command=self.show_frame1)
        buttonVoltar.grid(row=4, column=2,pady=(0,10))
View()