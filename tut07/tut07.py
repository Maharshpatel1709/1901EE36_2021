import pandas as pd

def feedback_not_submitted():
    
    output_file_name = "course_feedback_remaining.xlsx"

    course_registered_by_all_students = pd.read_csv('course_registered_by_all_students.csv')

    course_feedback_submitted_by_students = pd.read_csv('course_feedback_submitted_by_students.csv')
    # dropping duplicate entries mistakenly submitted for two professors but same course_code and feedback_type 
    course_feedback_submitted_by_students = course_feedback_submitted_by_students.drop_duplicates(subset=['stud_roll','course_code','feedback_type'])

    course_master = pd.read_csv('course_master_dont_open_in_excel.csv', index_col='subno')

    studentinfo = pd.read_csv('studentinfo.csv', index_col='Roll No')

    list = []

    for i in range(len(course_registered_by_all_students)):

        roll = course_registered_by_all_students.loc[i, 'rollno']
        sub = course_registered_by_all_students.loc[i, 'subno']

        register_sem = course_registered_by_all_students.loc[i, 'register_sem']
        schedule_sem = course_registered_by_all_students.loc[i, 'schedule_sem']

        # computing non-zero bits in l-t-p
        ltp = course_master.loc[sub, 'ltp']
        ltp = ltp.split('-')
        count = 0
        for i in ltp:
            if float(i) != 0:
                count += 1
        
        # comparing non-zero l-t-p bits(count) with the number of entries present in course_feedback_submitted_by_students with given stud_roll and course_code
        try:
            if count > len(course_feedback_submitted_by_students.loc[(course_feedback_submitted_by_students['stud_roll'] == roll) & (course_feedback_submitted_by_students['course_code'] == sub)]):
                try:
                    name = studentinfo.loc[roll, 'Name']
                except:
                    name = "NA_IN_STUDENTINFO"
                try:
                    email = studentinfo.loc[roll, 'email']
                except:
                    email = "NA_IN_STUDENTINFO"
                try:
                    aemail = studentinfo.loc[roll, 'aemail']
                except:
                    aemail = "NA_IN_STUDENTINFO"
                try:
                    contact = studentinfo.loc[roll, 'contact']
                except:
                    contact = "NA_IN_STUDENTINFO"
                
                list.append([roll, register_sem, schedule_sem, sub, name, email, aemail, contact])
        
        # if entry with given stud_roll and course_code is not present in course_feedback_submitted_by_students then we add it to the list if count is non-zero
        except:
            if count != 0:
                try:
                    name = studentinfo.loc[roll, 'Name']
                except:
                    name = "NA_IN_STUDENTINFO"
                try:
                    email = studentinfo.loc[roll, 'email']
                except:
                    email = "NA_IN_STUDENTINFO"
                try:
                    aemail = studentinfo.loc[roll, 'aemail']
                except:
                    aemail = "NA_IN_STUDENTINFO"
                try:
                    contact = studentinfo.loc[roll, 'contact']
                except:
                    contact = "NA_IN_STUDENTINFO"
                
                list.append([roll, register_sem, schedule_sem, sub, name, email, aemail, contact])
                    
    # sorting list and creating .xlsx output file

    list = sorted(list, key = lambda x: x[0])

    feedback_not_submitted_dataframe = pd.DataFrame(list, columns = ["rollno","register_sem","schedule_sem","subno","Name","email","aemail","contact"])

    feedback_not_submitted_dataframe.to_excel(output_file_name, index=False)

    
feedback_not_submitted()