Lab Report: Python Password Generator
CS-3180: Comparative Languages

Student Name: [Dylan Krebs] Date: [9/02/26] Environment Specs:[Windows 10, Python 3.14]

Part 1: Environment
Briefly describe the process of setting up your Python development environment. Did you experience any friction when compared to a Java or C++ workspace (e.g. virtual environments, interpreter paths, IDE extensions)?
[I set my environment up in VS Code. My prior experience in Python was done in PyCharm so getting it set up in VS Code was a little different but not hard. I had an issue where I had to get an interpreter path set up which I was able to do through the extensions options. I have used Java in Eclipse mainly so I have not had alot of experience with Java in VS Code but the environment set up for both Java and Python have been pretty straight forward.]

How does this setup process reflect Python's identity as a scripting language? How does skipping a compilation step change how your program executes?
[It is much easier to run the program and get it to work straight away by skipping the compilation step. I am used to fixing issues in Java and C++ has given me the most grief when trying to fix all the little errors it likes to give even when running a simple program. Python is much easier to get working and run right away compared to Java or C++.]

Part 2: Paradigms and Types
Did you use type hints (e.g. def read_size() -> int:) in your code? Why or why not? How do type hints impact the readability and safety of a dynamically typed language like Python?
[I did not use any type hints for this application since Python can determine the types of variables at runtime and I think the assignment is focusing more on Python's dynamic typing.]

Identify the primary Python collections or built-in types you leveraged in this assignment (odds are high you never explicitely stated them). Compare their syntax and behavior with their equivalent types in Java (e.g. Python list/str vs. Java ArrayList/String).
[I used the built in type str for this assignment for "service" and "string" and used string.ascii_letters and string.digits to generate passwords based on the strength chosen, the Java equivalent is String. I used int for the "size" variable and the Java equivalent is the same int. I also used a tuple for ("strong", "weak"), to check the user's options for password strength. Python tuples are immutable collections, while Java does not have a direct equivalent. A Java array such as String[] could provide similar functionality in this case, although its behavior is different.]

Python is inherently a multi-paradigm language. Did you write your implementation using a procedural, or object-oriented (or functional if you are familiar) style? Explain why you chose this paradigm for this problem.
[I used procedural programming in this application with the use of functions and a sequence of operation as opposed to using objects and classes in OOP.]

Part 3: Generative AI Disclosure
Remember, the course strict citation guidelines for AI usage. At least 50% of the submitted code must be your own work, and any AI-generated help must be fully documented below.

AI Tools Utilized: 
 No generative AI was used on this assignment.
 Gemini (Google) [x]
 ChatGPT (OpenAI)
 Claude (Anthropic)
 GitHub Copilot
 Other: [Specify]
Conversation Logs: (If you used any chat-based tools, paste the public shareable links below.)
Link 1: [Paste URL here]
Link 2: [Paste URL here]
Prompting, Modification, Original Contribution Log Explain what you asked the model to generate. What parts did you use directly and what modifications did you have to perform to adapt it to your final program. Specifically, detail how you ensured that you authored at least 50% of the code yourself.
[I did not intentionally use an AI tool to write anything for me, if I got stuck on a portion of the assignment I would type into Google "how to do x in Python" and it would give me an example that I would then work off of. If the results that it provides are Gemini's output then it would have been the Gemini's AI though I have never consciously sought out or used Google Gemini's services but just to be safe I have chosen the use of Google Gemini.] 