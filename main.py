contact_book = { }


def adicionar_contato():
    print('Adicionar Novo Contato')
    nome =  input("Insira o nome:  ")
    numero = int(input("Insira o número: "))
    numeros = []
    numeros.append(numero)
    contact_book.update({nome : numeros})
    

def incluir_numero():
    nome = input("Insira o nome o contato: ")
    if nome in contact_book:
        numero = int(input("Insira novo número: "))
        contact_book[nome].append(numero)
    else:
        print('Esse contato não está na agenda')


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
4- Incluir Telefone
5 - Procurar Contato
6 - Sair''')
    
user_command  = ' '

while user_command != 6:
    user_command = int(input(">> "))
    if user_command == 1:
        adicionar_contato()
    elif user_command == 2:
        deletar_contato()
    elif user_command == 3:
        editar_contato()
    elif user_command == 4:
        incluir_numero()
    elif user_command == 5:
        procurar_contato()
    else:
        print("Valor Inválido!!")
