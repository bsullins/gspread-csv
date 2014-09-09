import csv
import gspread
import urllib
import codecs
from config import config


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
        filename = path + doc["doc"] + '-worksheet' + str(i) + '.csv'
        with open(filename, 'wb') as f:
            writer = csv.writer(f)
            content = worksheet.get_all_values()
            for row in content:
                new_row=[]
                for record in row:
                    record=record.encode('utf8')
                    new_row.append(record)
                try:
                    writer.writerow(new_row)
                except (UnicodeEncodeError, UnicodeDecodeError):
                    print "Caught unicode error"
    print '== Finished Writing: ' + filename + ' =='
print '====== FINISHED ======'
