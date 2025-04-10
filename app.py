import os

restaurantes = [{"nome":"Praça", "categoria":"Self Service", "ativo":False},
                {"nome": "Bart", "categoria": "Rodizio", "ativo":True },
                {"nome": "Olivier", "categoria": "Italiano", "ativo":True }
]

def exibir_nome_programa():
    print("𝐒𝐀𝐁𝐎𝐑 𝐄𝐗𝐏𝐑𝐄𝐒𝐒\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar restaurante ")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Finalizar app")

def voltar_menuprincipal():
    input("Digite uma tecla para voltar ao programa!")
    main()
   

def opcao_invalida():
    print("Opçao invalida!\n")
    voltar_menuprincipal()
    
    
def exibir_subtitulo(texto):
    os.system("clear")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes\n")
    nome_restaurante = input("Digite o nome do seu restaurante que deseja cadastrar: \n").strip()
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante} \n").strip()
    dados_restaurante = {"nome":nome_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append({"nome": nome_restaurante, "categoria": categoria , "ativo": False})
    
    
    voltar_menuprincipal()

def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"  # CORRIGIDO
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
        
    voltar_menuprincipal()

def ativar_restaurante():
    exibir_subtitulo("Ativando restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja ativar: \n").strip()
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante["nome"].lower() == nome_restaurante.lower():
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            status = "ativado" if restaurante["ativo"] else "desativado"
            print(f"\nO restaurante {restaurante['nome']} foi {status} com sucesso!")
            break
    if not restaurante_encontrado:
        print("O restaurante nao foi encontrado!")
    voltar_menuprincipal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: (1 a 4) "))
        
        if opcao_escolhida == 1: #se a opçao escolhida for 1 imprima 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
   # os.system("clear")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
   
    

if __name__ == "__main__": #
    main()
