# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:01:55 2015

@author: HansG17
"""
#import os.path 
#assert os.path.isfile("newstuff2.xlsx")
#this will supposedly do some data analysis
import matplotlib.pyplot as plt
import numpy
import xlrd
wb=xlrd.open_workbook("player_data_soccer_new.xlsx")
sh = wb.sheet_by_index(0)

#hello = sh.row_values(0)
#print(hello[1])
#print(sh.row_values(0))
hello2 = sh.col_values(2)
#print(hello2)

# read a cell
#
#cell = sh.cell(0,0)
#print(cell)
#print(sh.cell(1,1))

arrayofgoodvalues = []
arrayofgoodvalues2= []
arrayofgoodvalues3= []
arrayGeneralSorness =[]
arraystress = []
arraymood = []
arraysleep=[]
arraygamedates =["9/30/2014","","","","","","","",""]
for i in range(0,len(hello2)):
    newarray = sh.row_values(i)
    if newarray[2] in arraygamedates:
        arrayofgoodvalues.append(newarray[4])
        arrayofgoodvalues2.append(newarray[5])
        arrayGeneralSorness.append(newarray[6])
        arraystress.append(newarray[7])
        arraymood.append(newarray[8])
       # arraysleep.append(newarray[9])
#
#
#
#
#
#print(arrayofgoodvalues)
#print(numpy.mean(arrayofgoodvalues))
#print(arrayofgoodvalues2)


#this will calculate the player with the most sleep


firstcol = sh.col_values(0)
totalsleeparry = []
for i in range(1,29):
    playerarray = []
    for x in range(0,len(firstcol)):
        if i == firstcol[x]:
            row = sh.row_values(x)
            playerarray.append(row[8])
    totsleep = sum(playerarray)    
    totalsleeparry.append(str(totsleep)+" "+str(i))
    
    
print(max(totalsleeparry))
print(totalsleeparry) 
  





plt.plot([1,2,3,4], [1,4,9,16])


















#now we can mess around
#from itertools import product
#
#def value_from_key(sheet, key):
#    for row_index, col_index in product(xrange(sheet.nrows), xrange(sheet.ncols)):
#        if sheet.cell(row_index, col_index).value == key:
#            return sheet.cell(row_index+1, col_index).value
#
#value = value_from_key(sheet, 'COLOR')