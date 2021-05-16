#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:51:10 2021

@author: richie
FreeCodeCamp Scientific Computing with Python Projects - Polygon Area Calculator
"""

class Rectangle:
    def __init__(self,width,height):
        self.width  = width
        self.height = height
                
    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height
        
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return (2*self.width) + (2*self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        for i in range(0,self.height):
            picture = picture + '*'*self.width + '\n'
        return picture
    
    def get_amount_inside(self,shape):
        x = int((self.width/shape.width // 1))
        y = int((self.height/shape.height // 1))
        return x*y
    
    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height='+ str(self.height) + ')'

class Square(Rectangle):
    def __init__(self,side):
        Rectangle.__init__(self,side,side)
        
    def set_side(self,side):
        Rectangle.set_width(self,side)
        Rectangle.set_height(self,side)
        
    def set_width(self,side):
        Rectangle.set_width(self,side)
        Rectangle.set_height(self,side)
        
    def set_height(self,side):
        Rectangle.set_width(self,side)
        Rectangle.set_height(self,side)
        
    def __str__(self):
        return 'Square(side=' + str(self.width) + ')'
    
