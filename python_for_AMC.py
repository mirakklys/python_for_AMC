quizFile = open('Qs.txt', encoding = "utf8") 
quizQs = quizFile.read().splitlines()
quizQs.append('\n')
quizFile.close()
outfile = open('prcssdQs.txt', 'wt', encoding = "utf8")
outfile.writelines('''\\documentclass[a4paper,12pt]{article}
\\usepackage[utf8x]{inputenc}
\\usepackage[T1]{fontenc}
\\usepackage[box,completemulti,separateanswersheet]{automultiplechoice} %this is the main AMC package, you have to have it imported

\\begin{document}

\\hfill \\namefield{\\fbox{[5] %this is a naming section. You might need it to identify students' works afterwards
\\begin{minipage}{.5\\linewidth}
Firstname and lastname:

\\vspace*{.5cm}\\dotfill
\\vspace*{1mm}
\\end{minipage}
}}

\\AMCrandomseed{1237893}

\\def\\AMCformQuestion#1{\\vspace{\\AMCformVSpace}\\par {\\sc Question #1:} }

\\setdefaultgroupmode{withoutreplacement}

%all questions should have an ID, they are indicated within curly braces after \\begin{question}. For the first question the ID=='prez'. It is needed to manage annotation of the results

\\element{general}
{''')
count = 1
for each in range(len(quizQs)):
    if each == 0:
        if quizQs[0][0:3] == 'qqq':
            outfile.writelines('''\n  \\begin{question}{00''' + str(count) + "}\n    " + quizQs[0][4:] + "\n    \\begin{choices}\n")
            count += 1
        else:
            outfile.writelines('''\n  \\begin{questionmult}{00''' + str(count) + "}\n    " + quizQs[0][4:] + "\n    \\begin{choices}\n")
            count += 1
    if quizQs[each][0:3] == 'qqq':
        outfile.writelines('''    \\end{choices}
  \\end{question!!!!!}
}

\element{general}
{
  \\begin{question}{00''' + str(count) + "}\n    " + quizQs[each][3:] + "\n    \\begin{choices}\n")
        count += 1
    if quizQs[each][0:3] == 'qmq':
        outfile.writelines('''    \\end{choices}
  \\end{question!!!!!}
}

\\element{general}
{
  \\begin{questionmult}{00''' + str(count) + "}\n    " + quizQs[each][3:] + "\n    \\begin{choices}\n")
        count += 1
    if quizQs[each][0:3] == '+++':
        outfile.writelines("      \\correctchoice{" + quizQs[each][3:] + "}\n")
    if quizQs[each][0:3] == '---':
        outfile.writelines("      \\wrongchoice{" + quizQs[each][3:] + "}\n")

outfile.writelines('''
    \\end{choices}
  \\end{question!!!!!}
}
\\onecopy{10}{ %here you indicate the number of copies for the exam

%%% beginning of the test sheet header:

{\\bf NAME OF THE EXAM} %name your exam

\\vspace*{.5cm} %the following section can be removed
\\begin{minipage}{.4\\linewidth}
\\large\\bf Jan. 1st, 2020 %date if needed
\\end{minipage}

\\begin{center}\\bf
Duration : 5 minutes %indicate the Duration of the exam if needed

\\end{center}
\\vspace{3ex}

%%% end of the header

\\insertgroup{general}

\\clearpage %use either \\clearpage or \\cleardoublepage options. Double page will result in even number of pages for questions, so that you can print out questions double-sided and answer sheets separately

\\AMCformBegin

%%% beginning of the answer sheet header


{
      \\AMCcode{etu}{9} %9 indicates the digits number needed to code your students ID. etu option indicates the parameter \\AMCcode you will need to associate your students automatically
  \\begin{minipage}[b]{6.5cm}
  
  $\\leftarrow{}$\\hspace{0pt plus 1cm} please encode your student number in the boxes to the left,
  and write your first and last names below.$\\downarrow{}$\\hspace{0pt plus 1cm} \\vspace*{.5cm}
\\vspace{3ex}
\\hfill\\namefield{\\fbox{    
    \\begin{minipage}{.9\\linewidth}

      First name and last name:
      
      
      \\vspace*{.5cm}\\dotfill
      \\vspace*{0.5mm}
    \\end{minipage}
  }}\\hfill\\vspace{5ex}\\end{minipage}\\hspace*{\\fill}
}

\\begin{center}
\\bf\\Large Answers must be given exclusively on this sheet:
answers given on the other sheets will be ignored.
\\end{center}

%%% end of the answer sheet header

\\AMCform


\\clearpage

}


\\end{document}
''')
outfile.close()
