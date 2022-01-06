import os
import re
import html

def extractData(text):
  matches = re.findall(r'"(.+?)"',text)
  return ",".join(matches)

def form1674Aggregator(fieldValue, dateValue):
    processedCSVLine = ""
    extractedString = extractData(fieldValue)
    dataArray = extractedString.split(",")

    processedCSVLine += getFirstName(dataArray) + ","
    processedCSVLine += getLastName(dataArray) + ","
    processedCSVLine += getEmail(dataArray) + ","
    processedCSVLine += getPhone(dataArray) + ","
    processedCSVLine += getMethod(dataArray) + ","
    processedCSVLine += getMessage(dataArray) + ","
    processedCSVLine += dateValue

    saveToFile(processedCSVLine)




def getMethod(array):
    if "preferred_contact_method" in array and "your_message" in array :
        index_start = array.index("preferred_contact_method")
        index_end = array.index("your_message")
        try:
            values = ""
            for item in range(index_start + 1, index_end):
                if item < index_end - 1 and (index_end - 1) - (index_start + 1) > 1:
                    values += array[item] + ", "
                else:
                    values += array[item]
            return '"{}"'.format(values)
        except IndexError:
            return ''
    else:
        return ''


def getFirstName(array):
    if "first_name" in array :
        index = array.index("first_name")
        try:
            return '"{}"'.format(array[index+1])
        except IndexError:
            return ''
    else:
        return ''

def getLastName(array):
    if "last_name" in array :
        index = array.index("last_name")
        try:
            return '"{}"'.format(array[index+1])
        except IndexError:
            return ''
    else:
        return ''


def getEmail(array):
    if "email" in array :
        index = array.index("email")
        try:
            return '"{}"'.format(array[index+1])
        except IndexError:
            return ''
    else:
        return ''

def getPhone(array):
    if "phone_number" in array :
        index = array.index("phone_number")
        try:
            return '"{}"'.format(array[index+1])
        except IndexError:
            return ''
    else:
        return ''

def getMessage(array):
    if "your_message" in array :
        index = array.index("your_message")
        try:
            return '"{}"'.format(array[index+1])
        except IndexError:
            return ''
    else:
        return ''


    
def saveToFile(line):
    if os.path.isfile("./exports/formID_1674.csv"):
        file1 = open("./exports/formID_1674.csv", "a")
        file1.write(line + '\n')
        file1.close()
    else:        
        file1 = open("./exports/formID_1674.csv", "a")
        file1.write("first_name, last_name, email, phone_number, preferred_contact_method, your_message, date \n")
        file1.write(line)
        file1.close()
