import json

"""
c provides serveral other basic data types besides int and float:
char character-a single byte
short short integer
long long integer
doubele double-precision floating point
"""

"""
%d  print as decimal integer
%6d print as decimal integer, at least 6 characters wide
%f  print as floating point
%6f print as floating point, at least 6 characters wide
%.2f print as floating point, 2 characters after decimal point
%6.2f print as floating point, at least 6 wide and 2 after decimal point
%o   for octal 
%x   for hexadecimal
%c   for character
%s   for character string
%%   for % itself
%ld  for long integer
"""

"""
EOF, end of file
EOF is an integer defined in <stdio.h>, but the specific numeric value does not matter as long as it is not the same as any char value.
"""

"""
a function definition has this form:

return-type function-name(parameter declarations, if any)
{
    declarations;
    statements;
}
"""

"""
each local variable in a function comes into existence only when the function is called , and disappears when the function is exited. We will use the term automatic henceforth to refer to these local variables.
"""

"""
if the program is in serveral source files, and a variable is defined in file1 and used in file2 and file3, the usual practice is to collect extern declarations of variables and functions in a separate file, historically called a header, that is included by #include at the front of each source file. the suffix .h is conventional for header names.
"""

"""
there are some restrictions on the names of variables and symbolic constants:
1. name are made up of letters and digits; 
2. the first character must be a letter.
3. the underscore '_' counts as a letter.
4. do not begin variable names with underscore, since library routines  often use such names.
5. upper case and lower case letter are distinct.
6. some keywords are reserved, can not use them as variable names.
"""

"""
certain characters can be represented in character and string constants by escape sequences, these sequences look like two characters, but represent only one.
the complete set of escape sequences is:
\a alert bell character
\b backspace
\f formfeed
\n newline
\r carriage return
\t horizontal tab
\v vertical tab
\\ backslash
\? question mark
\' single quote
\" double quote
\ooo octal number
\xhh  hexadecimal number

"""
