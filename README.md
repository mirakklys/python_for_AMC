# Auto Multiple Choice for Linux. AMC. Python-assisted source.tex creation. Only for tests with separate answer sheets!
This is the automation of AMC redaction. The internal AMC-TXT should be working in a similar way, but I wanted the one that reflects my needs, if you want you can freely use it :)

Place both <b>python_for_AMC.py</b> and <b>wrongCorrect.png</b> files in the folder with questions you want to convert.

The main rules:
1. Questions should be saved in ~~separate <b>Qs.txt</b>, <b>Qms.txt</b> or <b>Qhs.txt</b>~~, file utf-8 encoded depending on the type of questions
2. Simple question should start with <tt>'qqq'</tt> (see the example below)
3. Multi correct answer questions should start with triple <tt>'qmq'</tt> (see the example below)
4. Horizontal answer questions should start with <tt>'qhq'</tt> (5 columns by default) or <tt>'qhN'</tt>, where N is an integer reflecting the number of columns. I decided not to use the <tt>{choiceshoriz}</tt> since this option won't align the answers left. If you have 3 and less answers (e.g. True or False) you could leave default <tt>'qhq'</tt>
5. Correct answer starts with <tt>'+++'</tt>
6. Wrong answer starts with <tt>'---'</tt>

So far, most of the goals I set for the project achieved (simple questions, qmq, qhq/qhN)
In future, the code will also process image containing questions (as <tt>'qiq'</tt>).

The example for processing will look like:

<pre>qmqWhat is the best movie in the world?
+++Interstellar
---Harry Potter
+++Alita
---Saw
---Fifty Shades of Grey

qqqWhat is the best animated film?
+++Frozen
---Barbi
---Masha and the Bear

qhqI, Robot novel was written by Isaac Asimov
+++True
---False

qh4What is our genome made of
+++DNA and proteins
---Proteins
---Lipids
---Sugars
</pre>
The processed file will be in the same folder, called <b>prcssdQs.txt</b>

# List of changes:

# 0.3.0 

Now the script will process a single file <b>Qs.txt</b>

# 0.2.1

I jumped 0.2.0 because introduced the open answer questions in 0.1.1 version

So, finally it is one step closer to the final line :)

Minor code changes. Some windows machines when process txt in utf-8 encoding put some additional character at the beginning of the file. Since most people shouldn't use Win with AMC, I changed the code so it is suitable to Linux/Unix users :)

Now all files will have the same version numbering, so that it doesn't look stupidly messy

# 0.1.1 (9.1.1)

Added feature of column number choice. Now you will need to declare the feature with <tt>'qhq'</tt> (default) and <tt>'qh4'</tt> (4 columns)

Minor improvements to the code

Multiple correct horizontal answered questions are coming in the next release

Also released the open question script - <b>open_Qs_for_AMC.py</b>. You will need to declare the number of lines and maximum mark for the question, e.g. <tt>qoLM</tt>, where L is a number of lines and M is the max points received for the all correct answer. Partial point will be calculated depending on the number of lines and max point - <pre>partialPoint = maxPoint / (numberOfLines - 1)</pre>

# 0.1.0 (9.1.0 for fixed 9-digit student ID number)

Major update with the addition of <tt>qmq</tt> and <tt>qhq</tt> support

Now you will need to put all multiple correct answer questions into <b>Qms.txt</b> file utf-8 encoded, and all horizontal questions into <b>Qhs.txt</b> file utf-8 encoded

Please note that the number of columns per question (<tt>qhq</tt> ones) is defaulted to 5. Adjust according to your needs by changing this parameter in final .tex source file of AMC. In next version i will adjust it so that person could regulate it by coding <tt>qhq</tt> tag, e.g. <tt>qh2q</tt> or <tt>qh4q</tt>

Also, now code is much cleaner. Fewer possible weak points

# 0.0.3

Added the check-ups for user input, which catch wrong type

Added the number of digits in student ID number, now it is forom 2 to 12

Removed some repeated codes, functions rule!

Forked the NU-specific python script (it has 9-digit student ID number by default)

Next update will be a major one, with the support for <tt>qmq</tt> and <tt>qhq</tt>!

# 0.0.2

Added date, number of copy and name managing feature. In the terminal it will ask sequentially: number of copies, the date of the exam, the name of the exam

Please, note that the date is stricted to 2099 Dec 31 max, 2020 Jan 01 min, any other dates will cause the stop and error message

Inside the prcssdQs.txt you will need to change/correct the section <b>{etu}</b>, and <b>\clearpage <=> \AMCcleardoublepage</b> depending on your needs
  
For now it prints answer sheet on a separate piece of paper, should be easier to handle scanning

There is still no python script to handle <tt>qmq</tt>. It is comming in the next version

# 0.0.1
The beginning of the project
