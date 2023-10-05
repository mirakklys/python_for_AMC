#!/usr/bin/env python3
### GLOBAL DECLARATIONS
### All text after %%% sign will go to comments in LaTeX-based AMC

### imports

import sys
import os.path
import time
import urllib.request as ulr

### logging function


def logFileF(strToLog, n = 0, date = True, zone = False):
  
  with open('log.txt', 'a+') as logFile:
    
    timeZone = ' - ' + time.strftime("%z - %Z") if zone else '' 
    dateStr = '***' + time.strftime("%H:%M:%S") + timeZone + '\n' if date else ''
    newLine = '\n'
    logFile.write(dateStr + strToLog + newLine * n)
  

### inputs for test
logFileF('~~~Date: ' + time.strftime('%Y %B %d %A'), 1, zone = True)

while True:
  
  copyNumber = input("How many copies will you need? ")
  if int(copyNumber):
    
    break
  else:
    
    print("Wrong value. Should be a number, not a string")
    
### date processing
monthList = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
months31 = (0,2,4,6,7,9,11)
months30 = (3,7,8,10)

dateOfTest = input("Enter the date of the exam in the format YYYYMMDD: ")

while True:
  
  try:
    
    dateCheck = int(dateOfTest)
  except:
    
    print("Wrong value. Should be a number, e.g. 20201231")
    dateOfTest = input("Enter the date of the exam in the format YYYYMMDD: ")
  else:
    
    if dateCheck >= 20000101 and dateCheck <= 20991231:
      
      yearInt = int(dateOfTest[:4])
      monthInt = int(dateOfTest[4:6])
      dayInt = int(dateOfTest[6:])

      if monthInt < 13 and monthInt > 0:
        
        month = monthInt - 1
        if dayInt > 0 and ((month in months30 and dayInt < 31) or\
        (month in months31 and dayInt < 32) or (month == 1 and\
        yearInt % 4 == 0 and dayInt < 30) or (month == 1 and yearInt\
        % 4 != 0 and dayInt < 29)):
          
          day = dayInt
          break
        else:
          
          print("Wrong date format! Revise the date.")
      else:
        
        print("Wrong date format! Revise the month.")
    else:
      
      print("Wrong date format! Revise the date.")
    
    dateOfTest = input("Enter the date of the exam in the format YYYYMMDD: ")

dateOfTestM = monthList[month] + " " + str(day) + ", " + str(yearInt)

### exam name to put on answer sheet
examName = input("Please name your exam (if two lines needed place two backslash \\\\ on the linebreak): ")

### set up ID of a student
studentIdNumber = input("How many digits are in student ID number? (2-30 digits allowed): ")

while True:
  
  try:
    
    studentId = int(studentIdNumber)
  except:
    
    print("Wrong value. Should be a number, not a string")
    studentIdNumber = input("How many digits are in student ID number? (2-30 digits allowed): ")
  else:
    
    if studentId >= 2 and studentId <= 30:
      
      break
    else:
      
      print("Error! Should be between 2 and 30 digits")
      studentIdNumber = input("How many digits are in student ID number? (2-30 digits allowed): ")

### check if there are multiple correct choice questions, so that a special sign is put before the question
yess = ['y', 'yes']
askMult = input("Will you have any multiple correct choice answers? (y/n): ")
askMult = askMult.lower()
multSymbole = '\\begin{flushleft}\n  {\\bf Questions using the sign \\multiSymbole{} have several correct answers. Negative marking (-0.25 point) is applied to this question}\n\\\[1.5\\baselineskip]\n\\end{flushleft}' if askMult in yess else ''

### indicate if you want "None of the above" option

indicMulti = input("Do you want to have 'None of these answers are correct' option?: ")
indicateMulti = 'completemulti,' if indicMulti.lower() in yess else ''

### declarations

