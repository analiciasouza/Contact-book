contact_book = {
  'Ana' : 82999800205 ,
  'João' : 81999500987 ,
  'Carol' : 11988546702 ,
  'Thales' : 82999131401 ,
  'José' : 21994567834
}


def adicionar_contato():
    print('Adicionar Novo Contato')
    nome =  input("Insira o nome:  ")
    numero = int(input("Insira o número: "))
    contact_book.update({nome : numero})
    print(contact_book)


def deletar_contato():
    print("Deletar Contato")
    nome = input("Insira o nome do contato: ")
    del contact_book[nome]
    print(contact_book)


def editar_contato():
    print("Editar Contato")
    nomeContato = input("Insira o nome do contato que gostaria de editar: ")
    novoNumero = int(input("Insira o número novo: "))
    contact_book[nomeContato] = novoNumero
    print(contact_book)


def procurar_contato():
    print("Procurar Contato")
    searchContact = input("Procurar por Número ou Nome: ")
    if searchContact.lower() == 'nome':
        nomeContato = input("Insira o nome: ")
        print(contact_book[nomeContato])
    elif searchContact.lower() == 'numero' or 'número':
        numeroContato = int(input('Insira o número: '))
        for k, v in contact_book.items():  # IMPORTANTE
            if numeroContato == v:
               print(k)


print('''Insira: \n
1 - Adicionar Contato
2 - Deletar Contato
3- Editar Contato
4 - Procurar Contato
5 - Sair''')
    
user_command  = ' '

while user_command != 5:
    user_command = int(input(">> "))
    if user_command == 1:
        adicionar_contato()
    elif user_command == 2:
        deletar_contato()
    elif user_command == 3:
        editar_contato()
    elif user_command == 4:
        procurar_contato()
    else:
        print("Valor Inválido!!")
