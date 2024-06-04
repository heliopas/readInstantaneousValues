import datetime
import time

import io
import serial
import errno
from colorama import Fore, Back, Style
from time import sleep
import logging
import csv

#comm ports var
serialComm = 'COM21'
#global vars
global comport

def openportRelayBox():
    global comport
    try:
        comport = serial.Serial(port=serialComm, baudrate=115200, timeout=5, stopbits=serial.STOPBITS_ONE)
    except serial.SerialException as e:
        logging.error("Error during open port RelayBox: %s" % e)

def closeportRelayBox():
    global comport
    comport.close()

def sendData(data):
    global comport
    try:
        comport.write(data)
        logging.info("Rele open")
    except serial.SerialException as e:
        logging.error("Error during open RelayBox_ch1: %s" % e)

