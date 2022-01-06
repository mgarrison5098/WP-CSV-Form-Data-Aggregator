import os
import re
import html

def extractData(text):
  matches = re.findall(r'"(.+?)"',text)
  return ",".join(matches)

def form5Aggregator(fieldValue, dateValue):
    processedCSVLine = ""
    extractedString = extractData(fieldValue)
    dataArray = extractedString.split(",")

    processedCSVLine += getCompany(dataArray) + ","
    processedCSVLine += getCity(dataArray) + ","
    processedCSVLine += getCounty(dataArray) + ","
    processedCSVLine += getOpenings(dataArray) + ","
    processedCSVLine += getPostingLink(dataArray) + ","
    processedCSVLine += getIndustries(dataArray) + ","
    processedCSVLine += getOther(dataArray) + ","
    processedCSVLine += getFirstName(dataArray) + ","
    processedCSVLine += getLastName(dataArray) + ","
    processedCSVLine += getTitle(dataArray) + ","
    processedCSVLine += getEmail(dataArray) + ","
    processedCSVLine += getPhone(dataArray) + ","
    processedCSVLine += getMessage(dataArray) + ","
    processedCSVLine += getAcceptance(dataArray) + ","
    processedCSVLine += dateValue

    saveToFile(processedCSVLine)


def getCompany(array):
    if "company_name" in array :
        index = array.index("company_name")
        try:
            return '"{}"'.format(array[index+1])
        except IndexError:
            return ''
    else:
        return ''

def getCity(array):
    if "city_job_locations" in array :
        index = array.index("city_job_locations")
        try:
            return '"{}"'.format(array[index+1])
        except IndexError:
            return ''
    else:
        return ''

def getCounty(array):
    if "county_job_locations" in array :
        index = array.index("county_job_locations")
        try:
            return '"{}"'.format(array[index+1])
        except IndexError:
            return ''
    else:
        return ''

def getOpenings(array):
    if "job_openings" in array :
        index = array.index("job_openings")
        try:
            return '"{}"'.format(array[index+1])
        except IndexError:
            return ''
    else:
        return ''

def getPostingLink(array):
    if "job_postings_link" in array :
        index = array.index("job_postings_link")
        try:
            return '"{}"'.format(html.unescape(array[index+1]))
        except IndexError:
            return ''
    else:
        return ''

def getIndustries(array):
    if "industry_sector_alignment" in array and "other" in array :
        index_start = array.index("industry_sector_alignment")
        index_end = array.index("other")
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

def getOther(array):
    if "other" in array :
        index = array.index("other")
        try:
            return '"{}"'.format(array[index+1])
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

def getTitle(array):
    if "job_title" in array :
        index = array.index("job_title")
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

def getAcceptance(array):
    if "acceptance" in array :
        index = array.index("acceptance")
        try:
            return '"{}"'.format(array[index+1])
        except IndexError:
            return ''
    else:
        return ''

    
def saveToFile(line):
    if os.path.isfile("./exports/formID_5.csv"):
        file1 = open("./exports/formID_5.csv", "a")
        file1.write(line + '\n')
        file1.close()
    else:        
        file1 = open("./exports/formID_5.csv", "a")
        file1.write("company_name, city_job_locations, county_job_locations, job_openings, job_postings_link, industry_sector_alignment, other, first_name, last_name, job_title, email, phone_number, your_message, acceptance, date \n")
        file1.write(line)
        file1.close()
