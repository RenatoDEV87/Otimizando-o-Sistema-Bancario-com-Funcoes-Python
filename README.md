# Desafio Nível Avançado: Otimizando o Sistema Bancário com Funções Python

Este projeto é uma otimização de um sistema bancário simples, utilizando funções e classes em Python para criar, gerenciar usuários e contas bancárias, além de permitir operações de depósito, saque e exibição de extrato.

## Funcionalidades

- Cadastro de novos usuários (clientes)
- Cadastro de novas contas bancárias
- Depósito em conta bancária
- Saque de conta bancária
- Exibição de extrato bancário
- Validação de entradas (CPF, valores de transações)

## Estrutura do Código

O código está organizado da seguinte forma:

### Classes

- **Usuario**: Representa um cliente do banco.
- **ContaBancaria**: Representa uma conta bancária com métodos para depósito, saque e exibição de extrato.

### Funções

- **exibir_menu**: Exibe o menu principal e retorna a opção escolhida pelo usuário.
- **cadastrar_usuario**: Cadastra um novo cliente.
- **cadastrar_conta**: Cadastra uma nova conta bancária.
- **buscar_conta_por_cpf**: Busca uma conta bancária pelo CPF do titular.
- **main**: Função principal que gerencia o loop do programa e as operações baseadas nas escolhas do usuário.

## Requisitos

- Python 3.x

## Como Executar

1. Clone este repositório para sua máquina local.
2. Navegue até o diretório onde o arquivo `sistema_bancario.py` está localizado.
3. Execute o arquivo `sistema_bancario.py` com Python:

```bash
python sistema_bancario.py
```

## Exemplo de Uso

```bash
[d] Depositar
[s] Sacar
[e] Extrato
[n] Novo Usuário
[c] Nova Conta
[q] Sair

=> n
Informe o CPF (somente números): 12345678901
Informe o nome completo: João Silva
Informe a data de nascimento (dd/mm/aaaa): 01/01/1990
Informe o endereço (logradouro, número - bairro - cidade/estado): Rua A, 123 - Centro - Rio de Janeiro/RJ
Usuário cadastrado com sucesso!

[d] Depositar
[s] Sacar
[e] Extrato
[n] Novo Usuário
[c] Nova Conta
[q] Sair

=> c
Informe o CPF do titular da conta: 12345678901
Conta bancária cadastrada com sucesso!

[d] Depositar
[s] Sacar
[e] Extrato
[n] Novo Usuário
[c] Nova Conta
[q] Sair

=> d
Informe o CPF do titular da conta: 12345678901
Informe o valor do depósito: 500
Depósito realizado com sucesso!

[d] Depositar
[s] Sacar
[e] Extrato
[n] Novo Usuário
[c] Nova Conta
[q] Sair

=> e
Informe o CPF do titular da conta: 12345678901

================ EXTRATO ================
Depósito: R$ 500.00

Saldo: R$ 500.00
==========================================
```
## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
