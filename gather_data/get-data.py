#focus on gathering full articles 
import urllib.request as libreq

#ensure data directory is created. 

dir_name = "data"
file_name = "temp.txt"
from pathlib import Path
p = Path(dir_name)

if p.exists() and p.is_dir():
    print("Data Directory Exists.")

if (p / file_name).is_file():
    print("File Exists.")

def write_to_file(data, mode="a", d_name="data", f_name="temp.txt"):
    seperator = "#"
    seperator = seperator.rjust(50, seperator)      #filling the string '#'. Looks cleaner than adding 50 '#' on one line. 
    path = "{}/{}".format(d_name, f_name)
    with open(path, mode) as f:
        f.write(data.decode("utf-8"))
        f.write(seperator)

####Check what kind of data from the article I can get, ie. PDF, raw text, etc.
def search_via_id_list(date = 706, num = 1):
    #id_list format: YYDD.NNNN
    #NOTE: format changes based on date and number limitations respectively
    
    date = str(date).zfill(4)   #zfill is for number padding
    num = str(num)  .zfill(4)
    id = "{}.{}".format(date, num)
    url = "http://export.arxiv.org/api/query?id_list={}".format(id)
    with libreq.urlopen(url) as url:
        r = url.read()
    write_to_file(r, "a", dir_name, file_name)
search_via_id_list()

def check_pdf():
    #find all pdf links before the seperator, keeping track of number of seperators
    #   clean the link so only the pdf link is present
    #   add to a list of pdf links in new document
    #if no pdf link tag was found
    #   Save the count marked by seperator into a list of numbers. 
    #At end of function re-read the xml responses and find the sepeartors marked down in the list of numbers. 
    #   when corresponding seperator is found, save the xml response snippet into a new list of xmls responses for later analyzing. 
    xml_path = "{}/{}".format(dir_name, file_name)
    pdf_file_path = "all_pdfs.txt"
    pdf_path = "{}/{}".format(dir_name, pdf_file_path)
    count =  0
    with open(xml_path, "r", encoding="utf-8") as f:  
        target = "<link title={}".format('"pdf"')
        seperator = "#"
        seperator = seperator.rjust(50, seperator)
        for line in f:
            if target in line:
                #write the pdf link to a new file
                #increment sepatator count
                #first, I need to clean up the text to only extract the link from the line. 
                start = 'href="'
                end = '"'
                start_index = line.find(start)
                start_index += len(start)
                end_index = line.find(end, start_index)
                result = line[start_index:end_index] + "\n"
                with open(pdf_path, "a", encoding="utf-8") as p:
                    p.write(result)
            if seperator in line:
                count += 1
    print(count)
            
            
check_pdf()
#Search through a good amount 