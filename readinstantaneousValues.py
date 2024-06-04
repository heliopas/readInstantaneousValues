import binascii
import struct
import textwrap

def checkframeSize(data): #valida retorno do comando recebido
    if len(data)/2 == 258:
        return 0
    else:
        return 1

def framereacCMD14(data):
    if checkframeSize(data) == 0:
        vec = textwrap.wrap(data, 2)

        #obtem numero de serie do medidor
        serialNumber = vec[1]+vec[2]+vec[3]+vec[4]

        #obtem data de leitura realizada
        logTime = vec[8]+'/'+vec[9]+'/'+vec[10]+' '+vec[5]+':'+vec[6]+':'+vec[7]

        #obtem corrente por fase (octetos rotacionados BigEndian)
        uA = struct.unpack('>f', binascii.unhexlify(vec[14]+vec[13]+vec[12]+vec[11]))[0]
        uB = struct.unpack('>f', binascii.unhexlify(vec[18]+vec[17]+vec[16]+vec[15]))[0]
        uC = struct.unpack('>f', binascii.unhexlify(vec[22]+vec[21]+vec[20]+vec[19]))[0]

        # print(uA)
        # print(uB)
        # print(uC)

        #obtem tensão por fase (octetos rotacionados BigEndian)
        iA = struct.unpack('>f', binascii.unhexlify(vec[38]+vec[37]+vec[36]+vec[35]))[0]
        iB = struct.unpack('>f', binascii.unhexlify(vec[42]+vec[41]+vec[40]+vec[39]))[0]
        iC = struct.unpack('>f', binascii.unhexlify(vec[46]+vec[45]+vec[44]+vec[43]))[0]

        # print(iA)
        # print(iB)
        # print(iC)

        #obtem potência ativa por fase (octetos rotacionados BigEndian)
        paA = struct.unpack('>f', binascii.unhexlify(vec[54]+vec[53]+vec[52]+vec[51]))[0]
        paB = struct.unpack('>f', binascii.unhexlify(vec[58]+vec[57]+vec[56]+vec[55]))[0]
        paC = struct.unpack('>f', binascii.unhexlify(vec[62]+vec[61]+vec[60]+vec[59]))[0]

        # print(paA)
        # print(paB)
        # print(paC)

        # obtem potência ativa tri-fasica (octetos rotacionados BigEndian)
        paABC = struct.unpack('>f', binascii.unhexlify(vec[66]+vec[65]+vec[64]+vec[63]))[0]

        # print(paABC)

        #obtem potência reativa por fase (octetos rotacionados BigEndian)
        prA = struct.unpack('>f', binascii.unhexlify(vec[70]+vec[69]+vec[68]+vec[67]))[0]
        prB = struct.unpack('>f', binascii.unhexlify(vec[74]+vec[73]+vec[72]+vec[71]))[0]
        prC = struct.unpack('>f', binascii.unhexlify(vec[78]+vec[77]+vec[76]+vec[75]))[0]

        # print(prA)
        # print(prB)
        # print(prC)

        # obtem potência reativa tri-fasica (octetos rotacionados BigEndian)
        prABC = struct.unpack('>f', binascii.unhexlify(vec[82]+vec[81]+vec[80]+vec[79]))[0]

        # print(prABC)

        # obtem frequencia da rede
        fHz = struct.unpack('>f', binascii.unhexlify(vec[186]+vec[185]+vec[184]+vec[183]))[0]

        # print(fHz)

        # obtem temperatura medidor
        tempMeter = struct.unpack('>f', binascii.unhexlify(vec[182]+vec[181]+vec[180]+vec[179]))[0]

        # print(tempMeter)

        vec = [logTime, serialNumber, uA, uB, uC,
               iA, iB, iC,
               paC, paB, paC, paABC,
               prA, prB, prC, prABC,
               fHz, tempMeter]

        return vec

    else:
        return 1