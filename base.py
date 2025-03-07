import subprocess
#this script asks for an input of 1, 2, or 3 in order to choose whether to run
#f_analysis.py, f_analyis2.py or both files
answers = ['1', '2', '3']

while True:
    a = input()
    if not a in answers:
        print("Enter valid response")
        continue
    else:
        break

if int(a) == 1:
    subprocess.call(['python', 'f_analysis.py'])
elif int(a) == 2:
    subprocess.call(['python', 'f_analysis2.py'])
else:
    p1 = subprocess.Popen(['python', 'f_analysis.py'])
    p2 = subprocess.Popen(['python', 'f_analysis2.py'])
    p1.wait()
    p2.wait()