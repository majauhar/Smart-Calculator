# A Smart Calculator

## The Calculator handles both numerical inputs and variables.
The way it does it is by converting the input expression into postfix expression.
It also handles all the edge cases, and prints corresponding error messages.

# Here is a simple walkthrough 
```c
>> 8 * 3 + 12 * (4 - 2)
48

>> 2 - 2 + 3
3

>> 4 * (2 + 3
Invalid expression

>> -10
-10

>> a=4
>> b=5
>> c=6
>> a*2+b*3+c*(2+3)
53

>> 1 +++ 2 * 3 -- 4
11

>> 3 *** 5
Invalid expression

>> 4+3)
Invalid expression

>> /command
Unknown command

>> /exit
Bye!
```
