import time
import datetime
import json
rodando = True

# DEF DA CAIXA PARA MELHORAR VISUALIZAÇÃO (FEITO EXCLUSIVAMENTE POR IA)
def super_caixa(texto):
    linhas = texto.split('\n')
    largura = max(len(l) for l in linhas) + 4
    print("┏" + "━" * (largura - 2) + "┓")
    for l in linhas:
        print(f"│{l.center(largura - 2)}│")
    print("┗" + "━" * (largura - 2) + "┛")

# COMANDO ABOUT
def mostrarSobre():
    texto = """Gestor de Projetos
O projeto foi criado exclusivamente para um trabalho universitário. O gestor de projetos
foi feito com a finalidade de auxiliar no armazenamento e organização de ideias, onde você
poderá guardar sem se preocupar em perder nenhum arquivo. Dito isso, não se preocupe em perder
projetos quando encerrar o programa.

Este projeto foi iniciado no dia 23/03/2026 e a primeira versão estável foi finalizada
no dia 01/05/2026
Créditos: Julio Ormundo"""

    super_caixa(texto)
    print(f"Considere ler o README em: https://github.com/julioormundo/Gestor_de_Projetos")
    input("Pressione ENTER para continuar")
    time.sleep(1)

# COMANDO LIST
def listarProjetos(lista):
    if not lista:
        super_caixa("Você não possui nenhum projeto salvo.")
    else:
        for projeto in lista:
            print('\nNome:', projeto["nome"])
            print('Descrição:', projeto["descricao"])
            print('Status:', projeto["status"])
            print('Data:', projeto["criacao"])
    input("\nPressione ENTER para continuar")
    time.sleep(1)

# COMANDO QUIT
def sair_do_programa():
    time.sleep(1)
    super_caixa("Até logo\nSaindo do programa...")
    time.sleep(2)
    return False

# COMANDO ADD
def adicionarProjetos(lista_recebida):
    try:
        quantidade_projetos = int(input("Informe a quantidade de projetos que quer adicionar >>> "))
        if quantidade_projetos <= 0:
            print("Quantidade de projetos inválida.")
        else:
            for projeto in range(quantidade_projetos):
                achou_projeto = False
                nome_projeto = input("Qual será o nome do projeto? >>> ")
                for projeto_dicionario in projetos:
                    if projeto_dicionario['nome'].lower() == nome_projeto.lower():
                        print("ERRO: Já existe um projeto salvo com este nome.")
                        achou_projeto = True
                        break
                if not achou_projeto:
                    if not nome_projeto:
                        print("ERRO: Você não pode criar um arquivo sem nome.")
                    else:
                        descricao = input("Qual será a descrição do projeto >>> ")
                        status = input("Status (Em andamento / Concluído) >>> ").upper()
                        if not status:
                            print("Você não pode criar um arquivo sem mencionar o status.")
                        else:
                            projetos_dicionario = {
                                "nome": nome_projeto,
                                "descricao": descricao,
                                "status": status,
                                "criacao": datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')
                            }
                            lista_recebida.append(projetos_dicionario)
                            super_caixa(f"O projeto '{nome_projeto}' foi cadastrado com sucesso.\nData de criação: {projetos_dicionario['criacao']}")

        time.sleep(2)
    except ValueError:
        print("Ops! Parece que você digitou um caractere inválido.")
        input("Pressione ENTER para tentar novamente.")

# COMANDO DELETAR PROJETO
def deletarProjeto(lista_projetos):
    if not lista_projetos:
        super_caixa("Você não possui nenhum projeto salvo.")
    else:
        super_caixa("--- Projetos Cadastrados ---")
        for projeto in projetos:
            print(f"- {projeto['nome']}")
            print("----------------------------")

        deletar_projeto = input("Digite o nome do projeto que deseja deletar. (Digite 'all' para apagar todos) >>> ").lower()
        achou_projeto = False
        if deletar_projeto == "all":
            lista_projetos.clear()
            achou_projeto = True
            super_caixa("Todos os projetos foram apagados com sucesso...")
        for projeto in projetos:
            if projeto["nome"].lower() == deletar_projeto:
                lista_projetos.remove(projeto)
                time.sleep(1)
                super_caixa(f"O projeto '{deletar_projeto}' foi deletado com sucesso...")
                achou_projeto = True
                break
        if not achou_projeto:
            super_caixa("Seu projeto não foi encontrado...")
            input("Pressione ENTER para continuar")
    time.sleep(1)

