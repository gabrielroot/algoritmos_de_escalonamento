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

def sjfCompreepcao():
    class SJF:
        def infoProcesso(self, quant_processo):
            info_processos = []
            for i in range(quant_processo):
                aux = []
                processo = i+1
                print(f"P{processo}: ")
                tempo_de_chegada = int(input(f"Instante de chegada: "))
                tempo_de_execucao = int(input(f"Tempo de execução: "))
                aux.extend([processo, tempo_de_chegada, tempo_de_execucao, 0, tempo_de_execucao])
                info_processos.append(aux)

            SJF.escalonarProcesso(self, info_processos)

        def escalonarProcesso(self, info_processos):
            inicio_execucao = []
            final_execucao = []
            tempo_inicio = 0
            sequencia_execucao = []
            info_processos.sort(key=lambda x: x[1])
            while 1:
                fila_chegou = []
                fila_nchegou = []
                temp = []
                for i in range(len(info_processos)):
                    if info_processos[i][1] <= tempo_inicio and info_processos[i][3] == 0:
                        temp.extend([info_processos[i][0], info_processos[i][1], info_processos[i][2], info_processos[i][4]])
                        fila_chegou.append(temp)
                        temp = []
                    elif info_processos[i][3] == 0:
                        temp.extend([info_processos[i][0], info_processos[i][1], info_processos[i][2], info_processos[i][4]])
                        fila_nchegou.append(temp)
                        temp = []
                if len(fila_chegou) == 0 and len(fila_nchegou) == 0:
                    break
                if len(fila_chegou) != 0:
                    fila_chegou.sort(key=lambda x: x[2])
                    inicio_execucao.append(tempo_inicio)
                    tempo_inicio = tempo_inicio + 1
                    tempo_final = tempo_inicio
                    final_execucao.append(tempo_final)
                    sequencia_execucao.append(fila_chegou[0][0])
                    for k in range(len(info_processos)):
                        if info_processos[k][0] == fila_chegou[0][0]:
                            break
                    info_processos[k][2] = info_processos[k][2] - 1
                    if info_processos[k][2] == 0:        
                        info_processos[k][3] = 1
                        info_processos[k].append(tempo_final)
                if len(fila_chegou) == 0:
                    if tempo_inicio < fila_nchegou[0][1]:
                        tempo_inicio = fila_nchegou[0][1]
                    inicio_execucao.append(tempo_inicio)
                    tempo_inicio = tempo_inicio + 1
                    tempo_final = tempo_inicio
                    final_execucao.append(tempo_final)
                    sequencia_execucao.append(fila_nchegou[0][0])
                    for k in range(len(info_processos)):
                        if info_processos[k][0] == fila_nchegou[0][0]:
                            break
                    info_processos[k][2] = info_processos[k][2] - 1
                    if info_processos[k][2] == 0:    
                        info_processos[k][3] = 1
                        info_processos[k].append(tempo_final)
            tempo_turn = SJF.tTurnaround(self, info_processos)
            tempo_espe = SJF.tempoEspera(self, info_processos)
            SJF.imprimirDados(self, info_processos, sequencia_execucao)

        def tTurnaround(self, info_processos):
            for i in range(len(info_processos)):
                turnaround = info_processos[i][5] - info_processos[i][1]
                info_processos[i].append(turnaround)

        def tempoEspera(self, info_processos):
            for i in range(len(info_processos)):
                tempo_de_espera = info_processos[i][6] - info_processos[i][4]
                info_processos[i].append(tempo_de_espera)

        def imprimirDados(self, info_processos, sequencia_execucao):
            info_processos.sort(key=lambda x: x[0])
            print("Processos\tTempo de chegada\tInstante de execução\tFinal do processo\tTurnaround\tTempo de espera")
            for i in range(len(info_processos)):
                processo_P = info_processos[i][0]
                i_chegada = info_processos[i][1]
                inicio = info_processos[i][4]
                final_do_processo = info_processos[i][5]
                turna = info_processos[i][6]
                tempo_espera = info_processos[i][7]
                print(f"P{processo_P}\t\t\t{i_chegada}\t\t\t{inicio}\t\t\t{final_do_processo}\t\t\t{turna}\t\t{tempo_espera}")
            print(f"Sequência dos processos: {sequencia_execucao}")

    quant_processo = int(input("Informe a quantidade de processos: "))
    sjf = SJF()
    sjf.infoProcesso(quant_processo)

    return 0

