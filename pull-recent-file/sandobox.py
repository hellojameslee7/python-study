# Goal of this: Come up with script that will pull latest file using the date details from the file name

# Steps that I will take:
# Based on the type of file extract the date string from the filenames.
# Convert it to date object.
# Find latest date.
# Filter filename using the last date.

#Goal of this project: Come up with a function that can pull the latest file from a list of file based on some parameters provided to the function

#Got help from this stackoverflow site: https://stackoverflow.com/questions/21184018/get-latest-file-based-on-filename-python
#Also this site was v helpful for testing reg ex: https://regex101.com/
#Thanks googs: https://developers.google.com/edu/python/regular-expressions

"""
Some additional notes for self:
re.match always starts at the beginning of the string.
re.search steps through the string from the start looking for the first match. It stops when it finds a match.
re.findall returns a list of all the search matches.
"""

filenames = [
    'RandomStuffReport202104051119093gmawt.csv',
    'RandomStuffReport202104111119093gmawt.csv',
    'RandomStuffReport202104121119093gmawt.csv',
    'Random_Stuff_Report_2021-04-05T0905_3gmawt.csv',
    'Random_Stuff_Report_2021-04-11T0905_3gmawt.csv',
    'Random_Stuff_Report_2021-04-12T0905_3gmawt.csv',
    'Random_Stuff_Report_2021-05-12T0905_3gmawt.csv',
    'Random_Stuff_Report_2021-06-12T0905_3gmawt.csv',
    'Another_Report_Test-20131216.10_52-en.csv',
    'Another_Report_Test-20141216.10_52-en.csv',
    'Another_Report_Test-20141217.10_52-en.csv'
    'somany_reports_2020_20201228.txt'
    'somany_reports_2020_20210216.csv'
] # Used in place of `os.listdir(....)`

import re
import datetime

date_pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
alt_date_pattern = re.compile(r'(\d{4})(\d{2})(\d{2})')

def get_date(filename):
    matched = date_pattern.search(filename)
    if not matched:
        matched = alt_date_pattern.search(filename)
    y, m, d = map(int, matched.groups())
    return datetime.date(y, m, d)

dates = (get_date(fn) for fn in filenames)
dates = (d for d in dates if d is not None)
last_date = max(dates)
last_date = last_date.strftime('%Y-%m-%d')
filenames = [fn for fn in filenames if last_date in fn]
for fn in filenames:
    print(fn)


"""

filenames = [
    'RandomStuffReport202104051119093gmawt.csv',
    'RandomStuffReport202104111119093gmawt.csv',
    'RandomStuffReport202104121119093gmawt.csv',
    'Random_Stuff_Report_2021-04-05T0905_3gmawt.csv',
    'Random_Stuff_Report_2021-04-11T0905_3gmawt.csv',
    'Random_Stuff_Report_2021-04-12T0905_3gmawt.csv',
    'Another Report_Test-12-16-2013.10_52-en.zip',
] 

def compare_dates(fn1,fn2):
        # parse the date information
        day1,month1,year1 = fn1.split(".")[0].split("-")[-3:]
        day2,month2,year2 = fn2.split(".")[0].split("-")[-3:]
        ret = cmp(year1,year2) # first compare the years
        if ret != 0:
            return ret
        ret = cmp(month1,month2) # if years equal, compare months
        if ret != 0:
            return ret
        return cmp(day1,day2) # if months equal, compare days

filenames.sort(cmp=compare_dates)
"""
