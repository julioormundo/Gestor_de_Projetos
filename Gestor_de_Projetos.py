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
    texto = """
    🚀 Gestor de Projetos | v1.0.0
    -------------------------------------------
    Desenvolvido para organizar suas ideias e 
    potencializar sua produtividade acadêmica.

    Os dados são salvos automaticamente para 
    garantir que seu progresso esteja sempre seguro.

    Data de Lançamento: 03/05/2026
    Desenvolvedor: Julio Ormundo
    """
    super_caixa(texto)
    print(f"Considere ler o README em: https://github.com/julioormundo/Gestor_de_Projetos")
    input("Pressione ENTER para continuar")
    time.sleep(1)

# COMANDO LIST
def listarProjetos(lista):
    if not lista:
        super_caixa("Sua lista está vazia no momento. Que tal começar um novo projeto?")
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
    super_caixa("Até logo! Encerrando o programa...")
    time.sleep(2)
    return False

# COMANDO ADD
def adicionarProjetos(lista_recebida):
    try:
        quantidade_projetos = int(input("Quantidade de projetos que deseja adicionar >>> "))
        if quantidade_projetos <= 0:
            print("Ops! O valor deve ser um número inteiro superior a zero.")
        elif quantidade_projetos > 5:
            print("Ops! Por segurança, você só pode adicionar entre 1 e 5 projetos por vez.")
        else:
            for projeto in range(quantidade_projetos):
                achou_projeto = False
                nome_projeto = input("Defina o nome do projeto >>> ")
                for projeto_dicionario in projetos:
                    if projeto_dicionario['nome'].lower() == nome_projeto.lower():
                        print("Este nome já está em uso. Que tal tentar um nome diferente?")
                        achou_projeto = True
                        break
                if not achou_projeto:
                    if not nome_projeto:
                        print("Ops! O nome do projeto não pode ficar em branco.")
                    else:
                        descricao = input("Qual será a descrição do projeto? >>> ")
                        status = input("Status atual? (Em andamento / Concluído) >>> ").upper()
                        if not status:
                            print("Ops! Você precisa definir um status para o projeto.")
                        else:
                            projetos_dicionario = {
                                "nome": nome_projeto,
                                "descricao": descricao,
                                "status": status,
                                "criacao": datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')
                            }
                            lista_recebida.append(projetos_dicionario)
                            super_caixa(f"Pronto! O projeto '{nome_projeto}' foi salvo com sucesso.\nData de criação: {projetos_dicionario['criacao']}")
        time.sleep(2)
    except ValueError:
        print("Ops! Você digitou um valor inválido. Use apenas números inteiros.")
        input("Pressione ENTER para tentar novamente.")

# COMANDO DELETAR PROJETO
def deletarProjeto(lista_projetos):
    if not lista_projetos:
        super_caixa("Sua lista está vazia no momento. Não há o que deletar.")
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
            super_caixa("Feito! Todos os projetos foram removidos da sua lista.")
        for projeto in projetos:
            if projeto["nome"].lower() == deletar_projeto:
                lista_projetos.remove(projeto)
                time.sleep(1)
                super_caixa(f"Feito! O projeto '{deletar_projeto}' foi removido da sua lista.")
                achou_projeto = True
                break
        if not achou_projeto:
            super_caixa("Não encontramos nenhum projeto com esse nome. Verifique a digitação e tente de novo.")
            input("Pressione ENTER para continuar")
    time.sleep(1)

