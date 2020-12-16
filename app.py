import os

def menu():
    os.system('clear')

    print('        +=======+============================+')
    print('        | OPÇÃO |          ALGORITMO         |')
    print('        +=======+============================+')
    print('        |   1   |    FIFO                    |')
    print('        +-------+----------------------------+')
    print('        |   2   |    SJF (SEM PREEMPÇÃO)     |')
    print('        +-------+----------------------------+    [TECLE QUALQUER OUTRO NÚMERO PARA SAIR]')
    print('        |   3   |    SJF (COM PREEMPÇÃO)     |')
    print('        +-------+----------------------------+')
    print('        |   4   |    ALGOTITMO PRIORIDADE    |')
    print('        +-------+----------------------------+')
    print('        |   5   |    ROUND ROBIN (QUANTUM)   |')
    print('        +-------+----------------------------+')


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

    params['qt_processes'] = int(input('Informe a quantidade de processos: '))

    if params['option'] == 4:
        for i in range(int(params['qt_processes'])):
            print(f'P{i+1}:')

            priority = int(input('    Prioridade do processo: '))
            exec_time = int(input('    Tempo de execução: '))
            start_time = int(input('    Instante de chegada: '))
            print(' ')

            params['processes'].append({
                'id': i+1,
                'exec_time': exec_time,
                'start_time': start_time,
                'waiting_time': 0,
                'turnaround': -1,
                'priority': priority,
                'exec': []
            })
    else:
        for i in range(int(params['qt_processes'])):
            print(f'P{i+1}:')

            exec_time = int(input('    Tempo de execução: '))
            start_time = int(input('    Instante de chegada: '))
            print(' ')

            params['processes'].append({
                'id': i+1,
                'exec_time': exec_time,
                'start_time': start_time,
                'waiting_time': 0,
                'turnaround': -1,
                'exec': []
            })

    return params


def sort_by(processes, key):     #(Fila de processos, parametro para ordenação) 

    for i in range(1, len(processes)):
        j = i
        while j > 0 and processes[j - 1][key] > processes[j][key]:
            tmp = processes[j]
            processes[j] = processes[j - 1]
            processes[j - 1] = tmp
            j -= 1
    
    return processes

def sort_by_in_time(processes): 

    for i in range(1, len(processes)):
        j = i
        while j > 0 and processes[j - 1]['exec'][0]['in_time'] > processes[j]['exec'][0]['in_time']:
            tmp = processes[j]
            processes[j] = processes[j - 1]
            processes[j - 1] = tmp
            j -= 1
    
    return processes


def generic_escalation(processes, qt_processes, key):
    processes = sort_by(processes, key)    #Ordena os processesos em ordem crescente conforme parâmetro

    timeline = 0
    running = False
    exited = 0
    while True:
        cont = 0
        checked_until = -1
        while cont < len(processes):
            if not running and len(processes[cont]['exec']) == 0 and processes[cont]['start_time'] <= timeline: #Se existem mais que 2 processos, o anterior já está finalizado e já está na hora deste executar
                processes[cont]['exec'].append({
                    'in_time': timeline,
                    'out_time': 0
                })
                running = True

            if  len(processes[cont]['exec']) > 0 and processes[cont]['exec'][0]['out_time'] == 0 and processes[cont]['exec'][0]['in_time'] + processes[cont]['exec_time'] == timeline:  #Completamente executado!
                processes[cont]['exec'][0]['out_time'] = timeline
                exited += 1
                checked_until = cont
                cont = 0      #Para iniciar as verificações conforme a prioridade mais alta
                running = False
                continue
            
            if  cont > checked_until and processes[cont]['start_time'] <= timeline and len(processes[cont]['exec']) == 0: #Se processo já chegou | ainda não está executando | ainda não finalizou
                processes[cont]['waiting_time'] += 1
               
            cont += 1
        

        timeline += 1

        if exited == qt_processes:
            for x in range(0, len(processes)):
                processes[x]['turnaround'] = processes[x]['waiting_time'] + processes[x]['exec_time'] #Calcule o turnaround
            break


    processes = sort_by_in_time(processes)  #Para saber a ordem de execução dos processos
    

    result_processes = 'RESULTADOS:\n\n   Processo         Tempo de Espera         Turnaround\n'
    view_process = view_exec_time = view_timeline = ' '
    for i in range(0,qt_processes):
        view_process += f'P{processes[i]["id"]}'
        view_exec_time += '##'
        view_timeline += '##'
        result_processes += f'      P{processes[i]["id"]}                  {processes[i]["waiting_time"]}                      {processes[i]["turnaround"]}\n'
        for j in range(0,processes[i]['exec'][0]['out_time'] - processes[i]['exec'][0]['in_time']):
            view_timeline += f'{processes[i]["id"]}'
            view_process += '=' 
            view_exec_time += '-'
    

    print(result_processes)
    
    test =input('Deseja visualizar a linha de execução? (Talvez seja necessário redimensionar o terminal) S/N: ')
    if test == 's' or 's'.upper():
        print(f'{view_process}\n{view_exec_time}\n{view_timeline}')

    return processes


def main():
    params = {
        'option': -1,
        'qt_processes': 0,
        'processes': []
    }
    menu()
    params = insert_process(params)

    if not params:
        return
    elif params['option'] == 1:
        params['processess'] = generic_escalation(params['processes'],params['qt_processes'], 'start_time')
    elif params['option'] == 2:
        params['processess'] = generic_escalation(params['processes'],params['qt_processes'], 'exec_time')
    elif params['option'] == 4:
        params['processess'] = generic_escalation(params['processes'],params['qt_processes'], 'priority')


if __name__ == "__main__":
    main()