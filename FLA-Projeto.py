lista_cadastro = []

def Menu():
     print('Qual opção deseja?')
     print('1 - Cadastrar pessoa.')
     print('2 - Remover pessoa do cadastro.')
     print('3 - Listar cadastro.')
     print('4 - Sair do programa.')
     ca = input()
     if ca == '1' or ca == '2' or ca == '3' or ca == '4':
         return int(ca)
     else:
         print('Opção inválida!')
     return -1

def fazcadastro():
     lista1 = []
     nome = input('Qual é o seu nome?')
     idade = int(input('Informe sua idade:'))
     sexo = input('Qual o seu sexo?')
     lista1.append(nome)
     lista1.append(idade)
     lista1.append(sexo)
     lista_cadastro.append(lista1)
     print('')

def listcadastro():

    for lista in lista_cadastro:
        for ll in lista:
            print(ll)


def remcadastro():

     nome_procurar = input('Nome da pessoa deseja remover: ')
     idade_procurar = int(input('Idade da pessoa que você dejesa remover: '))
     sexo_procurar = input('Sexo da pessoa que você deseja remover: ')

     list_delete = [nome_procurar, idade_procurar, sexo_procurar]

     lista_cadastro.remove(list_delete)

     print('')

while True:
    ca = Menu()
    if ca == 1:
        fazcadastro()
    elif ca == 2:
        remcadastro()
    elif ca == 3:
        listcadastro()
    elif ca == 4:
        break