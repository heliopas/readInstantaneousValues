import binhex
from colorama import Fore, Back, Style
import csv
import time
import csvLayer

#logging config
#logging.basicConfig(filename='../files/log.txt', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.NOTSET)
#logging.Formatter(fmt='%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d,%H:%M:%S')

def loadCSV():
    global csvreader
    with open('../files/commands.csv', 'r') as file:
        csvreader = file.readlines()

csvLayer.createCsv()
