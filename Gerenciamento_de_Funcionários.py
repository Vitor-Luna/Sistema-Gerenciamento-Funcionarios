print("Bem-vindos à empresa ...")
lista_funcionarios = []
id_global = 12345678 

def cadastrar_funcionario(id):
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    while True:
        try:
            salario = float(input("Digite o salário do funcionário: "))
            break
        except ValueError:
            print("Salário inválido. Por favor, insira um valor numérico.")
    funcionario = {"id": id, "nome": nome, "setor": setor, "salario": salario}
    lista_funcionarios.append(funcionario)
    print(f"Funcionário {nome} cadastrado com sucesso!")

def consultar_funcionarios():
    if not lista_funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    while True:
        opcao = input("1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Setor\n4. Retornar ao menu\nEscolha: ")
        if opcao == "1":
            for func in lista_funcionarios:
                print(f"ID: {func['id']}, Nome: {func['nome']}, Setor: {func['setor']}, Salário: R${func['salario']:.2f}")
        elif opcao == "2":
            id_consulta = int(input("Digite o id do funcionário: "))
            for func in lista_funcionarios:
                if func["id"] == id_consulta:
                    print(f"ID: {func['id']}, Nome: {func['nome']}, Setor: {func['setor']}, Salário: R${func['salario']:.2f}")
                    break
            else:
                print("Funcionário não encontrado.")
        elif opcao == "3":
            setor_consulta = input("Digite o setor: ")
            funcionarios_encontrados = [func for func in lista_funcionarios if func["setor"] == setor_consulta]
            if funcionarios_encontrados:
                for func in funcionarios_encontrados:
                    print(f"ID: {func['id']}, Nome: {func['nome']}, Setor: {func['setor']}, Salário: R${func['salario']:.2f}")
            else:
                print("Nenhum funcionário encontrado nesse setor.")
        elif opcao == "4":
            return
        else:
            print("Opção inválida. Tente novamente.")

def remover_funcionario():
    id_remocao = int(input("Digite o id do funcionário a ser removido: "))
    for func in lista_funcionarios:
        if func["id"] == id_remocao:
            lista_funcionarios.remove(func)
            print("Funcionário removido com sucesso.")
            return
    print("Id inválido. Tente novamente.")

while True:
    opcao = input("1. Cadastrar Funcionário\n2. Consultar Funcionário\n3. Remover Funcionário\n4. Encerrar Programa\nEscolha: ")
    if opcao == "1":
        id_global += 1
        cadastrar_funcionario(id_global)
    elif opcao == "2":
        consultar_funcionarios()
    elif opcao == "3":
        remover_funcionario()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
