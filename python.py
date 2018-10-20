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
        gradeSum+=int(grade)
        gradeCount+=1

    print(studentNaam,"has an average of",gradeSum/gradeCount)

file.close()
