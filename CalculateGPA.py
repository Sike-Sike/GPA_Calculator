import sys
import csv


def calc_gpa(locn):
    grad_sch = { 'O':10 , 'A+':9 , 'A':8.5 , 'B+':8 , 'B':7 , 'C':6 , 'P':5 , 'F':0 , 'FE':0 , 'I':0 }
    cred_total = 0
    cred_earn = 0
    grad_total = 0
    weight_sum = 0
    sub_num = 0
    with open(locn, 'r') as file:
        reader = csv.reader(file)
        lnum=0
        for row_no, row in enumerate(reader):
            if(row_no==0):
                continue
            else:
                if(grad_sch[row[2]] != 0):
                    cred_earn += int(row[1])
                cred_total += int(row[1])
                print(row[0].upper()," : ",grad_sch[row[2]])
                weight_sum += int(row[1])*grad_sch[row[2]]
                lnum+=1
        sub_num = lnum
    print('\nNumber of subjects : ',sub_num)
    print('\nEarned Credits/Total Credits',cred_earn,'/',cred_total)
    print('\nGPA',round(weight_sum/cred_total,2))

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        print(sys.argv[1]+'\n')
        calc_gpa(sys.argv[1])
    else:
        print('Incorrect Arguments')
