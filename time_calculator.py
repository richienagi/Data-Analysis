#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 17:46:37 2021

@author: richie
"""


def convertTo24(start):
    start = start.split(':')     
    start2 = start[1].split()  
    start = [start[0],start2[0],start2[1]]
    
    if start[2] == 'AM':
        if start[0] == '12':
            ans = '00' + ':' + start[1] 
        else:
            ans = start[0] + ':' + start[1] 
    else:
        if start[0] == '12':
            ans = int(start[0])
        else:
            ans = 12 + int(start[0])
        ans = str(ans) + ':' + start[1] 
    return ans

def convertTo12(add_result):
    add_result = add_result.split(':')
    if int(add_result[0]) > 12:
        add_result = str(int(add_result[0]) - 12) + ':' + add_result[1] + ' PM'
    elif int(add_result[0]) == 0:
        add_result = '12' + ':' + add_result[1] + ' AM'
    elif int(add_result[0]) == 12:
        add_result = add_result[0] + ':' + add_result[1] + ' PM'
    else:
        add_result = add_result[0] + ':' + add_result[1] + ' AM'
    return add_result


def add_time(start, duration, day=''):
    days = 0     
    start = convertTo24(start)
    start = start.split(':')
    duration = duration.split(':')
    
    if int(start[1]) + int(duration[1]) > 59:
        sumMin = int(start[1]) + int(duration[1]) - 60
        sumHours = int(start[0]) + int(duration[0]) + 1
    else:
        sumMin = int(start[1]) + int(duration[1])
        sumHours = int(start[0]) + int(duration[0])
    
    if sumHours > 24:
        days = int((sumHours/24 // 1))
        sumHours = sumHours - (days*24)
    
    if sumMin < 10:
        add_result = str(sumHours) + ':0' + str(sumMin)
    else:
        add_result = str(sumHours) + ':' + str(sumMin)
        
    add_result = convertTo12(add_result)   
    day = day.capitalize()  
    weekCalendar = {'Sunday':1,'Monday':2,'Tuesday':3,'Wednesday':4,'Thursday':5,'Friday':6,'Saturday':7}
    outputDay = ''
    
    if day in weekCalendar:
        startDay = weekCalendar[day]
        endDay = startDay + days
        
        while endDay > 7:
            endDay = endDay - 7
        
        for key,value in weekCalendar.items():
            if value == endDay:
                outputDay = key
    
    if days == 0:
        if day != '':
            outputStr = add_result + ', ' + day 
        else:
            outputStr = add_result 
    elif days == 1:
        if day != '':
            outputStr = add_result + ', ' + outputDay + ' (next day)'
        else:
            outputStr = add_result + ' (next day)'
    else:
        if day != '':
            outputStr = add_result + ', ' + outputDay + ' (' + str(days) + ' days later)' 
        else:
            outputStr = add_result + ' (' + str(days) + ' days later)'
    
    return outputStr