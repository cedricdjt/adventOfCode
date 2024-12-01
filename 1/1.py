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

def sort(dataL, dataR):
    sortedL = sorted(dataL)
    sortedR = sorted(dataR)
    return sortedL, sortedR

def calcDistance(sortedL, sortedR):
    i = 0
    totalDistance = 0
    for point in sortedR:
        distance = abs(point - sortedL[i])
        i += 1
        totalDistance += distance
    return totalDistance

dataL, dataR = getData()
sortedL, sortedR= sort(dataL,dataR)
print(calcDistance(sortedL, sortedR))