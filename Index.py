class Usuario:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class ContaBancaria:
    LIMITE_SAQUES = 3

    def __init__(self, numero, cpf_titular, saldo_inicial=0, limite=500):
        self.numero = numero
        self.cpf_titular = cpf_titular
        self.saldo = saldo_inicial
        self.limite = limite
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            return True
        return False

    def sacar(self, valor):
        if valor <= 0:
            return "O valor informado é inválido."
        if valor > self.saldo:
            return "Você não tem saldo suficiente."
        if valor > self.limite:
            return "O valor do saque excede o limite."
        if self.numero_saques >= ContaBancaria.LIMITE_SAQUES:
            return "Número máximo de saques excedido."

        self.saldo -= valor
        self.extrato += f"Saque: R$ {valor:.2f}\n"
        self.numero_saques += 1
        return True

    def exibir_extrato(self):
        return f"\n================ EXTRATO ================\n" + \
               ("Não foram realizadas movimentações.\n" if not self.extrato else self.extrato) + \
               f"\nSaldo: R$ {self.saldo:.2f}\n" + \
               "=========================================="

def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Novo Usuário
    [c] Nova Conta
    [q] Sair

    => """
    return input(menu).lower()

def cadastrar_usuario(clientes):
    cpf = input("Informe o CPF (somente números): ")
    if not cpf.isdigit() or len(cpf) != 11 or any(c.cpf == cpf for c in clientes):
        print("CPF inválido ou já cadastrado.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    cliente = Usuario(cpf, nome, data_nascimento, endereco)
    clientes.append(cliente)
    print("Usuário cadastrado com sucesso!")

def cadastrar_conta(contas, clientes):
    cpf = input("Informe o CPF do titular da conta: ")
    if not any(c.cpf == cpf for c in clientes):
        print("Cliente não encontrado. Cadastre o usuário primeiro.")
        return

    numero_conta = len(contas) + 1
    conta = ContaBancaria(numero_conta, cpf)
    contas.append(conta)
    print("Conta bancária cadastrada com sucesso!")

def buscar_conta_por_cpf(contas, cpf):
    return next((conta for conta in contas if conta.cpf_titular == cpf), None)

def main():
    clientes = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            cpf = input("Informe o CPF do titular da conta: ")
            conta = buscar_conta_por_cpf(contas, cpf)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                if conta.depositar(valor):
                    print("Depósito realizado com sucesso!")
                else:
                    print("Operação falhou! O valor informado é inválido.")
            else:
                print("Conta não encontrada.")

        elif opcao == "s":
            cpf = input("Informe o CPF do titular da conta: ")
            conta = buscar_conta_por_cpf(contas, cpf)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                resultado = conta.sacar(valor)
                if resultado == True:
                    print("Saque realizado com sucesso!")
                else:
                    print(f"Operação falhou! {resultado}")
            else:
                print("Conta não encontrada.")

        elif opcao == "e":
            cpf = input("Informe o CPF do titular da conta: ")
            conta = buscar_conta_por_cpf(contas, cpf)
            if conta:
                print(conta.exibir_extrato())
            else:
                print("Conta não encontrada.")

        elif opcao == "n":
            cadastrar_usuario(clientes)

        elif opcao == "c":
            cadastrar_conta(contas, clientes)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
