# Auto Multiple Choice. AMC. Python-assisted source.tex creation. Only for tests with separate answer sheets!
This is the automation of AMC redaction. The internal AMC-TXT should be working in a similar way, but I wanted the one that reflects my needs, if you want you can freely use it :)

Place both <b>python_for_AMC.py</b> and <b>wrongCorrect.png</b> files in the folder with questions you want to convert.

The main rules:
1. Questions should be saved as <b>Qs.txt</b> file utf-8 encoded
2. Simple question should start with triple 'q' = <tt>'qqq'</tt> (see the example below)
3. Multi correct answer questions should start with triple <tt>'qmq'</tt> (see the example below) - Available in Ver 0.1.0
4. Correct answer starts with <tt>'+++'</tt>
5. Wrong answer starts with <tt>'---'</tt>

Since it is one of the first versions, the code will process the simple question-answer elements. In future, it will also process horizontal answers (as <tt>'qhq'</tt>), and image containing questions (as <tt>'qiq'</tt>) (this one is going to appear in Ver 0.2.0).

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
</pre>
The processed file will be in the same folder, called <b>prcssdQs.txt</b>

# List of changes:

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
