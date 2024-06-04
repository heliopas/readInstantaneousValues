import csv
import datetime

columns = ("ReadingDate", "PhaseA_current", "PhaseB_current", "PhaseC_current")

def createCsv():
    fileDate = datetime.datetime.now().strftime("%y%m%d+log.csv")

    with open('./files/'+fileDate, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csvfile)
