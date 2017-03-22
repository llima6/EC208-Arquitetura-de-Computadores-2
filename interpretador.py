# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 08:20:46 2017

@author: aluno
"""
AC = 0
REG = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
memoria = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
data = [0,0,0,0]
PC = -1
instr = -1
instr_type = -1
run_bit = True

instructions = {'0000':0, '0001':1, '0010':2, '0011':3, '0100':4, '0101':5, '0110':6, '0111':7}

def get_instr_type(instr): #Acessar o arquivo de OPCodes, passando os 4 caracteres como parametro e retornando um int correspondente ao codigo da instrucao desejada.
    print("Get instruction type")
    instruction = instr[0:4]
    instr_type = instructions[instruction]
    print(instr)
    print("Tipo: %d"%instr_type)
    return instr_type

def find_data(instr, instr_type): #Acessar o Acumulador ou a Memoria no endereco especificado no codigo, e entao armazenar o conteudo daquela posicao no vetor data.
    print("Find data")
    tipo_A = instr[8:10]
    pos_A = int(instr[4:8],2)

    tipo_B = instr[14:16]
    pos_B = int(instr[10:14],2)

    if(instr_type < 3):
        if(tipo_A == '00'):
            data[0] = REG[pos_A]
        elif(tipo_A == '01'):
            file = open("memoria.txt","r")
            memoria = file.readline()
            memoria = memoria.split(",")
            #if(pos_A > len(memoria)-1):
            #    memoria.append('0')
            #else:
            #    data[0] = int(memoria[pos_A])
            data[0] = int(memoria[pos_A])
            file.close()
        elif(tipo_A == '10'):
            data[0] = AC
    
        if(tipo_B == '00'):
            data[1] = REG[pos_B]
        elif(tipo_B == '01'):
            file = open("memoria.txt","r")
            memoria = file.readline()
            memoria = memoria.split(",")
            #if(pos_B > len(memoria)-1):
            #    memoria.append('0')
            #else:
            #    data[1] = int(memoria[pos_B])
            data[1] = int(memoria[pos_B])
            file.close()
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
    print(data)
    return data

def execute(instr_type, data, AC): #Usar os dados recebidos para executar a operacao escolhida na estrutura condicional
    print("Execute")
    if(instr_type == 0): #store
        file = open("memoria.txt","r")
        memoria = file.readline()
        print("Memoria")
        print(memoria)
        memoria = memoria.split(",")
        print(memoria)
        file.close()
        #if(data[2] > len(memoria)-1):
        #    memoria.append(data[0])
        #else:
        #    memoria[data[2]] = data[0]
        memoria[data[2]] = data[1]
        print(memoria)
        file = open("memoria.txt","w")
        file.write('')
        for x in memoria:
            file.writelines("%s,"%str(x))
        file.close()

    elif(instr_type == 1): #load
        file = open("memoria.txt","r")
        memoria = file.readline()
        memoria = memoria.split(",")
        REG[data[2]] = int(memoria[data[3]])
        file.close()

    elif(instr_type == 2): #move
        file = open("memoria.txt","r")
        memoria = file.readline()
        memoria = memoria.split(",")
        memoria[data[2]] = str(data[3])
        file.close()
        file = open("memoria.txt","w")
        for x in memoria:
            file.writelines("%s,"%str(x))
        file.close()

    elif(instr_type == 3): #add
        AC = data[0] + data[1]

    elif(instr_type == 4): #sub
        AC = data[0] - data[1]

    elif(instr_type == 5): #prod
        AC = data[0] * data[1]

    elif(instr_type == 6): #div
        AC = data[0] / data[1]

    elif(instr_type == 7): #literal
        REG[data[2]] = int(data[1])
    print(REG)
        

#def interpret():
print('Starting')
file = open("programa.txt","r")
programa = file.readline()
file.close()
PC = 0
file = open("memoria.txt","w")
for x in memoria:
    file.writelines("%s,"%str(x))
file.close()
while run_bit:
    instr = programa[PC*16:PC*16+16]    
    if(len(programa)/16 > PC):
        print("Instrução: %d"%(PC+1))
        PC += 1
        instr_type = get_instr_type(instr)
        #data_loc = find_data(instr, instr_type)
        data = find_data(instr, instr_type)
        #if data_loc >= 0:
        #    data = program[data_location]
        execute(instr_type, data, AC)
        print("\n")
    else:
        run_bit = False
    
        
#def main():
#    interpret()
