#!/usr/bin/python3.7
### GLOBAL DECLARATIONS
### All text after %%% sign will go to comments in LaTeX-based AMC

### imports

import sys
import os.path
import time
import urllib.request

### declarations

quizFile = open('Qs.txt', encoding = "utf8") 
quizQs = [each.strip() for each in quizFile if len(each) > 1]
#for each in quizFile:
#	if len(each) > 1:
#		quizQs.append(each.strip())
quizFile.close()
outfile = open('prcssdQs.txt', 'wt', encoding = "utf8")
count = 1
questionNumber = 0
columnNum = '5'
multSymbole = ''

### Preparing the questions for LaTeX

prohibSymbs = ['\\', '%', '$', '{', '_', '|', '™', '£', '#', '&', '}', '§', '<', '®', '©', '°', '>', '~', '^', 'ULINEDSPACE']
escSymbs = ['\\\\', '\\%', '\\$', '\\{', '\\_', 'extbar', 'exttrademark', '\\pounds', '\\#', '\\&', '\\}', '\\S', '\\txtless', '\\textregistered', '\\copyright', '\\textdegree', '\\textgreater', '\\~{}', '\\^{}', ]

for every in range(len(quizQs)):
	for each in range(len(prohibSymbs)):
		if prohibSymbs[each] in quizQs[every]:
			quizQs[every] = quizQs[every].replace(prohibSymbs[each], escSymbs[each])

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
	global columnNum
	global questionNumber
	questionNumber = questNum()
	horizLine = ''
	if horiz == True:
		horizLine = '    \\begin{multicols}{' + columnNum + '}\n'
	outfile.writelines('\\element{general}{\n  \\begin{question' + qmult + '}{' + qmult + questionNumber + '}\n    ' + argQuizMulti + '\n' + horizLine + '    \\begin{choices}\n')

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

### function to code column number

def columnNumber(value):
	global columnNum
	global questionNumber
	try:
		int(value)
		columnNum = value
	except:
		thisIsSparta = int(questionNumber[1:]) + 1
		if thisIsSparta < 10:
			questNumb = "q00" + str(thisIsSparta)
		elif thisIsSparta >= 100:
			questNumb = "q" + str(thisIsSparta)
		else:
			questNumb = "q0" + str(thisIsSparta)
		print('The question ' + questNumb + ' will have the default number of columns {5}')

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
studentIdNumber = input("How many digits are in student ID number? (2-12 digits allowed) ")
try:
	studentId = int(studentIdNumber)
except:
	print("Wrong value. Should be a number, not a string")
	sys.exit()
if studentId < 2 or studentId > 12:
	print("Error! Should be between 2 and 12 digits")
	sys.exit()
askMult = input("Will you have any multiple correct choice answers? (y/n)")
if askMult.lower() == 'y' or askMult.lower() == 'yes':
	multSymbole = '\\begin{flushleft}\n  {\\bf Questions using the sign \\multiSymbole{} have several correct answers}\n\\end{flushleft}'

### date processing

monthList = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
months31 = (0,2,4,6,7,9,11)
months30 = (3,7,8,10)

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
\\usepackage{textcomp}

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
countTemp = 0
while len(quizQs) > 0:
	temp = []
	countTemp += 1 
	for each in range(len(quizQs)):
		if each == 0:
			temp.append(quizQs[0])
		elif quizQs[each].startswith('+++') or quizQs[each].startswith('---'):
			temp.append(quizQs[each])
		else:
			break
	print('Question number {} is being processed'.format(countTemp))
	
	for each in range(len(temp)):
		if quizQs[each].startswith('qqq'):
			outfileBeg(quizQs[each][3:])
			time.sleep(0.05)
			print('...question body added')
		elif quizQs[each].startswith('qmq'):
			outfileBeg(quizQs[each][3:], 'mult')
			time.sleep(0.05)
			print('...question body added')
		elif quizQs[each].startswith('qh'):
			columnNumber(quizQs[each][2])
			outfileBeg(quizQs[each][3:], horiz = True)
			time.sleep(0.05)
			print('...question body added')
		elif quizQs[each].startswith('+++'):
			correctChoice(quizQs[each][3:])
			time.sleep(0.05)
			print('...correct answer added')
		elif quizQs[each].startswith('---'):
			wrongChoice(quizQs[each][3:])
			time.sleep(0.05)
			print('...incorrect answer added')
		else:
			time.sleep(0.05)
			print('...unnecessary stuff removed')
			continue
	if temp[0].startswith('qqq'):
		outfileEnding()
	elif temp[0].startswith('qmq'):
		outfileEnding('mult')
	elif temp[0].startswith('qh'):
		outfileEnding(horiz = True)
	print('Question number {} was processed successfully'.format(countTemp))
	time.sleep(0.15)
	for each in range(len(temp)):
		quizQs.pop(0)

### LAST PART OF AMC FILE

outfile.writelines('''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Actual test sheets
\\onecopy{''' + copyNumber + '''}{
  %%% Beginning of the test sheet header
  %%% Exam Name
  \\begin{flushleft}
  {\\bf ''' + examName + '''}
  \\end{flushleft}
  %%% Exam Date
  \\begin{minipage}{.4\\linewidth}
  \\bf '''+ dateOfTestM + ''' %date if needed
  \\end{minipage}
  \\vspace{1ex}''' + multSymbole + '''\\ \n \\
  %%% Questions


  \\insertgroup{general}
  \\AMCcleardoublepage 
  %%% Use either \\clearpage or \\AMCcleardoublepage options. Double page will result in even number of pages for questions, so that you can print out questions double-sided and answer sheets separately
  %%% Beginning of the answer sheet
  \\AMCformBegin{
    %%% Student ID number
    \\AMCcode{etu}{''' + studentIdNumber + '''} 
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

try:
	pathForPNG = os.getcwd()
	url = 'https://github.com/mirakklys/python_for_AMC/blob/master/wrongCorrect.png'
	urllib.request.urlretrieve(url, pathForPNG)
	print('I am downloading !wrongCorrect.png! that should be placed in the final test folder')
except:
	print('I couldn\'t download !wrongCorrect.png! from the GitHub, download it manually from https://github.com/mirakklys/python_for_AMC/blob/master/wrongCorrect.png and place in the final test folder')