quizFile = open('Qs.txt', encoding = "utf8") 
quizQs = [each.strip() for each in quizFile if len(each) > 1]
quizFile.close()
outfile = open('prcssdQs.txt', 'wt', encoding = "utf8")

count = 1
questionNumber = '1'
columnNum = '5'

logFileF('   Exam name: ' + examName + '\n   Exam date: ' + dateOfTestM + '\n   Exam copies Number: ' + copyNumber + '\n   Exam ID number digits: ' + studentIdNumber + '\n   Exam multiple correct choice: ' + str(askMult in yess) + '\n', 1)
logFileF('... imports and script declarations are successful\n')

### Preparing the questions for LaTeX

prohibSymbs = ['\\', '%', '$', '{', '_', '|', '™', '£', '#', '&', '}', '§', '<', '®', '©', '°', '>', '~', '^', 'ULINEDSPACE', 'α', 'ν', 'β', 'ξ', 'Ξ', 'γ', 'Γ', 'δ', 'Δ', 'π', 'Π', 'ε', 'ρ', 'ζ', 'σ', 'Σ', 'η', 'τ', 'θ', 'Θ', 'υ', 'ι', 'φ', 'Φ', 'κ', 'χ', 'λ', 'Λ', 'ψ', 'Ψ', 'μ', 'ω', 'Ω', 'Å']
escSymbs = ['\\\\', '\\%', '\\$', '\\{', '\\_', '\\textbar', '\\texttrademark', '\\pounds', '\\#', '\\&', '\\}', '\\S', '\\txtless', '\\textregistered', '\\copyright', '\\textdegree', '\\textgreater', '\\~{}', '\\textsuperscript{}', '\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_', '$\\alpha$', '$\\nu$', '$\\beta$', '$\\xi$' , '$\\Xi$', '$\\gamma$', '$\\Gamma$', '$\\delta$', '$\\Delta$', '$\\pi$', '$\\Pi$', '$\\epsilon$', '$\\rho$', '$\\zeta$', '$\\sigma$', '$\\Sigma$', '$\\eta$', '$\\tau$', '$\\theta$', '$\\Theta$', '$\\upsilon$', '$\\iota$', '$\\phi$', '$\\Phi$', '$\\kappa$', '$\\chi$', '$\\lambda$', '$\\Lambda$', '$\\psi$', '$\\Psi$', '$\\mu$', '$\\omega$', '$\\Omega$', '\\AA']

for every in range(len(quizQs)):
  tempProhib = []
  for each in range(len(prohibSymbs)):
    if prohibSymbs[each] in quizQs[every]:
      quizQs[every] = quizQs[every].replace(prohibSymbs[each], escSymbs[each])
      if prohibSymbs[each] not in tempProhib:
        tempProhib.append(prohibSymbs[each])
logFileF('... replaced LaTeX-prohibited characters: ' + ', '.join(tempProhib) + '\n', date = False)

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
  horizLine = '    \\begin{multicols}{' + columnNum + '}\n' if horiz else ''
  outfile.writelines('\\element{general}{\n  \\begin{question' + qmult + '}{' + questionNumber + qmult + '}\n    ' + argQuizMulti + '\n' + horizLine + '    \\begin{choices}\n\\scoring{p=0}\n')

### function to finish the question

def outfileEnding(qmult = '', horiz = False):
  horizLine = '    \\end{multicols}\n' if horiz else ''
  outfile.writelines('    \\end{choices}\n' + horizLine + '  \\end{question' + qmult + '}\n} % element\n')

### functions for correct and wrong answers

def correctChoice(choice, qmqN):
  outfile.writelines('      \\correctchoice{' + choice + '}\\scoring{b=' + qmqN + '}\n')

def wrongChoice(choice):
  outfile.writelines('      \\wrongchoice{' + choice + '}\\scoring{b=0,m=-0.25}\n')

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
    print('The question ' + questNumb + ' will have the default number of columns - 5')

logFileF('... function declarations are successful\n', date = False)

