# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 08:20:46 2017

@author: aluno
"""
program_counter = -1
current_instruction = -1
instruction_type = -1
run_bit = True

def get_instruction_type(current_instruction): #Acessar o arquivo de OPCodes.
    

def find_data(current_instruction, instruction_type): #Acessar o arquivo de variaveis.
    data = open("data.txt","r+")
    
    data.close()

def execute(instruction_type, data):
    

def interpret(program, starting_address):
    program_counter = starting_address
    while run_bit:
        current_instruction = program[program_counter]
        program_counter += 1
        instruction_type = get_instruction_type(current_instruction)
        data_location = find_data(current_instruction, instruction_type)
        if data_location >= 0:
            data = program[data_location]
        execute(instruction_type, data)
