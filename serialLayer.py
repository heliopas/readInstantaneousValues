import logging
import serial

#comm ports var
serialComm = 'COM21'
#global vars
global comport

def openportSerial():
    global comport
    try:
        comport = serial.Serial(port=serialComm, baudrate=9600, timeout=1, stopbits=serial.STOPBITS_ONE)
    except serial.SerialException as e:
        logging.error("Error during open port RelayBox: %s" % e)

def closeportSerial():
    global comport
    comport.close()

def sendData(data):
    openportSerial()
    global comport
    try:
        comport.write(bytes.fromhex(data))
    except serial.SerialException as e:
        print("Error during sending something by serial: %s" % e)
    closeportSerial()

def receiveData():
    openportSerial()
    global comport
    try:
        return comport.readall().hex()
    except serial.SerialException as e:
        print("Error during receiving something by serial: %s" % e)
    closeportSerial()