# COMANDO ATUALIZAR PROJETO EXISTENTE
def atualizarProjetos(lista_projetos):
    if not lista_projetos:
        super_caixa("Você não possui nenhum projeto salvo.")
    else:
        time.sleep(1)
        super_caixa("--- Projetos Cadastrados ---")
        for projeto in projetos:
            print(f"* {projeto['nome']}")
            print("-------------------")
        atualizar_projeto = input("Digite o nome do projeto que deseja atualizar. \n>>> ")
        achou_projeto = False
        for projeto in projetos:
            if projeto["nome"].lower() == atualizar_projeto.lower():
                achou_projeto = True
                acao_usuario = input("O que deseja atualizar? (nome, descrição, status) >>> ").lower()
                if acao_usuario == "nome":
                    novo_nome_projeto = input("Digite o novo nome do projeto >>> ")
                    if not novo_nome_projeto:
                        print("ERRO: Você não pode deixar seu arquivo sem nome.")
                    else:
                        projeto["nome"] = novo_nome_projeto
                        super_caixa(f"O nome do projeto foi atualizado para '{novo_nome_projeto}'.")
                        projeto["criacao"] = datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')
                        break
                elif acao_usuario in ["descrição", "descricao", "descriçao", "descricão"]:
                    nova_descricao_projeto = input("Digite a nova descrição do projeto >>> ")
                    projeto["descricao"] = nova_descricao_projeto
                    super_caixa(f"A descrição do projeto '{atualizar_projeto}' foi atualizado para '{nova_descricao_projeto}'.")
                    projeto["criacao"] = datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')
                    break
                elif acao_usuario == "status":
                    try:
                        novo_status_projeto = int(input("Você finalizou seu projeto? (1 para sim, 2 para não) >>> "))
                        if novo_status_projeto == 1:
                            projeto["status"] = "CONCLUÍDO"
                            super_caixa(f"O status do projeto '{atualizar_projeto}' foi atualizado para '{projeto['status']}'.")
                            projeto["criacao"] = datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')
                            break
                        elif novo_status_projeto == 2:
                            projeto["status"] = "EM ANDAMENTO"
                            super_caixa(f"O status do projeto '{atualizar_projeto}' foi atualizado para '{projeto['status']}'.")
                            projeto["criacao"] = datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')
                            break
                        else:
                            print("Ops! Parece que você digitou um número inválido.")
                            input("Pressione ENTER para tentar novamente.")
                    except ValueError:
                        print("Ops! Parece que você digitou um caractere inválido.")
                        input("Pressione ENTER para tentar novamente.")
        if not achou_projeto:
            super_caixa("Não foi possível achar seu projeto, tenha certeza de que digitou corretamente.")
    input("\nPressione ENTER para continuar")
    time.sleep(1)

# CARREGAR DADOS
def carregarDados():
    try:
        with open("SaveArchives.json", "r") as arquivo:
            projetos_lista = json.load(arquivo)
    except FileNotFoundError:
        print("Você ainda não tem arquivos salvos ou eles não foram encontrados.")
        projetos_lista = []
    except json.JSONDecodeError:
        print("Parece que seu(s) arquivo(s) estão vazios ou corrompidos.")
        projetos_lista = []
    return projetos_lista

# SALVAR DADOS
def salvarDados(lista_projetos):
    with open("SaveArchives.json", "w") as arquivo:
        json.dump(lista_projetos, arquivo, indent=4)

# COMANDO ESTATÍSTICAS
def mostrarEstatisticas(lista):
    concluidos = 0
    em_andamento = 0
    data_ultimo = "Nenhum projeto finalizado."
    for projeto in lista:
        if projeto['status'] in ["CONCLUIDO", "CONCLUÍDO", "CONCLUIDA", "CONCLUÍDA"]:
            concluidos += 1
            data_ultimo = projeto['criacao']
        elif projeto['status'] == "EM ANDAMENTO":
            em_andamento += 1
    print(f"Você possui {concluidos} projetos concluídos e {em_andamento} projetos em andamento.")
    if data_ultimo == "Nenhum projeto finalizado.":
        print(data_ultimo)
    else:
        print(f"{data_ultimo} foi o último dia em que você finalizou um projeto.")
    input("\nPressione ENTER para continuar.")
    time.sleep(1)

# COMANDO PROCURAR
def procurarProjeto(lista):
    while True:
        usuario_buscando = input("Qual projeto está procurando? (Digite 'quit' para voltar)\n>>> ").lower()
        if usuario_buscando.lower() == "quit":
            print("Voltando para a tela anterior...")
            time.sleep(1)
            break
        achou_projeto = False
        for projeto in lista:
            if usuario_buscando.lower() in projeto['nome'].lower():
                super_caixa(f"Nome: {projeto['nome']}\nDescrição: {projeto['descricao']}\nStatus Atual: {projeto['status']}")
                achou_projeto = True
        if achou_projeto:
            input("Pressione ENTER para continuar")
            time.sleep(1)
            break
        else:
            super_caixa("Não foi encontrado nenhum projeto com esse nome.")

# Lista para o armazenamento dos projetos
projetos = carregarDados()

# Solicitar ao usuário um comando e armazenar
while rodando:
    cmd = input("""
╭──────────────────────────╮
│         COMANDOS         │
├──────────────────────────┤
│ ABOUT                    │
│ ADD                      │
│ LIST                     │
│ UPDATE                   │
│ DELETE                   │
│ STATS                    │
│ SEARCH                   │
│ QUIT                     │
╰──────────────────────────╯
>>> """).upper()

    # Comandos
    if cmd in ["ABOUT", "SOBRE"]:
        mostrarSobre()

    elif cmd in ["QUIT", "SAIR"]:
        salvarDados(projetos)
        rodando = sair_do_programa()

    elif cmd in ["ADD", "ADICIONAR"]:
        adicionarProjetos(projetos)
        salvarDados(projetos)

    elif cmd in ["LIST", "LISTA", "PROJETOS"]:
        listarProjetos(projetos)

    elif cmd in ["UPDATE", "ATUALIZAR", "UPD"]:
        atualizarProjetos(projetos)
        salvarDados(projetos)

    elif cmd in ["DEL", "DELETE", "REMOVE", "DELETAR", "DELETA"]:
        deletarProjeto(projetos)
        salvarDados(projetos)

    elif cmd == "STATS":
        mostrarEstatisticas(projetos)

    elif cmd in ["SEARCH", "PROCURAR"]:
        procurarProjeto(projetos)

    else:
        print("O comando não foi reconhecido. Tente novamente.")
        time.sleep(1)