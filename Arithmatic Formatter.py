#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 12:12:51 2021

@author: richie

FreeCodeCamp Scientific Computing with Python Projects - Arithmatic Formatter

"""

def arithmetic_arranger(inputList,printResults=False):
    ansStrU = ''
    ansStrL = ''
    ansStrDash = ''
    ansStrResult = ''
    
    for j in range(0,len(inputList)):
        if len(inputList) > 5:
            return 'Error: Too many problems.'
        test = inputList[j].split()
        if len(str(test[0])) > 4 or len(str(test[2])) > 4:
            return "Error: Numbers cannot be more than four digits."
        if test[1] != '+' and test[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if str(test[0]).isdigit() == False or str(test[2]).isdigit() == False:
            return 'Error: Numbers must only contain digits.'
        filler = ''
        count = 0
        if len(test[0]) < len(test[2]):
            count = len(test[2]) - len(test[0])
            for i in range(0,count):
                filler = filler + ' '
            ansU = '  ' + filler + test[0]
            ansL = test[1] + ' ' + test[2]
            ansDash = '--' + '-'*len(test[2])
            if test[1] == '+':
                result = int(test[0]) + int(test[2])
            if test[1] == '-':
                result = int(test[0]) - int(test[2])
            resultFiller = len(ansDash) - len(str(result))
            ansResult = ' '*resultFiller + str(result)
        else:
            count = len(test[0]) - len(test[2])
            for i in range(0,count): 
                filler = filler + ' '
            ansU ='  '+ test[0] 
            ansL = test[1] + ' ' + filler + test[2]
            ansDash = '--' + '-'*len(filler) + '-'*len(test[2])
            if test[1] == '+':
                result = int(test[0]) + int(test[2])
            if test[1] == '-':
                result = int(test[0]) - int(test[2])
            resultFiller = len(ansDash) - len(str(result))
            ansResult = ' '*resultFiller + str(result) 
        
        ansStrU = ansStrU + ansU + '    '
        ansStrL = ansStrL + ansL + '    '
        ansStrDash = ansStrDash + ansDash + '    '
        ansStrResult = ansStrResult + ansResult + '    '
         
    ansStrU = ansStrU[:len(ansStrU)-4]
    ansStrL = ansStrL[:len(ansStrL)-4]
    ansStrDash = ansStrDash[:len(ansStrDash)-4]
    ansStrResult = ansStrResult[:len(ansStrResult)-4]
    
    if printResults == True:
        outputStr = ansStrU + '\n' + ansStrL + '\n' + ansStrDash + '\n' + ansStrResult
    else:
        outputStr = ansStrU + '\n' + ansStrL + '\n' + ansStrDash
    return outputStr

inputList  = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
