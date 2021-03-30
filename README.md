Prompt:   
Problem:
You are given a prefix expression. Write a function to evaluate it. 

INPUT SAMPLE:

1  
\* \+ 2 3 4  
\+ 9 \* 2 6  


You have to take each line of the input, pass it to your function, and your function has to read this and insert it into any data structure you like. Traverse that data structure and evaluate the prefix expression. Each token is delimited by a whitespace. You may assume that the only valid operators appearing in test data are '+',’-’,'*' and '/'  (floating-point division). 

OUTPUT SAMPLE:

Print to stdout, the output of the prefix expression, one per line. E.g.

1  
20  
21

Constraints: 
The evaluation result will always be an integer >= 0. 
The number of the test cases is <= 40.

TO RUN:  
* Import parse_prefix_expression() from prefix_notation.py
    * Pass function a python string with new lines split by '\n'  
      character
    * Optional argument for changing token delimiter. Pass as string
    * Ex: parse_prefix_expression('+ 9 * 2 6')
    * Ex: parse_prefix_expression('1\n* + 2 3 4\n+ 9 * 2 6\n* + 1 + + 2 3 4 + 5 + 6 7p \n/ -3 4\n- -1 1')  
    * Ex: parse_prefix_expression('+\t9\t*\t2\t6', token_delimiter='\t')

* Execute from command line
    * Pass string encased in single quotes, preceded by $, splitting  
      each statement with a '\n' 
    * Optional argument for changing token delimiter. Pass as string encased in single quotes
    preceded by $
    * Ex: user$ python3 parse_prefix_expression $'+ 9 * 2 6'
    * Ex: user$ python3 parse_prefix_expression $'1\n* + 2 3 4\n+ 9 * 2 6\n* + 1 + + 2 3 4 + 5 + 6 7p \n/ -3 4\n- -1 1'
    * Ex: user$ python3 parse_prefix_expression $'+\t9\t*\t2\t6' $'\t'
    
Expected behavior is as follows:
* Dividing by 0, improperly formed expression, and empty expressions are noted in output,
but do not stop execution. Can easily be changed to other output or error stopping 
execution
* Mixed delimiters aren't addressed, but could be with additional requirements