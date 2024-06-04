import time

import csvLayer
import serialLayer
import readinstantaneousValues

#logging config
#logging.basicConfig(filename='../files/log.txt', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.NOTSET)
#logging.Formatter(fmt='%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d,%H:%M:%S')

#csvLayer.createCsv()

#csvLayer.writeCSVdata(("1","1","3","4"))
#csvLayer.writeCSVdata(("1","1","3","4"))

#print(csvLayer.loadCSV()[1].split(',')[1])

# serialData = ("14550000521015460406248c4c0143b79301431b4f0143bf3f60439e0f6043e6f05f43f4fd6a411f858641f853474196438b3c"
#               "0060eb4400c0024500c0c0440068ac450000444300c012c40080adc3008038c40060ed44002008450040c94400b8b14500a0ec"
#               "4400c007450080c5440068b045ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff4c434343a370"
#               "7d3f8fc2753f3333733feb51783f9a99b9c09a59acc367e6adc36766ca4100007042ffffffffffffffffffff000000000000f0"
#               "42cdccefc2000070c3333370c39a19704300000040000000400000803f000000410000c04000009841ffffffffffffffffffffffcb2e")

if __name__ == "__main__":
    csvLayer.createCsv()
    serialLayer.openportSerial()

    for aux in range(200):
        #envia comando para o do medidor
        serialLayer.sendData(csvLayer.loadCSV()[1].split(',')[1])
        # recebe informações do medidor
        serialData = serialLayer.receiveData()
        # salva em CSV as informações do medidor
        csvLayer.writeCSVdata(readinstantaneousValues.framereacCMD14(serialData))
        print('Executando!!!!' + str(aux))
        time.sleep(10)

    serialLayer.closeportSerial()