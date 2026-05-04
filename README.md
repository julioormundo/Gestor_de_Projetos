# 💡 Gestor de Projetos e Ideias (CLI)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📝 Sobre o Projeto
Este é um sistema de gerenciamento de ideias desenvolvido como projeto prático acadêmico. O objetivo da aplicação é aplicar e consolidar fundamentos essenciais de lógica de programação em Python.

Diferente de scripts básicos que perdem as informações ao serem fechados, este sistema possui **persistência de dados**, salvando automaticamente todos os projetos do usuário em um arquivo `.json` local.

## ✨ Principais Funcionalidades
* **CRUD Completo:** Criação, leitura, atualização e exclusão de projetos.
* **Persistência de Dados:** Salvamento e carregamento automático usando a biblioteca `json`.
* **Tratamento de Exceções:** Sistema à prova de falhas básicas de digitação do usuário (uso de blocos `try/except`).
* **Flexibilidade de Idioma:** Os comandos podem ser acionados tanto em Inglês quanto em Português.

## 🕹️ Comandos Disponíveis
O programa funciona através de uma Interface de Linha de Comando (CLI). Ao executar o script, você pode utilizar os seguintes comandos:

* **`ADD`** (ou `ADICIONAR`): Cadastra um ou múltiplos projetos, definindo nome, descrição e status (Em andamento / Concluído).
* **`LIST`** (ou `PROJETOS`): Exibe no terminal todos os projetos cadastrados com suas respectivas datas de criação.
* **`UPDATE`** (ou `ATUALIZAR`): Permite editar o nome, descrição ou status de um projeto já existente.
* **`SEARCH`** (ou `PROCURAR`): Sistema de busca para encontrar um projeto específico pelo nome.
* **`STATS`**: Gera um relatório automático com a contagem de projetos em andamento/concluídos e a data da última finalização.
* **`ABOUT`** (ou `SOBRE`): Exibe os créditos e informações detalhadas da versão.
* **`QUIT`** (ou `SAIR`): Salva todas as alterações no arquivo JSON e encerra o sistema com segurança.

> 💡 **Dica - Exclusão em Massa:** O comando **`DELETE`** (ou `DEL`) remove um projeto específico. Porém, caso queira resetar seu gestor, basta digitar `DEL` e, em seguida, a palavra `all` para apagar todos os registros de uma vez.

## 🚀 Como Executar na Sua Máquina

1. Certifique-se de ter o [Python](https://www.python.org/) instalado em seu computador.
2. Faça o clone deste repositório ou baixe o arquivo principal.
3. Abra o terminal na pasta onde o arquivo está salvo.
4. Execute o comando abaixo:
   ```bash
   python Gestor_de_Projetos.py
