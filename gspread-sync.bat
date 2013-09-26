@echo off

set logfile="c:\tasks\gspread-sync.log.txt"

c:\Python27\Scripts\gspread\download-spreadsheet.py .>> %logfile%

exit
