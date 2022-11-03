# -> Utilizando o algoritmo FIFO dentro do contexto de um atendimento de uma fila de clientes

fila = list(range(1, 11))
atendidos = []
trabalhando = True

while trabalhando:
    print(f'Existem {len(fila)} cliente(s) na fila')
    
    if len(fila) == 0:
        print(f'Expediente terminado! Você atendeu um total de {len(atendidos)} clientes hoje. Bom trabalho! :)')
        trabalhando = False
    else:
        atendimento = input('Deseja atender um cliente? (S/N): ')
        atendimento.lower()

        if atendimento == 's':
            atendidos.append(fila.pop(0))
            print('Cliente atendido com sucesso!')
        elif atendimento == 'n':
            print('Nenhum cliente atendido no momento...')
        else:
            print('Ops... Não entendi.')