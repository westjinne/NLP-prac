import os
import requests
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re
from collections import OrderedDict

filepath = os.getcwd()+"/desktop/harrypotter/"
filename = "Harry Potter and the Sorcerer's Stone.txt"


def getContent():
    with open(os.getcwd()+"/desktop/harrypotter/Harry Potter and the Sorcerer's Stone.txt", "r") as f:
        fullSample = f.read()
    return fullSample

#fileToEdit = getContent()
#print(fileToEdit)


def splitContent(file):
    newFull = file.split(".")
    for i in newFull:
        i = i.split("!")
    return newFull

#splitedFileList = splitContent(fileToEdit)


def editMrMrsException(fileList):
    i = 0
    end = 500
    index_s = 0
    checkedTextList = []
    while i < end:
        if((fileList[i][-2:] == "Mr") or (fileList[i][-3:] == "Mrs")):
            if((fileList[i+1][-2:] == "Mr") or (fileList[i+1][-3:] == "Mrs")):
                fileList[i] = fileList[i]+"."+fileList[i+1]+"."+fileList[i+2] +"."
                checkedTextList.append(fileList[i])
                i = i+3
            else:
                fileList[i] = fileList[i] + "." + fileList[i+1] +"."
                checkedTextList.append(fileList[i])
                i = i+2
        else:
            fileList[i] = fileList[i] +"."
            checkedTextList.append(fileList[i])
            i = i+1
    return checkedTextList

#checkMrMrsList = editMrMrsException(splitedFileList)
#print(checkMrMrsList)


def editQuotesException(fileList):
    i = 1
    end = len(fileList)
    for i in range(end):
        cnt = fileList[i][1:].count('"')
        if (fileList[i][0] == '"'):
            if (fileList[i][1:].find('"') == -1):
                fileList[i-1] = fileList[i-1]+'"'
                fileList[i] = fileList[i][1:]
            elif (cnt > 0):
                fileList[i-1] = fileList[i-1]+'"'
                fileList[i] = fileList[i][1:]
    return fileList

#checkQuoteList = editQuotesException(checkMrMrsList)
#print(checkQuoteList)


def editEnterException(fileList):
    num = len(fileList)
    for index in range(num):
        fullIndex = len(fileList[index])
        i = 0
        while i < fullIndex:
            if(fileList[index][i].find('\n') != -1):
                if(fileList[index][i+1] != '\n'):
                    fileList[index] = fileList[index][:i] + " " + fileList[index][i+1:]
                    i = i+1
                elif(fileList[index][i+1] == '\n'):
                    fileList[index] = fileList[index][:i] + "\n" + fileList[index][i+1:]
                    i = i+2
            else:
                i = i+1
    return fileList

#checkEnterList = editEnterException(checkQuoteList)
#print(checkEnterList)


def convertBytes(fileList):
    num = len(fileList)
    convertedList = []
    for i in range(num):
        convertedList.append(bytes(fileList[i], 'utf-8'))
    return convertedList

def saveStr(filepath, fileList):
    with open(filepath + "1031_def_str.txt", "w") as w:
        for sent in fileList:
            w.write(sent)
        
#saveStr(filepath, checkEnterList)

def editPageNum(fileList):
    newList = []
    for sent in fileList:
        newList.append(re.sub(r"\n\n[0-9]\n\n", r" ", sent))
    return newList

#checkPageNumEdited = editPageNum(checkEnterList)


def checkTheExist(fileList):
    flagList = []
    for index in range(len(fileList)):
        check = fileList[index].split(" ")
        cnt = len(check)
        for i in range(cnt):
            if(check[i] == "the"):
                flagList.append(index)
    #print(flagList)
    newFlag = list(OrderedDict.fromkeys(flagList))
    #print(newFlag)
    for i in newFlag:
        print(fileList[i])
     
        
#AEX = checkTheExist(checkPageNumEdited)