### FIRST PART OF AMC FILE

outfile.writelines('''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\\documentclass[a4paper,11pt]{article}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Declaring packages
\\usepackage[utf8x]{inputenc}
\\usepackage[T1]{fontenc}
\\usepackage[box,''' + indicateMulti + '''separateanswersheet]{automultiplechoice}
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
%% Grouping the questions-answers\n\n''')
logFileF('... LaTeX header is written successfully\n', 1, date = False)

### QUESTIONS LOOP

### loop for simple questions
countTemp = 0
while len(quizQs) > 0:
  qmqNAnsw = '1'
  temp = []
  countTemp += 1 
  countTempStr = str(countTemp)
  for each in range(len(quizQs)):
    if each == 0:
      temp.append(quizQs[0])
    elif quizQs[each].startswith('+++') or quizQs[each].startswith('---'):
      temp.append(quizQs[each])
    else:
      break
  print('Question number {} is being processed'.format(countTemp))
  logFileF('...Question ' + countTempStr + ' is being processed\n')
  
  for each in range(len(temp)):
    if temp[each].startswith('qqq'):
      outfileBeg(temp[each][3:])
      time.sleep(0.1)
      print('...question body added')
      logFileF('...qestion ' + countTempStr + ' body added\n', date = False)
    elif temp[each].startswith('qm'):
      qmqNAnsw = str(round(1/int(temp[each][2]), 6))
      outfileBeg(temp[each][3:], 'mult')
      time.sleep(0.1)
      print('...question body added')
      logFileF('...qestion ' + countTempStr + ' body added\n', date = False)
    elif temp[each].startswith('qh'):
      columnNumber(temp[each][2])
      outfileBeg(temp[each][3:], horiz = True)
      time.sleep(0.1)
      print('...question body added')
      logFileF('...qestion ' + countTempStr + ' body added\n', date = False)
    elif temp[each].startswith('+++'):
      correctChoice(temp[each][3:], qmqNAnsw)
      time.sleep(0.1)
      print('...correct answer added')
      logFileF('...correct answer to qestion ' + countTempStr + ' added\n', date = False)
    elif temp[each].startswith('---'):
      wrongChoice(temp[each][3:])
      time.sleep(0.1)
      print('...incorrect answer added')
      logFileF('...incorrect answer to qestion ' + countTempStr + ' added\n', date = False)
    else:
      time.sleep(0.1)
      print('...unnecessary ' + temp[each] + ' stuff removed')
      logFileF('...trash ' + temp[each] + ' is disposed of\n', date = False)
      continue
  if temp[0].startswith('qqq'):
    outfileEnding()
  elif temp[0].startswith('qm'):
    outfileEnding('mult')
  elif temp[0].startswith('qh'):
    outfileEnding(horiz = True)
  print('Question number {} was processed successfully'.format(countTemp))
  logFileF('...Question ' + countTempStr + ' processed successfully\n', 1, date = False)
  time.sleep(0.1)
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
  \\vspace{1ex}''' + multSymbole + '''\n
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
logFileF('...LaTeX footer is written successfully\n', 1)

### Finalised programme

outfile.close()

# try:
#   url = 'https://github.com/mirakklys/python_for_AMC/raw/master/source/wrongCorrect.png'
#   ulr.urlretrieve(url, 'wrongCorrect.png')
#   print('I\'ve downloaded !wrongCorrect.png!\n Placed in the final test folder')
#   logFileF('...wrongCorrect.png image file is downloaded successfully\n')

# except:
#   pathForPNG = os.getcwd()
#   print('I couldn\'t download !wrongCorrect.png! from the GitHub, download it manually from https://github.com/mirakklys/python_for_AMC/blob/master/wrongCorrect.png and place in the final test folder')
#   logFileF('...Couldn\'t download the file to ' + pathForPNG)
  
logFileF('\n~~~Writing to file finished, all files are closed\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n', date = False)