def roundRobin():
    class RoundRobin:

        def infoProcesso(self, quant_processo):
            info_processos = []
            for i in range(quant_processo):
                aux = []
                processo = i+1
                print(f"P{processo}")
                tempo_de_chegada = int(input(f"Instante de chegada: "))
                tempo_de_execucao = int(input(f"Tempo de execução: "))
                aux.extend([processo, tempo_de_chegada, tempo_de_execucao, 0, tempo_de_execucao])
                info_processos.append(aux)
            tempo_quantum = int(input("Digite o quantum: "))
            RoundRobin.escalonarProcesso(self, info_processos, tempo_quantum)

        def escalonarProcesso(self, info_processos, tempo_quantum):
            inicio_execucao = []
            final_execucao = []
            sequencia_execucao = []
            fila_chegou = []
            tempo_inicio = 0
            info_processos.sort(key=lambda x: x[1])
            while 1:
                fila_nchegou = []
                temp = []
                for i in range(len(info_processos)):
                    if info_processos[i][1] <= tempo_inicio and info_processos[i][3] == 0:
                        present = 0
                        if len(fila_chegou) != 0:
                            for k in range(len(fila_chegou)):
                                if info_processos[i][0] == fila_chegou[k][0]:
                                    present = 1

                        if present == 0:
                            temp.extend([info_processos[i][0], info_processos[i][1], info_processos[i][2], info_processos[i][4]])
                            fila_chegou.append(temp)
                            temp = []

                        if len(fila_chegou) != 0 and len(sequencia_execucao) != 0:
                            for k in range(len(fila_chegou)):
                                if fila_chegou[k][0] == sequencia_execucao[len(sequencia_execucao) - 1]:
                                    fila_chegou.insert((len(fila_chegou) - 1), fila_chegou.pop(k))

                    elif info_processos[i][3] == 0:
                        temp.extend([info_processos[i][0], info_processos[i][1], info_processos[i][2], info_processos[i][4]])
                        fila_nchegou.append(temp)
                        temp = []
                if len(fila_chegou) == 0 and len(fila_nchegou) == 0:
                    break
                if len(fila_chegou) != 0:
                    if fila_chegou[0][2] > tempo_quantum:

                        inicio_execucao.append(tempo_inicio)
                        tempo_inicio = tempo_inicio + tempo_quantum
                        e_time = tempo_inicio
                        final_execucao.append(e_time)
                        sequencia_execucao.append(fila_chegou[0][0])
                        for j in range(len(info_processos)):
                            if info_processos[j][0] == fila_chegou[0][0]:
                                break
                        info_processos[j][2] = info_processos[j][2] - tempo_quantum
                        fila_chegou.pop(0)
                    elif fila_chegou[0][2] <= tempo_quantum:

                        inicio_execucao.append(tempo_inicio)
                        tempo_inicio = tempo_inicio + fila_chegou[0][2]
                        e_time = tempo_inicio
                        final_execucao.append(e_time)
                        sequencia_execucao.append(fila_chegou[0][0])
                        for j in range(len(info_processos)):
                            if info_processos[j][0] == fila_chegou[0][0]:
                                break
                        info_processos[j][2] = 0
                        info_processos[j][3] = 1
                        info_processos[j].append(e_time)
                        fila_chegou.pop(0)
                elif len(fila_chegou) == 0:
                    if tempo_inicio < fila_nchegou[0][1]:
                        tempo_inicio = fila_nchegou[0][1]
                    if fila_nchegou[0][2] > tempo_quantum:

                        inicio_execucao.append(tempo_inicio)
                        tempo_inicio = tempo_inicio + tempo_quantum
                        e_time = tempo_inicio
                        final_execucao.append(e_time)
                        sequencia_execucao.append(fila_nchegou[0][0])
                        for j in range(len(info_processos)):
                            if info_processos[j][0] == fila_nchegou[0][0]:
                                break
                        info_processos[j][2] = info_processos[j][2] - tempo_quantum
                    elif fila_nchegou[0][2] <= tempo_quantum:

                        inicio_execucao.append(tempo_inicio)
                        tempo_inicio = tempo_inicio + fila_nchegou[0][2]
                        e_time = tempo_inicio
                        final_execucao.append(e_time)
                        sequencia_execucao.append(fila_nchegou[0][0])
                        for j in range(len(info_processos)):
                            if info_processos[j][0] == fila_nchegou[0][0]:
                                break
                        info_processos[j][2] = 0
                        info_processos[j][3] = 1
                        info_processos[j].append(e_time)
            tempo_turn = RoundRobin.tTurnaround(self, info_processos)
            tempo_espe = RoundRobin.TempoEspera(self, info_processos)
            RoundRobin.imprimirDados(self, info_processos, sequencia_execucao)

        def tTurnaround(self, info_processos):
            for i in range(len(info_processos)):
                turnaround = info_processos[i][5] - info_processos[i][1]
                info_processos[i].append(turnaround)

        def TempoEspera(self, info_processos):
            for i in range(len(info_processos)):
                waiting_time = info_processos[i][6] - info_processos[i][4]
                info_processos[i].append(waiting_time)

        def imprimirDados(self, info_processos,sequencia_execucao):
            info_processos.sort(key=lambda x: x[0])
            print("Processos\tTempo de chegada\tInstante de execução\tFinal do processo\tTurnaround\tTempo de espera")
            for i in range(len(info_processos)):
                processo_P = info_processos[i][0]
                i_chegada = info_processos[i][1]
                inicio = info_processos[i][4]
                final_do_processo = info_processos[i][5]
                turna = info_processos[i][6]
                tempo_espera = info_processos[i][7]
                print(f"P{processo_P}\t\t\t{i_chegada}\t\t\t{inicio}\t\t\t{final_do_processo}\t\t\t{turna}\t\t{tempo_espera}")

            print(f"Sequência dos processos: {sequencia_execucao}")
    
    quant_processo = int(input("Informe o número de processos: "))
    rr = RoundRobin()
    rr.infoProcesso(quant_processo)
    
    return 0


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

    
    if params['option'] == 3:
        sjfCompreepcao()      
        return 0

    if params['option'] == 5:
        roundRobin()
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

def generic_escalation(processes, qt_processes, key): #Executa os algoritmos: FIFO, SJF (SEM PREEMPÇÂO), PRIORIDADE 
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
    

    result_processes = 'RESULTADOS:\n\n         Processo         Tempo de Chegada         Instante de Execução         Final do Processo         Turnaround         Tempo de Espera\n'
    view_process = view_exec_time = view_timeline = ' '
    for i in range(0,qt_processes):
        view_process += f'P{processes[i]["id"]}'
        view_exec_time += '  '
        view_timeline += '  '
        result_processes +=f'            P{processes[i]["id"]}                   {processes[i]["start_time"]}                           {processes[i]["exec"][0]["in_time"]}                         {processes[i]["exec"][0]["out_time"]}                       {processes[i]["turnaround"]}                   {processes[i]["waiting_time"]} \n'
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
