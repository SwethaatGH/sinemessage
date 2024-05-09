# SINEMESSAGE
Are you looking for a very simple (beginner friendly)python based project? Try printing a sine message!

![Screenshot 2024-05-09 at 10 36 38 PM](https://github.com/SwethaatGH/sinemessage/assets/98175379/1e8108fa-1e94-42e1-ae19-ce39d333a006)

The pattern is formed by adding appropriate number of spaces infront of the message. 

The sin() function in python’s math module takes an argument(x). A variable named step is passed to math.sin(). It starts from 0 and increases by 0.25 on each iteration of the main loop of the program. The least number of spaces we want infront of the message is ‘zero’. Sine function has a range of [-1,1] mathematically. To get rid of this limitation, we add ‘1’ to the return value of sin() such that it returns in the range [0,2]. To include the required number of spaces we use a common multiplier with the return value variable.

When CTRL+C is pressed, the program terminates.

get_terminal_size()
The function gets the value of the width of the terminal of the user. The message cannot be printed to the last column on Windows without it adding a newline automatically.

### Modules Used
1. Sys module: This module provides access to some variables used or maintained by the Python interpreter and functions that interact strongly with the interpreter.
2. Math module: The Python Math module includes mathematical functions like trigonometric functions, representation functions, logarithmic functions, etc. It includes all basic operations and constants for calculation.
3. Shutil module: Python shutil module helps perform high-level file operation. It can operate with the file objects and offers us the ability to copy and remove files. It handles low-level semantics such as creating and closing file objects.

## ASSESSMENT

1.What happens when we change math.sin() to math.cos(step)?
![Screenshot 2024-05-09 at 10 36 24 PM](https://github.com/SwethaatGH/sinemessage/assets/98175379/7f9d5d99-21ce-4d54-853f-515c97e606f2)

2. What happens if you change math.sin(step) to math.sin(0)?
![Screenshot 2024-05-09 at 10 36 10 PM](https://github.com/SwethaatGH/sinemessage/assets/98175379/510f6903-8a5c-4ec9-b092-94eaf586974a)
