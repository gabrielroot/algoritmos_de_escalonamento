import os

def menu():
    os.system('clear')

    print('        +=======+============================+')
    print('        | OPÇÃO |          ALGORITMO         |')
    print('        +=======+============================+')
    print('        |   1   |    FIFO                    |')
    print('        +-------+----------------------------+')
    print('        |   2   |    SJF (SEM PREEMPÇÃO)     |')
    print('        +-------+----------------------------+    [TECLE  QUALQUER OUTRO NÚMERO]')
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

    params['qt_processes'] = int(input('Informe a quantidade de processesos: '))

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


def sort_by_start_time(processes):      #Odena os processesos em ordem crescente de tempo de chegada
    for i in range(1, len(processes)):
        j = i
        while j > 0 and processes[j - 1]['start_time'] > processes[j]['start_time']:
            tmp = processes[j]
            processes[j] = processes[j - 1]
            processes[j - 1] = tmp
            j -= 1
    
    return processes


def fifo(processes, qt_processes):
    processes = sort_by_start_time(processes)

    timeline = i = 0
    while i < 100:      #CORRIGIR

        count = 0
        while count < len(processes):
            if processes.index(processes[count]) == 0:
                if processes[count]['start_time'] == timeline: 
                    processes[count]['exec'].append({ 
                        'in_time': timeline,
                        'out_time': 0
                    })

            if count > 0 and len(processes[count-1]['exec']) > 0 and processes[count-1]['exec'][0]['out_time'] > 0 and len(processes[count]['exec']) == 0: #Se existem mais que 2 processos e o anterior já está finalizado
                print(processes[count-1]['exec'][0]['out_time'],'Processo anterior finalizou')
                processes[count]['exec'].append({
                    'in_time': timeline,
                    'out_time': 0
                })

            if  len(processes[count]['exec']) > 0 and processes[count]['exec'][0]['in_time'] + processes[count]['exec_time'] == timeline:  #Completamente executado!
                print(f'Tempo de inicio+tempo de execução == timeline atual {processes[count]["start_time"]} + {processes[count]["exec_time"]} = {timeline}')
                processes[count]['exec'][0]['out_time'] = timeline
            
            if  processes[count]['start_time'] <= timeline and len(processes[count]['exec']) == 0: #Se processo já chegou | ainda não está executando | ainda não finalizou
                processes[count]['waiting_time'] += 1
            
            

            count += 1
        i +=1
        # if qt_processes == i:
        #     break


        timeline += 1

        for x in range(0, len(processes)):
            processes[x]['turnaround'] = processes[x]['waiting_time'] + processes[x]['exec_time']


    return processes



def main():
    params = {
        'option': -1,
        'qt_processes': 0,
        'processes': []
    }

    menu()
    params = insert_process(params)
    sort_by_start_time(params['processes'])    
    if not params:
        return
    elif params['option'] == 1:
        params['processess'] = fifo(params['processes'],params['qt_processes'])

    print(params['processes'])


if __name__ == "__main__":
    main()