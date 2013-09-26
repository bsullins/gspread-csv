import csv
import gspread
import urllib
from config import config

#functions
def norm(s):
    if type(s) == unicode:
        return s.encode('utf-8').strip()
    else:
        return s

#config
username = config['USERNAME']
password = config['PASSWORD']
docs = [
    {"doc": "My 1st Spreadsheet Name"},
    {"doc":"My 2nd Spreadsheet Name"} 
    ]


# login first
client = gspread.login(username, password)

#process doc list
for doc in docs:
    spreadsheet = client.open(doc["doc"])
    for i, worksheet in enumerate(spreadsheet.worksheets()):
        filename = doc["doc"] + '-worksheet' + str(i) + '.csv'
        #filename = doc + '.csv'
        with open(filename, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(worksheet.get_all_values())
    print '== Finished Writing: ' + filename + ' =='
print '====== FINISHED ======'
