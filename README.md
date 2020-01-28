# python_for_AMC
This is the automation of AMC redaction. The internal AMC-TXT should be working in a similar way, but I wanted the one that reflects my needs, if you want you can freely use it :)

Place the .py file in the folder with questions you want to convert.

The main rules:
1. Questions should be saved as Qs.txt file utf-8 encoded
2. Simple question should start with triple 'q' = <pre>'qqq'</pre> (see the example below)
3. Multi correct answer questions should start with triple <pre>'qmq'</pre> (see the example below)
4. Correct answer starts with <pre>'+++'</pre>
5. Wrong answer starts with <pre>'---'</pre>

Since it is the first version, the code will process the simple question-answer elements. In future, it will also process horizontal answers (as <pre>'qhq'</pre>), and image containing questions (as <pre>'qiq'</pre>).

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
The processed file will be in the same folder, called prcssdQs.txt
