import os
import sys

restaurantes = [{'nome': 'Praça do Sushi', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Pizza  Suprema', 'categoria': 'Italiano', 'ativo': True},
                {'nome': 'Cantina da Vó', 'categoria': 'Salgados', 'ativo': True}]

def exibir_nome_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante.')
    print('2. Listar restaurantes.')
    print('3. Alternar estado do restaurante.')
    print('4. Sair.\n')

def exibir_subtítulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def reseta_menu():
    input('\nPressione qualquer tecla para voltar ao menu')
    main()

def cadastrar_novo_restaurante():
    exibir_subtítulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    reseta_menu()

def listar_restaurantes():
    exibir_subtítulo('Listando os restaurantes\n')
    print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(10)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(10)} | {ativo}')
    reseta_menu()

def alternar_estado_restaurante():
    exibir_subtítulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')
    reseta_menu()

def main():
    exibir_nome_programa()
    exibir_opcoes()

    opcao_escolhida = input('Escolha uma opção: ')
        
    if opcao_escolhida.isdigit():
        opcao_escolhida = int(opcao_escolhida)
            
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            print('Finalizar o programa.')
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            sys.exit()
        else:
            print('Erro. Selecione um número de 1 a 4.')
    else:
        print('Erro. Insira um número válido.')

if __name__ == '__main__':
    main()