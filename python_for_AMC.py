#!/usr/bin/python3.7
### GLOBAL DECLARATIONS
### All text after %%% sign will go to comments in LaTeX-based AMC

### imports

import sys

### declarations

quizFile = open('Qs.txt', encoding = "utf8") 
quizQs = quizFile.read().splitlines()
quizFile.close()
outfile = open('prcssdQs.txt', 'wt', encoding = "utf8")
count = 1
questionNumber = 0

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
%% Grouping the questions-answers
\\element{general}{''')

### QUESTIONS LOOP

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

### for loops for questions

for each in range(len(quizQs)):
	if each == 0:
		if quizQs[0][0:3] == 'qqq':
			questionNumber = questNum()
			outfile.writelines('\n  \\begin{question}{' + questionNumber + "}\n    " + quizQs[0][4:] + "\n    \\begin{choices}\n")
		else:
			continue
	elif quizQs[each][0:3] == '+++':
		outfile.writelines('      \\correctchoice{' + quizQs[each][3:] + '}\n')
	elif quizQs[each][0:3] == '---':
		outfile.writelines('      \\wrongchoice{' + quizQs[each][3:] + '}\n')
	elif quizQs[each][0:3] == 'qqq':
		questionNumber = questNum()
		outfile.writelines('''    \\end{choices}
  \\end{question}
} % element
\\element{general}
{
  \\begin{question}{''' + questionNumber + "}\n    " + quizQs[each][3:] + "\n    \\begin{choices}\n")
	else:
		continue

### LAST PART OF AMC FILE

outfile.writelines('''    \\end{choices}
  \\end{question}
} % element
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
  \\bf '''+ str(dateOfTestM) + ''' %date if needed
  \\end{minipage}
  \\vspace{1ex}
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
