import csv
import datetime

columns = ("ReadingDate", "PhaseA_current", "PhaseB_current", "PhaseC_current")
fileDate = datetime.datetime.now().strftime("%y%m%d_log.csv")

def createCsv():
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

