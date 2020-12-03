import os

def menu():
    os.system('clear')

    print('+=======+============================+')
    print('| OPÇÃO |          ALGORITMO         |')
    print('+=======+============================+')
    print('|   1   |    FIFO                    |')
    print('+-------+----------------------------+')
    print('|   2   |    SJF (SEM PREEMPÇÃO)     |')
    print('+-------+----------------------------+    [TECLE  QUALQUER OUTRA ENTRADA PARA SAIR]')
    print('|   3   |    SJF (COM PREEMPÇÃO)     |')
    print('+-------+----------------------------+')
    print('|   4   |    ALGOTITMO PRIORIDADE    |')
    print('+-------+----------------------------+')
    print('|   5   |    ROUND ROBIN (QUANTUM)   |')
    print('+-------+----------------------------+')


def insert_process(params):
    params['option'] = int(input('Informe a opção desejada: '))
    
    os.system('clear')
    if params['option'] == 1:
        print('================FIFO================')
    elif params['option'] == 2:
        print('================SJF (SEM PREEMPÇÃO)================')
    elif params['option'] == 3:
        print('================SJF (COM PREEMPÇÃO)================')
    elif params['option'] == 4:
        print('================ALGOTITMO PRIORIDADE================')
    elif params['option'] == 5:
        print('================ROUND ROBIN (QUANTUM)================')
    else:
        return 0

    params['qt_process'] = input('Informe a quantidade de processos: ')

    for i in range(int(params['qt_process'])):
        print(f'P{i+1}:')

        exec_time = int(input('    Tempo de execução: '))
        start_time = int(input('    Instante de chegada: '))
        print(' ')

        params['process'].append({
            'exec_time': exec_time,
            'start_time': start_time,
            'waiting_time': 0,
            'turnaround': 0,
            'priority':-1,
            'exec': []
        })

    return params


def sort_by_start_time(process):
    for i in range(0,len(process)): 
        key = process[i]['start_time']
        j = i-1
        while j >= 0 and key < process[j]['start_time']: 
            process[j + 1]['start_time'] = process[j]['start_time'] 
            j -= 1
        process[j + 1]['start_time'] = key 
    
    return process


def fifo(params):
    params['process'] = sort_by_start_time(params['process'])

    print(params['process'])


def main():
    params = {
        'option': -1,
        'qt_process': 0,
        'process': []
    }

    menu()
    params = insert_process(params)
    
    if params == 0:
        return
    elif params['option'] == 1:
        fifo(params)

    # print(params['process'])


if __name__ == "__main__":
    main()