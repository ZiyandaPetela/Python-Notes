# Python-week-1
* today was my first day since I was at the hospital the last two days. I learnt new things like installing all the necessary apps for my coding environment like python, jupiter and the text editor visual studio codde, I also created github.
* I also learnt introduction to python,why python is important and syntax that python uses which is different from other different languages.
* python variables, how to declare the variables and assign variables to them
* why comments are important and how to use them.
* the differre between global and local variables.
* Different python data types that are available like float,int string, boolean etc
* Data structures that we have lists and how is it different from tuples and dictionery's
* list
      * List is a collection which is ordered and changeable. Allows duplicate members
      * List items are ordered, changeable, and allow duplicate values.
      *List items are indexed, the first item has index [0], the second item has index [1] etc
      *To determine how many items a list has, use the len() function
      *lists are defined as objects with the data type 'list'
  *Tuples
     *tuples are used to store multiple items in a single variable
     *is ordered and unchangeable.
     * are written with round brackets.
     *Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
*Dictionery's
   *Dictionary is a collection which is ordered and changeable. No duplicate members.
   * items are presented in key:value pairs, and can be referred to by using the key name.

* different opearators that we have got such as arithmetic,logic,string ,comparison etc.
* python divides the operations the following groups:
  * arithmetic * / + %
  * assignment = += -= 
  * comparison == < > <= >= !=
  * logical and or not
  * identity is  is not
  *the order of operator precedence describes the order which operations are performed.
    ()	Parentheses	
    **	Exponentiation	
    +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
    *  /  //  %	Multiplication, division, floor division, and modulus
   
    *  Control flow
    *  conditions can be used commonly are "if statements" and loops.
    * "if statement" is written by using the if keyword.
    * I learnt that python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
    * for example
    * use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is 
       greater than a"
    * Elif
      *The elif keyword is if the previous conditions were not true, then try this condition
    *  Else
     * The else keyword catches anything which isn't caught by the preceding conditions.
     * python has two primitive loop commands:
       *while loops
       *for loops
       
    *while loop
       * With the while loop  can execute a set of statements as long as a condition is true
       *to increment index, or else the loop will continue forever.
       *With the break statement  can stop the loop even if the while condition is true
       * Stop the repetion when the loop reaches the specified value
       *With the continue statement can stop the current iteration, and continue with the next
* for loop
     * for loop is used for iterating over a sequence
     * does not require an indexing variable to set beforehand
     * To loop through a set of code a specified number of times, can use the range() function,
     * The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
     * it is possible to specify the starting value by adding a parameter range(2,6)which means values from 2 to 6 (but not adding 6)
     * it is possible to specify the increment value by adding a third parameter range(2,30,3)
     * the else  in for loop specifies a block of code to be executes when the loop is finished
     * nested loop is a loop inside a loop
     * the inner loop will be executes done-time for each iteration of the outer loop 
* functions
* can be defined using the "def" keyword followed by the function name and arguments in parentheses
* can take one or more arguments, and they may or may not return a value
* Functions can take one or more arguments, and they may or may not return a value.
* the print function is an example of a function that does not return anything, but rather prints output to the console.
* To call a function, use the function name followed by parenthesis.
* def my_function():
       print("Hello from a function")
 my_function()
*Information can be passed into functions as arguments.
*Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
*By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less
*If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
*This way the function will receive a tuple of arguments, and can access the items accordingly
* if you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.This way the function will receive a dictionary of arguments, and can access the items accordingly
* You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
E.g. if you send a List as an argument, it will still be a List when it reaches the function

* Classes and objects
*  When we define a class, we use an uppercase letter for the class name, and we start defining all the functions and attributes inside the class definition.
*  A Class is like an object constructor, or a "blueprint" for creating objects.
*  To create a class, use the keyword class
*  Now we can use the class named MyClass to create objects
*  To understand the meaning of classes we have to understand the built-in __init__() function.
*  All classes have a function called __init__(), which is always executed when the class is being initiated.
* Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
* usually begin by creating a special function called the initialization function, or "init" function, which gets called every time an instance of the class is created. The init function takes in a variable called "self,"
  *can access any of the attributes or functions in the class using the "self" variable.
  * These class instances are called objects, and the variables inside these classes are called attributes, while the functions are called methods. 
 *The __init__() function is called automatically every time the class is being used to create a new object.
*The __str__() function controls what should be returned when the class object is represented as a string.
*It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class the __str__() function is not set, the string representation of the object is returned
*IfThe self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.


      * BASIC DATA TYPES
* converting from one type to another, such as float to int, we call it casting
*Python doesn't round when casting floats to ints, it merely removes the decimal part.
*To round a float to the nearest int, we can use the round function.
*can also specify how many decimal places to round to, such as rounding 4.67 to 5. 
*Floats are stored as binary ones and zeros in memory, and due to limited memory
*if you pass a number as a string, the int class will convert it to an integer. For example, "100" becomes the integer 100.
*To use the decimal module, you need to import the decimal class and the getcontext function at the top of your code. The getcontext function returns a context object that holds global settings for using the decimal class
*Python easily casts integers to booleans - 1 is true and 0 is false. In fact, anything except 0 is true. So even -1 and imaginary 1 are true, but float 0 and imaginary 0 are false.
*Boolean true is true, of course, and anything other than an empty string is also true. So even the string "false" is true. The only false string is an empty one, but be careful not to accidentally have a space in there
*Python has numerous tools to analyze and construct strings, and one of the most useful is slicing. Slicing refers to taking a portion of a string and returning it
*Python has a few ways to create strings, including string concatenation and f-strings. F-strings allow us to insert variables or expressions inside curly braces in a string. We can also do rounding and number formatting with f-strings
* Python has a handy feature for creating multi-line strings by using triple quotes. If we need to include literal triple quotes in the string, we can escape them with a backslash
* When computers store information, it's done as ones and zeros.
* Bytes objects are immutable, like tuples, but you can use a byte array if you need to modify the data. You can treat a byte array like a string and modify specific byte values using slice notation.


* Basic Data Structures
* 




