# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 08:20:46 2017

@author: aluno
"""
AC = 0
REG = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
data = [0,0]
PC = -1
instr = -1
instr_type = -1
run_bit = True

instructions = {'0000':0, '0001':1, '0010':2, '0011':3, '0100':4, '0101':5, '0110':6}

def get_instr_type(instr): #Acessar o arquivo de OPCodes, passando os 4 caracteres como parametro e retornando um int correspondente ao codigo da instrucao desejada.
    instruction = instr[0:4]
    instr_type = instructions[instruction]
    return instr_type

def find_data(instr, instr_type): #Acessar o Acumulador ou a Memoria no endereco especificado no codigo, e entao armazenar o conteudo daquela posicao no vetor data.
    
    tipo_A = instr[8:10]
    pos_A = int(instr[4:8],2)
    print(pos_A)
    if(tipo_A == '00'):
        data[0] = REG[pos_A]
    elif(tipo_A == '01'):
        file = open("memoria.txt","r")
        memoria = file.readlines()
        data[0] = memoria[pos_A]
        file.close()
    
    tipo_B = instr[14:16]
    pos_B = int(instr[10:14],2)
    print(pos_B)
    if(tipo_B == '00'):
        data[1] = REG[pos_B]
    elif(tipo_B == '01'):
        file = open("memoria.txt","r")
        memoria = file.readlines()
        data[1] = memoria[pos_B]
        file.close()
    
    return data

def execute(instr_type, data): #Usar os dados recebidos para executar a operacao escolhida na estrutura condicional
    if(instr_type == 0): #store
        file = open("memoria.txt","r")
        memoria = file.readlines()
        memoria[data[0]] = AC
        file = open("memoria.txt","w")
        file.writelines(memoria)
        file.close()
    elif(instr_type == 1): #load
        file = open("memoria.txt","r")
        memoria = file.readlines()
        AC = memoria[data[0]]
        file.close()
    elif(instr_type == 2): #move
        file = open("memoria.txt","r")
        memoria = file.readlines()
        memoria[data[0]] = data[1]
        file = open("memoria.txt","w")
        file.writelines(memoria)
        file.close()
    elif(instr_type == 3): #add
        AC = data[0] + data[1]
    elif(instr_type == 4): #sub
        AC = data[0] - data[1]
    elif(instr_type == 5): #prod
        AC = data[0] * data[1]
    elif(instr_type == 6): #div
        AC = data[0] / data[1]
        

#def interpret():
print('Starting')
file = open("programa.txt","r")
program = file.readlines()
PC = 0
while run_bit:
    instr = program[PC]
    print(instr)
    PC += 1
    instr_type = get_instr_type(instr)
    print(instr_type)
    #data_loc = find_data(instr, instr_type)
    data = find_data(instr, instr_type)
    #if data_loc >= 0:
    #    data = program[data_location]
    execute(instr_type, data)
        
#def main():
#    interpret()
