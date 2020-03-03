#!/usr/bin/python3.7
### GLOBAL DECLARATIONS
### All text after %%% sign will go to comments in LaTeX-based AMC

### imports

import sys

### declarations

quizFile = open('Qos.txt', encoding = "utf8") 
quizQs = quizFile.read().splitlines()
quizFile.close()
outfile = open('prcssdOpnQs.txt', 'wt', encoding = "utf8")
count = 1
questionNumber = 0
quizQos = []

for each in quizQs:
	if each != '':
		quizQos.append(each.strip())
	else:
		continue

### FUNCTIONS

### function to number the question

def questNum():
	global count
	if count < 10:
		questNum = "q00" + str(count)
	elif count >= 100:
		questNum = "q" + str(count)
	else:
		questNum = "q0" + str(count)
	count += 1
	return questNum

### function to start the question

def outfileBeg(beginning):
	global questionNumber
	global numberOfLines
	questionNumber = questNum()
	outfile.writelines('\\begin{question}{' + questionNumber + '}\n  ' + beginning + '\n  \\AMCOpen{lines=' + str(numberOfLines) + '}{\\wrongchoice[W]{0}\\scoring{0}')

### function to finish the question

def outfileEnding():
	outfile.writelines('\\end{question}\n')

### functions for correct and partially correct answers

def correctChoice():
	global maxPoints
	outfile.writelines('  \\correctchoice[C]{' + str(maxPoints) + '}\\scoring{' + str(maxPoints) + '}}')

def partialCorrectChoice():
	global pointsPerCorrect
	global correctPoints
	global numberOfLines
	for each in range(numberOfLines - 1):
		outfile.writelines('  \\wrongchoice[P]{' + str(round(correctPoints,2)) + '}\\scoring{' + str(round(correctPoints,2)) + '}')
		correctPoints = correctPoints + pointsPerCorrect

### inputs for test

copyNumber = input("How many copies will you need? ")
try:
	int(copyNumber)
except:
	print("Wrong value. Should be a number, not a string")
	sys.exit()
dateOfTest = input("Enter the date of the exam in the format YYYYMMDD: ")
try:
	dateCheck = int(dateOfTest)
except:
	print("Wrong value. Should be a number, e.g. 20201231")
	sys.exit()
if dateCheck < 20200101 or dateCheck > 20991231:
	print("Wrong date format! Revise the date.")
	sys.exit()
examName = input("Please name your exam (if two lines needed place two backslash \\\\ on the linebreak): ")

### date processing

monthList = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
months31 = [0,2,4,6,7,9,11]
months30 = [3,7,8,10]

yearInt = int(dateOfTest[:4])
monthInt = int(dateOfTest[4:6])
dayInt = int(dateOfTest[6:])

if yearInt >= 2020:
	year = yearInt
else:
	print("Wrong date format! Revise the exam year.")
	sys.exit()

if monthInt < 13 and monthInt > 0:
	month = monthInt - 1
else:
	print("Wrong date format! Revise the month.")
	sys.exit()

if month in months30 and dayInt < 31:
	day = dayInt
elif month in months31 and dayInt < 32:
	day = dayInt
elif month == 1 and year % 4 == 0 and dayInt < 30:
	day = dayInt
elif month == 1 and year % 4 != 0 and dayInt < 29:
	day = dayInt
else:
	print("Wrong date format! Revise the date.")
	sys.exit()

dateOfTestStr = monthList[month] + " " + str(day) + ", " + str(year)

### FIRST PART OF AMC FILE

outfile.writelines('''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\\documentclass[a4paper]{article}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\\usepackage[utf8x]{inputenc}    
\\usepackage[T1]{fontenc}
\\usepackage[box,completemulti]{automultiplechoice}    
\\usepackage{graphicx}
\\graphicspath{{.//}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\\begin{document}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\\onecopy{''' + copyNumber + '''}{    
%%% beginning of the test sheet header:    
\\vspace*{.5cm}
\\begin{flushleft}
{\\bf ''' + examName + ''' \\hfill '''+ dateOfTestStr + '''}
\\end{flushleft}

\\namefield{
  \\fbox{
    \\begin{minipage}{.9\\linewidth}
    First name and last name:\\\\
    \\vspace*{.01cm}\\dotfill
    \\vspace*{0.5mm}
    \\end{minipage}
  } % fbox
} % namefield
	
\\vspace{1ex}

%%% end of the header\n''')

### QUESTIONS LOOP

### loop for open answer questions

quizMod = [each[:4] for each in quizQos]
lineNumbers = [each[2] for each in quizMod]
pointsMax = [each[3] for each in quizMod]
for each in range(len(quizQos)):
	numberOfLines = int(lineNumbers[each])
	maxPoints = int(pointsMax[each])
	pointsPerCorrect = maxPoints / numberOfLines
	correctPoints = pointsPerCorrect
	if each == 0 and quizQos[0][0:2] == 'qo':
		outfileBeg(quizQos[0][4:])
		partialCorrectChoice()
		correctChoice()
	elif quizQos[each][0:2] == 'qo':
		outfileEnding()
		outfileBeg(quizQos[each][4:])
		partialCorrectChoice()
		correctChoice()
	else:
		continue

outfileEnding()

### LAST PART OF AMC FILE

outfile.writelines('''
}   

\\end{document}''')

### Finalised programme

outfile.close()
