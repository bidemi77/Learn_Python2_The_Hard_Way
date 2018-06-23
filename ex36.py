Rule for If-Statements 

 Every if-statement must have an else.
If this else should never be run because it doesn't make sense, then you 
must use a die function in the else  that prints out an error 
 message  and dies, just like we did in the last exercise.This will find any errors.

 Never nest if-statements more than two deep and always try to do them one deep.

 This means if you put an if in an if, then you should be looking to move 
that second if into another function.

Treat if-statements like paragraphs, where each if,elif, else grouping 
is like a set of sentences. Put blank lines before and after.

 Your boolean tests should be simple. If they are complex, move their 
calculations to variables earlier in your function and use a good name 
for the variable.


RULE FOR LOOPS 

1. Use  while-loop only to loop forever, and that means probably never
# This only applies to Python; other languagaes are different.

2. Use a for-loop for all other kinds of looping especially if there is a 
fixed or limited number of things to loop over.

Tips for Debugging 

1. Do not use a "debugger." A debugger is like doing a full-body scan on a 
 sick person. You do not get any specific useful information, and you find a 
 whole lot of information that doesn't help and is just confusing.

 The best way to debug a program is to use print to print out the values of 
 variables at points in the program to see where they go wrong.


 Make sure parts of your programs work as you work on them. Do not write 
massive files of code before you try to run them. Code a litlle, run a little,
 fix a little.
