#!/bin/python3

file = open("textFile.txt","r")
file.readline()


for line in file:
    gradeSum = 0
    gradeCount = 0

    gradeList = line.rstrip().split(" ")
    studentNum=gradeList[0]
    studentNaam=gradeList[1]

    for grade in gradeList[2:]:
        if int(grade)!=0:
            gradeSum+=int(grade)
            gradeCount+=1
        else:
            continue

    if gradeSum!=0:
        print(studentNaam,"has an average of",gradeSum/gradeCount)
    else:
        print(studentNaam,"has an average of 0.")

file.close()
