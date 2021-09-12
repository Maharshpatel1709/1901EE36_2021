import os
import csv
import openpyxl

os.mkdir('output_individual_roll')
os.mkdir('output_by_subject')

# Task - 1

with open('regtable_old.csv', 'r') as csvfile:

    memory = []

    csvreader = csv.DictReader(csvfile)

    dict = {}
    for row in csvreader:
        
        list = []
        list.append(row['rollno'])
        list.append(row['register_sem'])
        list.append(row['subno'])
        list.append(row['sub_type'])

        if(row['rollno'] in memory):
            dict[row['rollno']].append(list)
        else:
            memory.append(row['rollno'])
            dict[row['rollno']] = [list]

for rollno in dict:
    path = 'output_individual_roll/' + rollno + '.xlsx'

    wb = openpyxl.Workbook()
    sheet = wb.active

    header = ['rollno', 'register_sem', 'subno', 'sub_type']
    sheet.append(header)

    for row in dict[rollno]:
        sheet.append(row)

    wb.save(path)


# Task - 2

with open('regtable_old.csv', 'r') as csvfile:

    memory = []

    csvreader = csv.DictReader(csvfile)

    dict = {}
    for row in csvreader:
        
        list = []
        list.append(row['rollno'])
        list.append(row['register_sem'])
        list.append(row['subno'])
        list.append(row['sub_type'])

        if(row['subno'] in memory):
            dict[row['subno']].append(list)
        else:
            memory.append(row['subno'])
            dict[row['subno']] = [list]

for subno in dict:
    path = 'output_by_subject/' + subno + '.xlsx'

    wb = openpyxl.Workbook()
    sheet = wb.active

    header = ['rollno', 'register_sem', 'subno', 'sub_type']
    sheet.append(header)

    for row in dict[subno]:
        sheet.append(row)

    wb.save(path)

