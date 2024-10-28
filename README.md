# Sistema de Gerenciamento de Funcionários

## Preview
Bem-vindo ao sistema de gerenciamento de funcionários, que permite cadastrar, consultar e remover funcionários de uma empresa.

## Funcionalidades
- **Cadastrar Funcionário**: Insira o nome, setor e salário do funcionário.
- **Consultar Funcionário**: Consulte todos os funcionários, por ID ou por setor.
- **Remover Funcionário**: Remova um funcionário pelo ID.

## Código
Aqui está uma visão geral do código principal. Para ver o código completo, acesse o arquivo [main.py](https://github.com/Vitor-Luna/Sistema-Gerenciamento-Funcionarios/blob/main/Gerenciamento_de_Funcion%C3%A1rios.py).

```python
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

# Exemplo de como chamar a função
id_global += 1
cadastrar_funcionario(id_global)
