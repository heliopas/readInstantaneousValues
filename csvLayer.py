import csv
import datetime
import os.path

columns = ("ReadingDate","SerialNumber",
           "PhaseA_voltage", "PhaseB_voltage", "PhaseC_voltage",
           "PhaseA_current", "PhaseB_current", "PhaseC_current",
           "PhaseA_activePower", "PhaseB_activePower", "PhaseC_activePower", "PhaseABC_activePower",
           "PhaseA_reactivePower", "PhaseB_reactivePower", "PhaseC_reactivePower", "PhaseABC_reactivePower",
           "LineFrequency","MeterTemperature")

fileDate = datetime.datetime.now().strftime("%y%m%d_log.csv")

def createCsv():
    if not os.path.exists('./files/'+fileDate):
        with open('./files/'+fileDate, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, dialect='excel',)
            writer.writerow(columns)
        csvfile.close()


def writeCSVdata(data):
    with open('./files/'+fileDate, 'a', newline='', encoding='utf-8') as csvfile:
        try:
            writer = csv.writer(csvfile, dialect='excel')
            writer.writerow(data)
        except csv.Error as e:
            print("Error during write something on CSV: %s" % e)

def loadCSV():
    global csvreader
    with open('./files/commands.csv', 'r') as file:
        csvreader = file.readlines()
        return csvreader

