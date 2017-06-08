from collections import namedtuple
import sys
import os

"""Basic sript for generating command that will remove all explicitly stated
pages using tkpdf"""

def collectUserData():
    """Uply little thing to collect all the data we want from the user (feilds in named tuple)"""
    request = namedtuple("request", ["orginalDocName", "newDocName", "numPages", "pagesToRemove"])
    if(len(sys.argv)==1):
        print("name of the doc")
        request.orginalDocName = input()
        print("name of the output doc")
        request.newDocName = input()
    else:
        request.orginalDocName = sys.argv[1]
        request.newDocName = sys.argv[2]
    print("num of pages in doc")
    request.numPages = int(input())
    request.pagesToRemove = []
    pageRemoval = -1
    print("enter the pages that you want removed")

    while pageRemoval != "":
        pageRemoval = input()
        if pageRemoval.isdigit():
            pageRemoval = int(pageRemoval)
            if pageRemoval >= 1 and pageRemoval <= request.numPages:
                request.pagesToRemove.append(pageRemoval)
            else:
                print("this is not a page within bounds 1-%s" % request.numPages)
    return request

def cmdGen(requestu):
    """Formats the command that we want based on the usere request"""
    toolName = "pdftk"
    correctNums = " ".join([str(x) for x in range(1, request.numPages+1) if x not in request.pagesToRemove])
    cmd = "%s %s cat %s output %s"%(toolName, request.orginalDocName, correctNums, request.newDocName)
    return cmd

request = collectUserData()
#print(cmdGen(request))
os.system(cmdGen(request))
