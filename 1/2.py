from collections import Counter

def getData():
    with open ('input.txt') as file:
        dataL = []
        dataR = []
        if file.readable():
            for line in file:
                parts = line.split()
                if len(parts) == 2:
                    dataL.append(int(parts[0]))
                    dataR.append(int(parts[1]))

        return dataL,dataR

def calcScore(dataL, dataR):
    countR = Counter(dataR)
    total = 0
    for point in dataL:
        total += point * countR[point]
    return total



dataL, dataR = getData()
print(calcScore(dataL, dataR))