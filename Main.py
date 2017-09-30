import csv
import numpy as np

def readFile():
    file = open('arcos.csv', 'rt')
    dataTemp = list(csv.reader(file))
    data = []
    for l in dataTemp:
        newLine = str.split(l[0], '\t')
        newLine.pop(1)
        newLine.pop(2)
        data.append(newLine)
        # l.pop(1)
        # l.pop(2)
        # data.append(l)
    return data

def generateMatrix(data):
    data.pop(0)
    print(data)
    colHeader = []
    rowHeader = []
    for c in data:
        i = findInArray(colHeader, c[0])
        j = findInArray(rowHeader, c[1])
        if i == -1:
            colHeader.append(c[0])
        if j == -1:
            rowHeader.append(c[1])
    filledMatrix = fillMatrix(rowHeader, colHeader, data)

    convertToFile(filledMatrix, "paoCircos")
    newMatrix = calculateGetAndSend(filledMatrix)
    for i in range(0, len(newMatrix)):
        for j in range(0, len(newMatrix[0])):
            print(newMatrix[i][j]," ", end="")
        print()

def calculateGetAndSend(matrix):
    sendArray = ["RECEIVES-ARC"]
    lenRow = len(matrix[0])
    lenCol = len(matrix)
    matrix[0].append("SENDS-ARC")
    for i in range(1,lenCol):
        count = 0
        for j in range(1,lenRow):
            if int(matrix[i][j]) > 0:
                count += 1
        matrix[i].append(count)

    for j in range(1,lenRow):
        count = 0
        for i in range(1,lenCol):
            if int(matrix[i][j]) > 0:
                count += 1
        sendArray.append(count)
    sendArray.append("-")
    matrix.append(sendArray)
    convertToFile(matrix, "PaoFileCount")
    return matrix


def convertToFile(data, fileName):
    out = csv.writer(open(fileName+".csv", "w"), delimiter=',')

    for d in data:
        out.writerow(d)


def fillMatrix(rowHeader, colHeader, data):
    matrix = []
    matrix.append(["data"]+rowHeader)
    for c in colHeader:
        newLine = [c]
        # newLine.append(c)
        for r in rowHeader:
            value = findInData(c, r, data)
            newLine.append(getValueMatrix(value))
        matrix.append(newLine)
    print(matrix)
    return matrix

def findInData(gen1, gen2, data):
    for d in data:
        if gen1 == d[0] and gen2 == d[1]:
            return d[2]
    return 'X'

def getValueMatrix(letter):
    if (str.upper(letter) == 'A'):
        return 350
    elif (str.upper(letter) == 'R'):
        return 10
    else:
        return 0

def findInArray(array, value):
    index = -1
    cont = 0
    for e in array:
        if e == value:
            index = cont
        cont+=1
    return index


def main():
    fileValues = readFile()
    generateMatrix(fileValues)



main()