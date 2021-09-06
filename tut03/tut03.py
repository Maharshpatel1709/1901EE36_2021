with open('regtable_old.csv', 'r') as file:

    memory = []

    for line in file:
        row = line.split(',')

        rollno = row[0]
        register_sem = row[1]
        subno = row[3]
        sub_type = row[8]

        if(rollno == 'rollno'):
            continue

        path = 'output_individual_roll/' + rollno + '.csv'

        if(rollno in memory):
            with open(path, 'a') as f:
                f.write(rollno + ',' + register_sem + ',' + subno + ',' + sub_type)
        else:
            memory.append(rollno)
            with open(path, 'w') as f:
                f.write('rollno,' + 'register_sem,' + 'subno,' + 'sub_type\n')
                f.write(rollno + ',' + register_sem + ',' + subno + ',' + sub_type)


with open('regtable_old.csv', 'r') as file:

    memory = []

    for line in file:
        row = line.split(',')

        rollno = row[0]
        register_sem = row[1]
        subno = row[3]
        sub_type = row[8]

        if(rollno == 'rollno'):
            continue

        path = 'output_by_subject/' + subno + '.csv'

        if(subno in memory):
            with open(path, 'a') as f:
                f.write(rollno + ',' + register_sem + ',' + subno + ',' + sub_type)
        else:
            memory.append(subno)
            with open(path, 'w') as f:
                f.write('rollno,' + 'register_sem,' + 'subno,' + 'sub_type\n')
                f.write(rollno + ',' + register_sem + ',' + subno + ',' + sub_type)
