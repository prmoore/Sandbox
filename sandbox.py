#declarations
fltMyFloat = float(7.124 / 5.456)
y = int(1)
strPrintString = ""
lstTestList = []

#code
#strPrintString = "My float is: " + str(fltMyFloat)
#print(strPrintString)


#list stuff
lstTestList.append("item 1")
lstTestList.append("item 2")
lstTestList.append("item 3")
lstTestList.append(4)


strPrintString = "List: "
for x in lstTestList:
    strPrintString = strPrintString + str(x) + ", "

print(strPrintString)
