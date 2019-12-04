lista_cadastro = []

def Menu():
    print('*' * 34)
    print('* 1 - Cadastrar pessoa           *')
    print('* 2 - Remover pessoa do cadastro *')
    print('* 3 - Listar cadastro            *')
    print('* 4 - Sair do programa           *')
    print('*' * 34)
    op = input('Qual opção deseja? ')
    print('\n')
    if op == '1' or op == '2' or op == '3' or op == '4':
        return int(op)
    else:
        print('Opção inválida!' , '\n')
    return -1

def fazcadastro():
    lista1 = []
    nome = input('Qual é o seu nome? ')
    nomeM = nome.title()
    idade = int(input('Informe sua idade: '))
    sexo = input('Qual o seu sexo? ')
    lista1.append(nomeM)
    lista1.append(idade)
    lista1.append(sexo)
    lista_cadastro.append(lista1)
    print('')

def listcadastro():

    for lista in lista_cadastro:
            print('nome: ', lista[0])
            print('idade: ', lista[1],'anos')
            print('sexo: ', lista[2], '\n')


def remcadastro():

    nome_procurar = input('Nome da pessoa deseja remover: ')
    idade_procurar = int(input('Idade da pessoa que você dejesa remover: '))
    sexo_procurar = input('Sexo da pessoa que você deseja remover: ')

    list_delete = [nome_procurar, idade_procurar, sexo_procurar]

    if list_delete in lista_cadastro:
        print('')
        print('Removido com sucesso!', '\n')
        return lista_cadastro.remove(list_delete)
    else:
        print('')
        print('Algo foi escrito errado! ', '\n')
    return -1

while True:
    op = Menu()
    if op == 1:
        fazcadastro()
    elif op == 2:
        remcadastro()
    elif op == 3:
        listcadastro()
    elif op == 4:
        break