# COMANDO ATUALIZAR PROJETO EXISTENTE
def atualizarProjetos(lista_projetos):
    if not lista_projetos:
        super_caixa("Sua lista está vazia no momento.")
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
                        print("Ops! O nome do projeto não pode ficar em branco.")
                    else:
                        projeto["nome"] = novo_nome_projeto
                        super_caixa(f"Alteração realizada! O nome foi atualizado para '{novo_nome_projeto}'.")
                        projeto["criacao"] = datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')
                        break
                elif acao_usuario in ["descrição", "descricao", "descriçao", "descricão"]:
                    nova_descricao_projeto = input("Digite a nova descrição do projeto >>> ")
                    projeto["descricao"] = nova_descricao_projeto
                    super_caixa(f"Alteração realizada! A descrição foi atualizada.")
                    projeto["criacao"] = datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')
                    break
                elif acao_usuario == "status":
                    try:
                        novo_status_projeto = int(input("Você finalizou seu projeto? (1 para sim, 2 para não) >>> "))
                        if novo_status_projeto == 1:
                            projeto["status"] = "CONCLUÍDO"
                            super_caixa(f"Alteração realizada! O status foi atualizado para '{projeto['status']}'.")
                            projeto["criacao"] = datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')
                            break
                        elif novo_status_projeto == 2:
                            projeto["status"] = "EM ANDAMENTO"
                            super_caixa(f"Alteração realizada! O status foi atualizado para '{projeto['status']}'.")
                            projeto["criacao"] = datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')
                            break
                        else:
                            print("Ops! Você digitou um número inválido.")
                            input("Pressione ENTER para tentar novamente.")
                    except ValueError:
                        print("Ops! Você digitou um valor inválido.")
                        input("Pressione ENTER para tentar novamente.")
        if not achou_projeto:
            super_caixa("Não encontramos nenhum projeto com esse nome. Verifique a digitação e tente de novo.")
    input("\nPressione ENTER para continuar")
    time.sleep(1)

# CARREGAR DADOS
def carregarDados():
    try:
        with open("SaveArchives.json", "r") as arquivo:
            projetos_lista = json.load(arquivo)
    except FileNotFoundError:
        print("Bem-vindo! Nenhum salvamento encontrado. Iniciando um novo banco de dados local.")
        projetos_lista = []
    except json.JSONDecodeError:
        print("Aviso: O arquivo de salvamento parece corrompido ou vazio. Iniciando do zero.")
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
    data_atual_objeto = "Nenhum projeto finalizado."
    salvar_data = None
    for projeto in lista:
        if projeto['status'] in ["CONCLUIDO", "CONCLUÍDO", "CONCLUIDA", "CONCLUÍDA"]:
            concluidos += 1
            data_atual_objeto = datetime.datetime.strptime(projeto['criacao'], '%d/%m/%Y às %H:%M')
            if salvar_data is None or data_atual_objeto > salvar_data:
                salvar_data = data_atual_objeto
        elif projeto['status'] == "EM ANDAMENTO":
            em_andamento += 1
    print(f"Você possui {concluidos} projetos concluídos e {em_andamento} projetos em andamento.")
    if data_atual_objeto == "Nenhum projeto finalizado.":
        print("Ainda não há projetos finalizados para exibir datas.")
    else:
        print(f"Sua última conquista foi em: {salvar_data.strftime('%d/%m/%Y às %H:%M')}")
    input("\nPressione ENTER para continuar.")
    time.sleep(1)

# COMANDO PROCURAR
def procurarProjeto(lista):
    while True:
        usuario_buscando = input("Qual projeto está procurando? (Digite 'sair' para voltar)\n>>> ").lower()
        if usuario_buscando.lower() in ["quit", 'sair']:
            print("Voltando para a tela anterior...")
            time.sleep(1)
            break
        achou_projeto = False
        for projeto in lista:
            if usuario_buscando.lower() in projeto['nome'].lower():
                super_caixa(
                    f"Nome: {projeto['nome']}\nDescrição: {projeto['descricao']}\nStatus Atual: {projeto['status']}")
                achou_projeto = True
        if achou_projeto:
            input("Pressione ENTER para continuar")
            time.sleep(1)
            break
        else:
            super_caixa("Não encontramos nenhum projeto com esse nome. Verifique a digitação e tente de novo.")

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
        print("Ops! Comando não reconhecido. Escolha uma das opções do menu acima.")
        time.sleep(1)