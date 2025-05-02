import os
import time
import csv
os.system('clear')
lineslist = [''] * 30
def drawframe(text='',line=1):
    '''
    Clears the terminal (including the previous frame) and draws a new frame, including (by-default), the textbox outlines.
    
    Args:
        text (str): The text that will be written in the textbox.
        line (int): The line that the text will be written on.
    '''
    lineslist[(line-1)] = text
    os.system('clear')
    print(' ' + ('-'*50) + '  ' + ('-'*50))
    for i in range(30):
        buffer = lineslist[(i)] + (' ' * (49-len(lineslist[(i)])))
        if (line-1) == i or lineslist[(i)] != '':
            if i == 15:
                print(('|')+(buffer)+(' | ') + ('-'*50))
            elif i <= 14:
                print(('|')+(buffer)+(' ||')+(' ' * 50)+('|'))
            else:
                print(('|')+(buffer)+(' | ') + ('-'*50))
        elif i == 15:
            print(('|')+(' ' * 49)+(' | ') + ('-'*50))
        elif i <= 14:
            print(('|')+(' ' * 49)+(' ||')+(' ' * 50)+('|'))
        else:
            print(('|')+(' ' * 49)+(' |'))
    print(' ' + ('-'*50))
def writeword(text,line=1,delay=0.2):
    """Utilises drawframe() to write a full word/sentence which includes (by-default), the textbox outlines.
    
    Args:
        text (str): The text that will be written in the textbox.
        line (int): The line that the text will be written on.
        delay (float): The delay between each character in the text.
    """
    for i in range(len(text)):
        drawframe((text[0:i])+'_',line)  
        time.sleep(delay)
    drawframe((text),line)
def getfromcsv(file):
    """Reads a CSV file line-by-line and uses writeword(), with the arguments coming from the CSV values.
    
    Args:
        file (str): The name/path of the CSV file which will be read.
    """
    with open(file) as file_obj: 
        reader_obj = csv.reader(file_obj) 
        for row in reader_obj: 
            writeword(str(row[0]),int(row[1]),float(row[2]))