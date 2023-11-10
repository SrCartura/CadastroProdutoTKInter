from Model import Produto
produtos = []

def criar_produto():
    nome = input("Nome do Produto: ")
    descricao = input("Descrição: ")
    valor = float   (input("Valor: "))
    status = input("Disponível para venda? (sim/não): ").lower() == "sim" #para que não de erro caso o usuário digitar "SIM"

    novo_produto = {
        "nome": nome,
        "descrição": descricao,
        "valor": valor,
        "status": status
    }
    produtos.append(novo_produto)
    print("Produto cadastrado com Sucesso!")


def valor_ordenado(produto):
    return produto["valor"]


def listar_produtos():
    produtos_ordenados = sorted(produtos, key = valor_ordenado)
    print("\nListagem de Produtos: ")
    for produto in produtos_ordenados:
        disponivel = "sim" if  produto["status"] else "não"
        print(f"Nome: {produto['nome']}, Valor: R$ {produto['valor']:.2f}, Disponível para venda: {disponivel}")

if __name__ == "__main__":
    while True:

        print("\n Opções:")
        print("1. Novo Produto")
        print("2. Listar Produtos")
        print("3. Fechar")
    
        opcao = input("Escolha uma opção: ")
        
        
        if opcao == "1":
            criar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            break
        else:
            print("Opção inválida")
