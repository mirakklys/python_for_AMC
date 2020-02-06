#!/usr/bin/python3.7
### GLOBAL DECLARATIONS
### All text after %%% sign will go to comments in LaTeX-based AMC

### imports

import sys
import os.path

### declarations

quizFile = open('Qs.txt', encoding = "utf8") 
quizQs = quizFile.read().splitlines()
quizFile.close()
outfile = open('prcssdQs.txt', 'wt', encoding = "utf8")
count = 1
questionNumber = 0

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

def outfileBeg(argQuizMulti, qmult = '', horiz = False):
	global questionNumber
	questionNumber = questNum()
	horizLine = ''
	if horiz == True:
		horizLine = '    \\begin{multicols}{5}\n'
	outfile.writelines('\\element{general}{\n  \\begin{question' + qmult + '}{' + questionNumber + '}\n    ' + argQuizMulti + '\n' + horizLine + '    \\begin{choices}\n')

### function to finish the question

def outfileEnding(qmult = '', horiz = False):
	horizLine = ''
	if horiz == True:
		horizLine = '    \\end{multicols}\n'
	outfile.writelines('    \\end{choices}\n' + horizLine + '  \\end{question' + qmult + '}\n} % element\n')

### functions for correct and wrong answers

def correctChoice(choice):
	outfile.writelines('      \\correctchoice{' + choice + '}\n')

def wrongChoice(choice):
	outfile.writelines('      \\wrongchoice{' + choice + '}\n')

### inputs for test

copyNumber = input("How many copies will you need? ")
try:
	copyNumber = int(copyNumber)
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

dateOfTestM = monthList[month] + " " + str(day) + ", " + str(year)

### FIRST PART OF AMC FILE

outfile.writelines('''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\\documentclass[a4paper,11pt]{article}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Declaring packages
\\usepackage[utf8x]{inputenc}
\\usepackage[T1]{fontenc}
\\usepackage[box,completemulti,separateanswersheet]{automultiplechoice}
\\usepackage{graphicx}
\\graphicspath{{.//}}
\\usepackage{multicol}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Starting of the document
\\begin{document}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Student's name part
\\hfill
	\\fbox{
		\\begin{minipage}{.5\\linewidth}
		Firstname and lastname:\\\\
		\\vspace*{.1cm}\\dotfill
		\\vspace*{1mm}
		\\end{minipage}
	} % fbox
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Document properties
\\AMCrandomseed{1237893}
\\def\\AMCformQuestion#1{\\vspace{\\AMCformVSpace}\\par{\\bf Q#1:} }
\\AMCformVSpace=0.3ex
\\AMCformHSpace=0.3ex
\\setdefaultgroupmode{withoutreplacement}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Grouping the questions-answers\n''')

### QUESTIONS LOOP

### loop for simple questions

for each in range(len(quizQs)):
	if each == 0 and quizQs[0][0:3] == 'qqq':
		questionNumber = questNum()
		outfileBeg(quizQs[0][4:])
	elif quizQs[each][0:3] == '+++':
		correctChoice(quizQs[each][3:])
	elif quizQs[each][0:3] == '---':
		wrongChoice(quizQs[each][3:])
	elif quizQs[each][0:3] == 'qqq':
		questionNumber = questNum()
		outfileEnding()
		outfileBeg(quizQs[each][3:])
	else:
		continue

outfileEnding()

### loop for mult questions

if os.path.exists('Qms.txt'):
	quizMultiFile = open('Qms.txt', encoding = 'utf8') 
	quizQms = quizMultiFile.read().splitlines()
	quizMultiFile.close()
	multSymbole = '\\begin{flushleft}\n  {\\bf Questions using the sign \\multiSymbole{} have several correct answers}\n\\end{flushleft}'
	for each in range(len(quizQms)):
		if each == 0 and quizQms[0][0:3] == 'qmq':
			outfileBeg(quizQms[0][4:], 'mult')
		elif quizQms[each][0:3] == '+++':
			correctChoice(quizQms[each][3:])
		elif quizQms[each][0:3] == '---':
			wrongChoice(quizQms[each][3:])
		elif quizQms[each][0:3] == 'qmq':
			outfileEnding('mult')
			outfileBeg(quizQms[each][3:], 'mult')
		else:
			continue
	outfileEnding('mult')

### loop for horiz questions

if os.path.exists('Qhs.txt'):
	quizHorizFile = open('Qhs.txt', encoding = 'utf8') 
	quizQhs = quizHorizFile.read().splitlines()
	quizHorizFile.close()
	for each in range(len(quizQhs)):
		if each == 0 and quizQhs[0][0:3] == 'qhq':
			outfileBeg(quizQhs[0][4:],horiz = True)
		elif quizQhs[each][0:3] == '+++':
			correctChoice(quizQhs[each][3:])
		elif quizQhs[each][0:3] == '---':
			wrongChoice(quizQhs[each][3:])
		elif quizQhs[each][0:3] == 'qhq':
			outfileEnding(horiz = True)
			outfileBeg(quizQhs[each][3:], horiz = True)
		else:
			continue
	outfileEnding(horiz = True)

### LAST PART OF AMC FILE

outfile.writelines('''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Actual test sheets
\\onecopy{''' + str(copyNumber) + '''}{
  %%% Beginning of the test sheet header
  %%% Exam Name
  \\begin{flushleft}
  {\\bf ''' + examName + '''}
  \\end{flushleft}
  %%% Exam Date
  \\begin{minipage}{.4\\linewidth}
  \\bf '''+ dateOfTestM + ''' %date if needed
  \\end{minipage}
  \\vspace{1ex}''' + multSymbole + '''
  %%% Questions


  \\insertgroup{general}
  \\AMCcleardoublepage 
  %%% Use either \\clearpage or \\AMCcleardoublepage options. Double page will result in even number of pages for questions, so that you can print out questions double-sided and answer sheets separately
  %%% Beginning of the answer sheet
  \\AMCformBegin{
    %%% Student ID number
    \\AMCcode{etu}{9} 
    \\begin{minipage}[b]{9cm}
    \\includegraphics[width=8cm]{wrongCorrect.png}\\\\ % Wrong and correct filling of the sheet
    $\\leftarrow{}$\\hspace{0pt plus 2cm} please encode your student number in the boxes to the left,
    and write your first and last names below.$\\downarrow{}$\\hspace{0pt plus 1cm} \\vspace*{.2cm}
    \\vspace{1ex}
    \\hfill\\namefield{
      \\fbox{
        \\begin{minipage}{.9\\linewidth}
        First name and last name:\\\\
        \\vspace*{.1cm}\\dotfill
        \\vspace*{0.5mm}
        \\end{minipage}
      } % fbox
    } % namefield
    \\hfill\\vspace{5ex}\\end{minipage}\\hspace*{\\fill}
  } % \\AMCformBegin
  %%% Beginning of the answer sheet body 
  \\begin{center}
    \\bf\\normalsize Answers must be given exclusively on this sheet:
    answers given on the other sheets will be ignored.
  \\end{center}
  %%% Ending of the answer sheet
  \\begin{multicols}{2}
  \\AMCform
  \\end{multicols}
  \\AMCcleardoublepage 
} % onecopy
\\end{document}''')

### Finalised programme

outfile.close()
