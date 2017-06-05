# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 08:20:46 2017

@author: aluno
"""
AC = 0
REG = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
memoria = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
cache = [-1,-1,-1]
data = [0,0,0,0]
PC = -1
instr = -1
instr_type = -1
run_bit = True

instructions = {'0000':0, '0001':1, '0010':2, '0011':3, '0100':4, '0101':5, '0110':6, '0111':7}

#------------------------------------------------------------------------------------------

def get_from_memory(): #Atualizar o vetor memoria com os valores presentes no txt memoria
    file = open("memoria.txt","r")
    memoria = file.readlines()
    memoria = [x.strip() for x in memoria]
    file.close()
    return memoria

#------------------------------------------------------------------------------------------

def send_to_memory(memoria): #Atualizar o txt memoria com os valores do vetor memoria
    file = open("memoria.txt","w")
    file.write('')
    for x in memoria:
        file.write("%s\n"%str(x))
    file.close()

#------------------------------------------------------------------------------------------

def cache_pull(cache, pos): #Preenche a cache com dois valores da memoria, pos e pos+1
    memoria = get_from_memory()
    cache[0] = pos
    cache[1] = int(memoria[pos])
    cache[2] = int(memoria[pos+1])

#------------------------------------------------------------------------------------------

def cache_push(pos_M, pos_C):
    if(cache[pos_C] != memoria[pos_M]):
        memoria[pos_M] = cache[pos_C]

#------------------------------------------------------------------------------------------

def get_instr_type(instr): #Acessar o arquivo de OPCodes, passando os 4 caracteres como parametro e retornando um int correspondente ao codigo da instrucao desejada.
    print("Get instruction type")
    instruction = instr[0:4]
    instr_type = instructions[instruction]
    print(instr)
    print("Tipo: %d"%instr_type)
    return instr_type

#------------------------------------------------------------------------------------------

def find_data(instr, instr_type): #Acessar o Acumulador ou a Memoria no endereco especificado no codigo, e entao armazenar o conteudo daquela posicao no vetor data.
    global AC
    global cache
    print("Find data")
    tipo_A = instr[8:10]
    pos_A = int(instr[4:8],2)

    tipo_B = instr[14:16]
    pos_B = int(instr[10:14],2)

    if(instr_type < 3):
        if(tipo_A == '00'):
            data[0] = REG[pos_A]
        elif(tipo_A == '01'):
            if(cache[0] == pos_A):
                data[0] = cache[1]
            elif(cache[0] == (pos_A - 1)):
                data[0] = cache[2]
            else:
                cache_pull(cache,pos_A)
                data[0] = cache[1]
        elif(tipo_A == '10'):
            data[0] = AC
    
        if(tipo_B == '00'):
            data[1] = REG[pos_B]
        elif(tipo_B == '01'):
            if(cache[0] == pos_B):
                data[0] = cache[1]
            elif(cache[0] == (pos_B - 1)):
                data[0] = cache[2]
            else:
                cache_pull(cache,pos_B)
                data[0] = cache[1]
        elif(tipo_B == '10'):
            data[1] = AC
        print("1")

    elif(instr_type < 7):
        data[0] = REG[pos_A]
        data[1] = REG[pos_B]
        print("2")

    elif(instr_type == 7):
        data[1] = int(instr[10:16],2)
        print("3")

    data[2] = pos_A
    data[3] = pos_B
    print(AC)
    print(data)
    return data

#------------------------------------------------------------------------------------------

def execute(instr_type, data): #Usar os dados recebidos para executar a operacao escolhida na estrutura condicional
    global AC
    global memoria
    print("Execute")
    if(instr_type == 0): #store
        #memoria = get_from_memory()
        cache[1] = data[1]
        cache_push(data[2],1)
        #memoria[data[2]] = data[1]
        send_to_memory(memoria)
        
    elif(instr_type == 1): #load
        #memoria = get_from_memory()
        cache_pull(cache,data[3])
        REG[data[2]] = cache[1]
        #REG[data[2]] = int(memoria[data[3]])
        
    elif(instr_type == 2): #move
        memoria = get_from_memory()
        memoria[data[2]] = str(data[3])
        send_to_memory(memoria)
        
    elif(instr_type == 3): #add
        AC = data[0] + data[1]

    elif(instr_type == 4): #sub
        AC = data[0] - data[1]

    elif(instr_type == 5): #prod
        AC = data[0] * data[1]

    elif(instr_type == 6): #div
        AC = data[0] / data[1]

    elif(instr_type == 7): #literal
        REG[cache[0]] = int(cache[2])
        REG[data[2]] = int(data[1])
    print(REG)
    print(AC)

#------------------------------------------------------------------------------------------

print('Starting')
file = open("programa.txt","r")
programa = file.readline()
file.close()
PC = 0
send_to_memory(memoria)
while run_bit:
    instr = programa[PC*16:PC*16+16]  
    if(len(programa)/16 > PC):
        print("Instrução: %d"%(PC+1))
        PC += 1
        instr_type = get_instr_type(instr)
        data = find_data(instr, instr_type)
        execute(instr_type, data)
        print("\n")
    else:
        run_bit = False
