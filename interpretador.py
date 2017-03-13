# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 08:20:46 2017

@author: aluno
"""
AC[] = 0
PC = -1
instr = -1
instr_type = -1
run_bit = True

def get_instr_type(instr): #Acessar o arquivo de OPCodes, passando os 4 caracteres como parametro e retornando um int correspondente ao codigo da instrucao desejada.
    instruction = instr[0:4]
    instr_type = type(instruction)
    return instr_type

def find_data(instr, instr_type): #Acessar o Acumulador ou a Memoria no endereco especificado no codigo, e entao armazenar o conteudo daquela posicao no vetor data.
    
    tipo_A = instr[8:10]
    pos_A = instr[4:8]
    if(tipo_A == '00'):
        data[0] = AC[pos_A]
    elif(tipo_A == '01'):
        file = open("memoria.txt","r")
        file.readlines()
        data[0] = file[pos_A]
        file.close()
    
    tipo_B = instr[14:16]
    pos_B = instr[10:14]
    if(tipo_B == '00'):
        data[1] = AC[pos_B]
    elif(tipo_B == '01'):
        file = open("memoria.txt","r")
        file.readlines()
        data[1] = file[pos_B]
        file.close()
    
    return data

def execute(instr_type, data): #Usar os dados recebidos para executar a operacao escolhida na estrutura condicional
    if(instr_type == 0):
        file = open("memoria.txt","r")
        memoria = file.readlines()
        memoria[data[0]] = data[1]
        file = open("memoria.txt","w")
        file.writelines(memoria)
        file.close()
    elif(instr_type == 1):
        
    elif(instr_type == 2):
        
    elif(instr_type == 3):
        data[1] = data[0] + data[1]
    elif(instr_type == 4):
        data[1] = data[0] - data[1]
    elif(instr_type == 5):
        data[1] = data[0] * data[1]
    elif(instr_type == 6):
        data[1] = data[0] / data[1]

def interpret(program, starting_address):
    PC = starting_address
    while run_bit:
        instr = program[PC]
        PC += 1
        instr_type = get_instr_type(instr)
        data_loc = find_data(instr, instr_type)
        if data_loc >= 0:
            data = program[data_location]
        execute(instr_type, data)
