# python-programming-language
Python Programming Language

## Overview
Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, Scheme, or Java.

### Some of Python's notable features:
* Uses an elegant syntax, making the programs you write easier to read.
* Is an easy-to-use language that makes it simple to get your program working. This makes Python ideal for prototype development and other ad-hoc programming tasks, without compromising maintainability.
* Comes with a large standard library that supports many common programming tasks such as connecting to web servers, searching text with regular expressions, reading and modifying files.
* Python's interactive mode makes it easy to test short snippets of code. There's also a bundled development environment called IDLE.
* Is easily extended by adding new modules implemented in a compiled language such as C or C++.
* Can also be embedded into an application to provide a programmable interface.
* Runs anywhere, including `Mac OS X`, `Windows`, `Linux`, and `Unix`, with unofficial builds also available for `Android` and `iOS`.
* Is free software in two senses. It doesn't cost anything to download or use Python, or to include it in your application. Python can also be freely modified and re-distributed because while the language is copyrighted it's available under an open-source license.

### Some programming-language features of Python are:
* A variety of basic data types are available: numbers (floating point, complex, and unlimited-length long integers), strings (both ASCII and Unicode), lists, and dictionaries.
* Python supports object-oriented programming with classes and multiple inheritances.
* Code can be grouped into modules and packages.
* The language supports raising and catching exceptions, resulting in cleaner error handling.
* Data types are strongly and dynamically typed. Mixing incompatible types (e.g. attempting to add a string and a number) causes an exception to be raised, so errors are caught sooner.
* Python contains advanced programming features such as generators and list comprehensions.
* Python's automatic memory management frees you from having to manually allocate and free memory in your code.

## Downloading Python
* install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions; you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2), but you should install an updated one (Python 3).*

On many systems Python comes pre-installed, you can try running the python command to start the Python interpreter to check and see if it is already installed. On windows you can try the py command which is a launcher which is more likely to work. If it is installed you will see a response which will include the version number, for example:

![Alt text](./images/1.png "a title") *image 1*

If you don't see this, you will need to install Python on your system.

If the version number is Python 2.x.y (where x and y are any number) you are using Python 2 which is no longer supported and is not a good choice for development. You can try running python3 to see if there is also a Python 3.x.y version installed, if not you'll want to install the latest version of Python.

If you do not have Python installed or need a newer version you can go to:

[![App Platorm](./images/2.png)](https://www.python.org/downloads/) *image 2*

Below are some system specific notes to keep in mind.

* `Linux`

    On most Linux distributions Python comes pre-installed and/or available via the distribution's package managers. Below are some common examples, but refer to your specific distribution's documentation and package list to get the most up to date instructions.

    If you'd like to download and build Python from source (or your distribution's package manager does not include a version of Python you need) you can download a source tarball from the general download page: https://www.python.org/downloads/
    
    *Debian or Ubuntu*
    ```bash
        apt-get install python3 python3-dev
    ```
## Learning Python
### Introduction

#### Why learn Python?
Since you’re here, you probably know why, but let’s quickly review Python’s advantages!

Python is one of the world’s most used and most popular programming languages. It’s powerful, versatile, and easy to learn. Python is widely used in various applications, some notable ones:

* Web development
* Data Science
* Data analysis
* Machine learning
* Artificial Intelligence (AI)
* Scripting and tooling

Many people say that Python comes with batteries included. It’s a fun way to state that it includes a comprehensive base library. In addition, because so many people use Python, hundreds of thousands of high-quality libraries and frameworks exist to get things done quickly and without hassle. You can do a lot with a little bit of Python code!

Learning Python is a no-brainer, and I promise you will be up and running quickly with this Python tutorial. Regardless of your future in IT, it will be a helpful tool to have in your toolbox!

#### Python history 
Let’s start by defining Python more precisely. Python is a computer programming language. Or, in other words, a vocabulary and set of grammatical rules for instructing a computer to perform tasks. Its original creator, Guido van Rossum, named it after the BBC television show ‘Monty Python’s Flying Circus.’ Hence, you’ll find that Python books, code examples, and documentation sometimes contain references to this television show.

In 1987, Guido worked on a large distributed operating system at the CWI, a national research institute for mathematics and computer science in the Netherlands. Within that project, he had some freedom to work on side projects. With the knowledge and experience he had built up in the years before, working on a computer language called ABC, he started writing the Python programming language.

Python is easy to learn, and it’s designed around a set of clearly defined principles (the Zen of Python) that encourage Python core developers to make a language that is unambiguous and easy to use.

### Install Python
#### Installation on MacOS
On most versions of MacOS before Catalina, a distribution of Python is already included. Unfortunately, it’s almost certainly an old version, Python 2.7. Luckily, there are two ways to easily install Python 3 on a Mac.

##### Homebrew
First and foremost, I recommend looking into Homebrew. It allows you to install almost anything easily. The added benefits:

* Homebrew packages are usually very up-to-date.
* It’s also easy to upgrade to newer versions later on.

However, you must be comfortable using a command-line shell to use Homebrew. If that’s entirely new for you, I recommend the following option for now: using the official installer.

If you choose to install Homebrew, installing Python on MacOS is as easy as:
```sh
$ brew install python
```
##### Official installer
Alternatively, you can download an installer from the Python download website. It’s easy and works like the installation of any other MacOS software program. The downside to this approach is that you won’t get automatic updates. Just like with Windows, you should ensure that Python is added to your system’s PATH.

#### Install Python on Linux
There are several ways to install Python on Linux, that is if you need to install it at all!

##### Check what’s installed first
Most Linux distributions include Python. Many will include both Python 2 and Python 3.

If you enter python --version on the command line, you’ll see the version number. It’s probably version 2.7:
```sh
$ python --version
Python 2.7.16
```
Unfortunately, you don’t want Python 2, but some OS’es still ship with it.

Now try python3 --version. If you get a “command not found,” you must install Python 3. If your output looks similar to this, you’re in luck:
```sh
$ python3 --version
Python 3.8.5    
```

##### Using a package manager
Depending on the distribution of Linux you are running, you can install Python with the default package manager: Yum, APT, etcetera. You’ll need to determine which package manager is used for your specific Linux distribution and how to use it.

If you’re on Ubuntu, Linux Mint, or Debian, you can install it using apt:
```sh
$ apt install python3 python-is-python3
```
This also installs a package called python-is-python3, which makes the command python point to python3. Trust me when I say it will save you a lot of headaches later on.

### Quickstart
Python is an interpreted programming language, this means that as a developer you write Python (.py) files in a text editor and then put those files into the python interpreter to be executed.

### Python Syntax

#### Whitespace and indentation
If you’ve been working in other programming languages such as Java, C#, or C/C++, you know that these languages use semicolons (;) to separate the statements.

However, Python uses whitespace and indentation to construct the code structure.

The following shows a snippet of Python code:
```py
# define main function to print out something
def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1

# call function main 
main()
```
The meaning of the code isn’t important to you now. Please pay attention to the code structure instead.

At the end of each line, you don’t see any semicolon to terminate the statement. And the code uses indentation to format the code.

By using indentation and whitespace to organize the code, Python code gains the following advantages:

* First, you’ll never miss the beginning or ending code of a block like in other programming languages such as Java or C#.
* Second, the coding style is essentially uniform. If you have to maintain another developer’s code, that code looks the same as yours.
* Third, the code is more readable and clear in comparison with other programming languages.

#### Comments
The comments are as important as the code because they describe why a piece of code was written.

When the Python interpreter executes the code, it ignores the comments.

In Python, a single-line comment begins with a hash (#) symbol followed by the comment. For example:

```py
# This is a single line comment in Python
```
And Python also supports other kinds of comments.

#### Continuation of statements
Python uses a newline character to separate statements. It places each statement on one line.

However, a long statement can span multiple lines by using the backslash (\) character.

The following example illustrates how to use the backslash (\) character to continue a statement in the second line:

```py
    if (a == True) and (b == False) and \
    (c == True):
        print("Continuation of statements")
```

#### Identifiers
Identifiers are names that identify `variables`, `functions`, `modules`, `classes`, and other objects in Python.

The name of an identifier needs to begin with a letter or underscore (_). The following characters can be alphanumeric or underscore.

Python identifiers are case-sensitive. For example, the `counter` and `Counter` are different identifiers.

In addition, you cannot use Python keywords for naming identifiers.

#### Keywords
Some words have special meanings in Python. They are called keywords.

The following shows the list of keywords in Python:
```py
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
```
Python is a growing and evolving language. So its keywords will keep increasing and changing.

Python provides a special module for listing its keywords called keyword. 

To find the current keyword list, you use the following code:

```py
import keyword

print(keyword.kwlist) 
```
#### String literals
Python uses single quotes ('), double quotes ("), triple single quotes (''') and triple-double quotes (""") to denote a string literal.

The string literal need to be surrounded with the same type of quotes. For example, if you use a single quote to start a string literal, you need to use the same single quote to end it.

The following shows some examples of string literals:
```py
s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line '''
print(s)
```
Summary
* A Python statement ends with a newline character.
* Python uses spaces and indentation to organize its code structure.
* Identifiers are names that identify variables, functions, modules, classes, etc. in Python.
* Comments describe why the code works. They are ignored by the Python interpreter.
* Use the single quote, double-quotes, triple-quotes, or triple double-quotes to denote

### Python Variables
#### What is a variable in Python
When you develop a program, you need to manage values, a lot of them. To store values, you use variables.
In Python, a variable is a label that you can assign a value to it. And a variable is always associated with a value. For example:
```py
message = 'Hello, World!'
print(message)

message = 'Good Bye!'
print(message)
```
Output:
```
Hello, World!
Good Bye!
```
In this example, message is a variable. It holds the string 'Hello, World!'. The print() function shows the message Hello, World! to the screen.

The next line assigns the string 'Good Bye!' to the message variable and print its value to the screen.

The variable message can hold various values at different times. And its value can change throughout the program.
#### Creating variables
To define a variable, you use the following syntax:
```py
variable_name = value
```
The = is the assignment operator. In this syntax, you assign a value to the variable_name.

The value can be anything like a number, a string, etc., that you assign to the variable.

The following defines a variable named counter and assigns the number 1 to it:
```py
counter = 1
```
#### Naming variables
When you name a variable, you need to adhere to some rules. If you don’t, you’ll get an error.

* The following are the variable rules that you should keep in mind:
* Variable names can contain only letters, numbers, and underscores (_). They can start with a letter or an underscore (_), not with a number.
* Variable names cannot contain spaces. To separate words in variables, you use underscores for example sorted_list.
* Variable names cannot be the same as keywords, reserved words, and built-in functions in Python.

The following guidelines help you define good variable names:

* Variable names should be concise and descriptive. For example, the active_user variable is more descriptive than the au.
* Use underscores (_) to separate multiple words in the variable names.
* Avoid using the letter l and the uppercase letter O because they look like the number 1 and 0.
### Variables in Python: Usage and Best Practices
In Python, variables are symbolic names that refer to objects or values stored in your computer’s memory. They allow you to assign descriptive names to data, making it easier to manipulate and reuse values throughout your code.

Understanding variables is key for Python developers because variables are essential building blocks for any Python program. Proper use of variables allows you to write clear, readable, and maintainable code.

In this block, you’ll learn how to:
* Create and assign values to variables
* Change a variable’s data type dynamically
* Use variables to create expressions, counters, accumulators, and Boolean flags
* Follow best practices for naming variables
* Create, access, and use variables in their scopes

#### Creating Variables With Assignments
The primary way to create a variable in Python is to assign it a value using the assignment operator and the following syntax:
```py
variable_name = value
```
In this syntax, you have the variable’s name on the left, then the assignment (=) operator, followed by the value you want to assign to the variable at hand. The value in this construct can be any Python object, including strings, numbers, lists, dictionaries, or even custom objects.

Here are a few examples of variables:

```py
>>> word = "Python"

>>> number = 42

>>> coefficient = 2.87

>>> fruits = ["apple", "mango", "grape"]

>>> ordinals = {1: "first", 2: "second", 3: "third"}

>>> class SomeCustomClass: pass
>>> instance = SomeCustomClass()
```
In this code, you’ve defined several variables by assigning values to names. The first five examples include variables that refer to different built-in types. The last example shows that variables can also refer to custom objects like an instance of your SomeCustomClass class.

#### Setting and Changing a Variable’s Data Type
Python is a dynamically typed language, which means that variable types are determined and checked at runtime rather than during compilation. Because of this, you don’t need to specify a variable’s type when you’re creating the variable. Python will infer a variable’s type from the assigned object.

*Note: In Python, variables themselves don’t have data types. Instead, the objects that variables reference have types.*

For example, consider the following variables:

```py
>>> name = "Jane Doe"
>>> age = 19
>>> subjects = ["Math", "English", "Physics", "Chemistry"]

>>> type(name)
<class 'str'>
>>> type(age)
<class 'int'>
>>> type(subjects)
<class 'list'>
```

In this example, name refers to the "Jane Doe" value, so the type of name is str. Similarly, age refers to the integer number 19, so its type is int. Finally, subjects refers to a list, so its type is list. Note that you don’t have to explicitly tell Python which type each variable is. Python determines and sets the type by checking the type of the assigned value.

Because Python is dynamically typed, you can make variables refer to objects of different data types in different moments just by reassigning the variable:
```py
>>> age = "19"
>>> type(age)
<class 'str'>

>>> subjects = {"Math", "English", "Physics", "Chemistry"}
>>> type(subjects)
<class 'set'>
```
Now, age refers to a string, and subjects refer to a set object. By assigning a value of a different type to an existing variable, you change the variable’s type.

#### Working With Variables in Python
Variables are an essential concept in Python programming. They work as the building blocks for your programs. So far, you’ve learned the basics of creating variables. In this section, you’ll explore different ways to use variables in Python.

You’ll start by using variables in expressions. Then, you’ll dive into counters and accumulators, which are essential for keeping track of values during iteration. You’ll also learn about other common use cases for variables, such as temporary variables, Boolean flags, loop variables, and data storage variables.
##### Expressions
In Python, an expression is a simple statement that Python can evaluate to produce and return a value. For example, consider the following expressions that compute the circumference of two different circles:
```py
>>> 2 * 3.1416 * 10
62.912

>>> 2 * 3.1416 * 20
125.824
```
Each of these expressions represents a specific computation. To build the expressions, you’ve used values and the multiplication operator (*). Python evaluates each expression and returns the resulting value.

*Note: To dive deeper into expressions and operators, check out the Operators and Expressions in Python tutorial.*

The above expressions are sort of rigid. For each expression, you have to repeat the input values, which is an error-prone and repetitive task.

Now consider the following examples:
```py
>>> pi = 3.1416
>>> radius = 10

>>> 2 * pi * radius
62.912

>>> radius = 20
>>> 2 * pi * radius
125.824
```
In this example, you first define variables to hold the input values. Then, you use those variables in the expressions. Note that when you build an expression using variables, Python replaces the variable by its value. As shown in the example, you can conveniently reuse the values in different expressions.

Another important point to note is that now you have descriptive names to properly identify the values used in the expressions.

To summarize, variables are great for reusing values in expressions and running computations with data that varies over time. In general, variables let you name or label objects so that you can reference and manipulate them later in the program. In the following sections, you’ll see use cases of variables in practice.

##### Object Counters
A counter is an integer variable that allows you to count objects. Counters typically have an initial value of zero, which increments to reflect the number of times a given object appears. To illustrate, say that you need to count the objects that are strings in a given list of objects. In this situation, you can do something like the following:
```py
>>> str_counter = 0

>>> for item in ("Alice", 30, "Programmer", None, True, "Department C"):
...     if isinstance(item, str):
...          str_counter += 1
...

>>> str_counter
3
```
In this example, you create the str_counter variable by initializing it to 0. Then, you run a for loop over a list of objects of different types. Inside the loop, you check whether the current object is a string using the built-in isinstance() function. If the current object is a string, then you increment the counter by one.

At the end of the loop, str_counter has a value of 3, reflecting the number of string objects in the input list.

*Note: The highlighted line in the above example uses the expression str_counter += 1, which is a shortcut for str_counter = str_counter + 1. The += operator is known as the augmented addition operator.*

You reuse the expression str_counter += 1 in each iteration of the loop to increment the value of str_counter, making it change over time. This dynamic updating is a key feature of variables. As the name variables suggests, they are designed to hold values that can vary over time.

##### Accumulators
Accumulators are another common type of variable used in programming. An accumulator is a variable that you use to add consecutive values to form a total that you can use as an intermediate step in different calculations.

A classic example of an accumulator is when you need to compute the sum of numeric values:
```py
>>> numbers = [1, 2, 3, 4]
>>> total = 0

>>> for number in numbers:
...     total += number
...

>>> total
10
```
In this example, the loop iterates over a list of numbers and accumulates each value in total. You can also use accumulators as parts of larger computations, for example to calculate the mean of a list of numbers:
```py
>>> total / len(numbers)
2.5
```
Then, you take advantage of total to compute the average using the built-in len() function. You could have used an object counter instead of len(). Similarly, Python comes with several accumulator functions that you can often use instead of explicit accumulators. For example, you can use sum() instead of calculating total as above.

##### Temporary Variables
Temporary variables hold intermediate results that you need for a more elaborate computation. A classic use case for a temporary variable is when you need to swap values between variables:
```py
>>> a = 5
>>> b = 10

>>> temp = a
>>> a = b
>>> b = temp

>>> a
10
>>> b
5
```
In this example, you use a temporary variable called temp to hold the value of a so that you can swap values between a and b. Once you’ve done the swap, temp is no longer needed.

*Note: In Python, there’s a clean and elegant way to swap values between variables without using temporary variables. You’ll learn about this topic in the section on iterable unpacking.*

For a more elaborate example of using temporary variables, consider the following function that calculates the variance of a sample of numeric data:

```py
>>> def variance(data, degrees_of_freedom=0):
...     return sum((x - sum(data) / len(data)) ** 2 for x in data) / (
...         len(data) - degrees_of_freedom
...     )
...

>>> variance([3, 4, 7, 5, 6, 2, 9, 4, 1, 3])
5.24
```
The expression that you use as the function’s return value is quite involved and challenging to understand. It’s also difficult to debug because you’re running multiple operations in a single expression.

To make your code easier to understand and debug, you can take advantage of an incremental development approach that uses temporary variables for intermediate calculations:
```py
>>> def variance(data, degrees_of_freedom=0):
...     number_of_items = len(data)
...     mean = sum(data) / number_of_items
...     total_square_dev = sum((x - mean) ** 2 for x in data)
...     return total_square_dev / (number_of_items - degrees_of_freedom)
...

>>> variance([3, 4, 7, 5, 6, 2, 9, 4, 1, 3])
5.24
```

In this alternative implementation of variance(), you calculate the variance in several steps. Each step is represented by a temporary variable with a meaningful name, making your code more readable.

#### Naming Variables in Python
The examples you’ve seen so far use short variable names. In practice, variable names should be descriptive to improve the code’s readability, so they can also be longer and include multiple words.

In the following sections, you’ll learn about the rules to follow when creating valid variable names in Python. You’ll also learn best practices for naming variables and other naming-related practices.

##### Rules for Naming Variables
Variable names in Python can be any length and can consist of uppercase letters (A-Z) and lowercase letters (a-z), digits (0-9), and the underscore character (_). The only restriction is that even though a variable name can contain digits, the first character of a variable name can’t be a digit.

> *Note: Python currently has full Unicode support, and you can use many unicode characters in variable names. For example, the following variable names are valid:*
```py
>>> α = 45
>>> β = 90
>>> δ = 180
>>> π = 3.14
```

*These variable names may be uncommon in Python code, but they’re completely valid. You can use them in code that performs scientific calculations when you want the code to reflect the notation used in the target discipline.*

All of the following are valid variable names:

```py
>>> name = "Bob"
>>> year_of_birth = 1970
>>> is_adult = True
```

These variables follow the rules for creating valid variable names in Python. They also follow best naming practices, which you’ll learn about in the next section.

The variable name below doesn’t follow the rules:
```py
>>> 1099_filed = False
  File "<input>", line 1
    1099_filed = False
        ^
SyntaxError: invalid decimal literal
```
The variable name in this example starts with a number, which isn’t allowed in Python. Therefore, you get a SyntaxError exception.

It’s important to know that variables are case-sensitive. Lowercase and uppercase letters aren’t treated the same:
```py
>>> age = 1
>>> Age = 2
>>> aGe = 3
>>> AGE = 4

>>> age
1
>>> Age
2
>>> aGe
3
>>> AGE
4
```
In this example, Python interprets the names as different and independent variables. So, casing is something to consider when you’re creating variable names in Python.

Nothing stops you from creating two different variables in the same program called age and Age, or, for that matter, agE. However, this practice isn’t recommended because it can confuse people trying to read your code and even yourself after a while. In general, you should use lowercase letters when creating your variable names.

The use of underscore characters is also significant. You’ll use an underscore to separate multiple words in a variable name:
```py
>>> first_name = "John"
>>> pen_color = "red"
>>> next_node = 123
```
In these variable names, you use the underscore character as a separator for multiple words. This is a way to improve the readability of your code by substituting the space character with an underscore. To illustrate this, consider how your variables would look without the underscores:

```py
>>> firstname = "John"
>>> pencolor = "red"
>>> nextnode = 123
```

Even though these names are technically valid, they can be challenging to read and understand at a glance. The lack of separation makes it harder to grasp the meaning of each variable quickly, and they require more effort to interpret. Using underscores improves the clarity of your code and makes it more maintainable.

##### Best Practices for Naming Variables
You should always give a variable a descriptive name that clearly explains the variable’s purpose. Sometimes, you can find a single word to name a given variable:
```py
>>> temperature = 25
>>> weight = 54.5
>>> message = "Hello, Pythonista!"
```
Variables always refer to concrete objects, so their names should be nouns. You should try to find specific names for your variables that uniquely identify the referred object. Names like variable, data, or value may be too generic. While these names can work for short examples, they’re not descriptive enough for production code.

In general, you should avoid single-letter names:

```py
>>> t = 25  # Don't do this
>>> temperature = 25  # Do this instead
```

Single-letter names may be hard to decipher, making your code difficult to read, especially when you use them in expressions with other similar names. Of course, there are exceptions. For example, if you’re working with nested lists, then you can use single-letter names to identify indices:

```py
>>> matrix = [
...     [9, 3, 8],
...     [4, 5, 2],
...     [6, 4, 3],
... ]

>>> for i in matrix:
...     for j in i:
...         print(j)
...
9
3
8
4
5
2
6
4
3
```
It’s common to use letters like i, j, and k to represent indices, so you can use them in the right context. It’s also common to use x, y, and z to represent point coordinates, so these are also okay to use.

Using abbreviations to name variables is discouraged, in favor of using the complete name:

```py
>>> doc = "Freud"  # Don't do this
>>> doctor = "Freud"  # Do this instead
```
It’s best practice to use a complete name instead an abbreviated name because it’s more readable and clear. However, sometimes abbreviations are okay when they’re widely accepted and used:

```py
>>> cmd = "python -m pip list"
>>> msg = "Hello, Pythonista!"
```
In these examples, cmd is a commonly used abbreviation for command and msg is commonly used for message. A classic example of a widely used abbreviation in Python is the cls name, which you should use to identify the current class object in a class method.

Sometimes, you need multiple words to build a descriptive variable name. When using multi-word names, you can struggle to read them if there isn’t a distinguishable boundary between words:
```py
>>> numberofgraduates = 200
```
This variable name is difficult to read. You have to pay close attention to figuring out the words’ boundaries so that you can understand what the variable represents.

The most common practices for multi-word variable names are the following:

* **Snake case**: Lowercase words are separated by underscores. For example: number_of_graduates.
* **Camel case**: The second and subsequent words are capitalized to make word boundaries easier to see. For example: numberOfGraduates.
* **Pascal case**: Similar to camel case, except the first word is also capitalized. For example: NumberOfGraduates.

The Style Guide for Python Code, also known as PEP 8, contains naming conventions that list suggested standards for names of different object types. Regarding variables, PEP 8 recommends using the snake case style.

When you need multi-word names, it’s common to combine an adjective as a qualifier with a noun:
```py
>>> initial_temperature = 25
>>> current_file = "marketing_personel.csv"
>>> next_point = (2, 4)
```
In these examples, you create descriptive variable names by combining adjectives and nouns, which can dramatically improve your code’s readability. Another point to consider is to avoid multi-word names that start with my_, like my_file, my_color, and so on. The my_ part doesn’t really add anything useful to the name.

Flag variables are another good example of when to use a multi-word variable name:
```py
>>> is_authenticated = True
>>> has_permission = False
```
In these examples, you’ve used an underscore to separate the words, making their boundaries visible and quick to spot.

When it comes to naming lists and dictionaries, you should use plural nouns in most situations:

```py
>>> fruits = ["apple", "banana", "cherry"]

>>> colors = {
...     "Red": (255, 0, 0),
...     "Green": (0, 255, 0),
...     "Blue": (0, 0, 255),
...     "Yellow": (255, 255, 0),
...     "Black": (0, 0, 0),
...     "White": (255, 255, 255),
... }
```

Using plural nouns in these examples makes it clear that the variable refers to a container that stores several objects of similar types.

When naming tuples, you should consider that they’re commonly used to store objects of different types or meanings. So, it’s okay to use singular nouns:
```py
>>> color = (255, 0, 0)
>>> row = ("Jane", 25, "Python Dev", "Canada")
```
Although these tuples store multiple objects, they represent a single entity. The first tuple represents an RGB (red, green, blue) color, while the second represents a row in a database table or some other tabular data.

#### Exploring Core Features of Variables
When you start digging deeper into how Python variables work internally, you discover several interesting features worth studying. In the following sections, you’ll explore some of the core features of variables so that you can better understand them.

##### Variables Hold References to Objects
What happens when you create a variable with an assignment? This is an important question in Python because the answer differs from what you’d find in many other programming languages.
Python is an object-oriented programming language. Every piece of data in a Python program is an object of a specific type or class. Consider this code:
```py
>>> 300
300
```
When presented with the statement 300, Python does the following operations:

* Creates an integer object
* Gives it a value of 300
* Displays it on the screen

You can see that an integer object is created using the built-in type() function:
```py
>>> type(300)
<class 'int'>
```

A Python variable is a symbolic name that refers to or points to an object like 300. Once an object is assigned to a variable, you can refer to it by the variable’s name, but the data itself is still contained within the object.

For example, consider the following variable definition:
```py
>>> n = 300
```
This assignment creates an integer object with a value of 300 and makes the variable n point to that object. The diagram below shows how this happens:
![alt text](./images/3.png) Variable Assignment

In Python, variables don’t store objects. They point or refer to objects. Every time you create an object in Python, it’s assigned a unique number, which is then associated with the variable.

The built-in id() function returns an object’s identifier or identity:
```py
>>> n = 300
>>> id(n)
4399012816
```

In CPython, the standard Python distribution, an object’s identity coincides with its memory address. Therefore, CPython variables store memory addresses. Through these memory addresses, variables access the concrete objects stored in memory.

You can create multiple variables that point to the same object. In other words, variables that hold the same memory address:

```py
>>> m = n
>>> id(n) == id(m)
True
```

In this example, Python doesn’t create a new object. It creates a new variable name or reference, m, which points to the same object that n points to:
![alt text](image.png)
Multiple References to a Single Object

Next, suppose you do something like this:
```py
>>> m = 400
```
Now, Python creates a new integer object with the value 400, and m becomes a reference to it:
![alt text](image-1.png) References to separate objects 

Finally, say that you run the following statement:
```py
>>> n = "foo"
```
Now, Python creates a string object with the value "foo" and makes n a reference to that:

![alt text](image-2.png) Orphaned Object

Because of the n and m reassignments, you no longer have a reference to integer object 300. It’s orphaned, and you have no way to access it again.

When the references to an object drop to zero, the object is no longer accessible. At that point, its lifetime is over. Python reclaims the allocated memory so it can be used for something else. In programming terminology, this process is known as garbage collection.

##### Variables Have Dynamic Types
In many programming languages, variables are statically typed, which means they’re initially declared to have a specific data type during their lifetime. Any value assigned to that variable during its lifetime must be of the specified data type.

Python variables aren’t typed this way. In Python, you can assign values of different data types to a variable at different moments:
```py
>>> value = "A string value"
>>> value
'A string value'

>>> # Later
>>> value = 23.5
>>> value
23.5
```
In this example, you’re making the value variable refer to or point to an object of another type. Because of this feature, Python is a dynamically typed language.

It’s important to note that changes in a variable’s data type can lead to runtime errors. For example, if a variable’s data type changes unexpectedly, you may face type-related bugs or even get an exception:
```py
>>> value = "A string value"
>>> value.upper()
'A STRING VALUE'

>>> # Later
>>> value = 23.5

>>> # Try to use .upper() again
>>> value.upper()
Traceback (most recent call last):
    ...
AttributeError: 'float' object has no attribute 'upper'
```
In this example, the variable type changes during the code’s execution. When value points to a string, you can use the .upper() method to convert the letters into uppercase. However, when the type changes to float, the .upper() method isn’t available, and you get an AttributeError exception.

##### Variables Can Use Type Hints
You can use type hints to add explicit type information to your variables. To do this, you can use the following Python syntax:
```py
variable: data_type [= value]
```

The square brackets aren’t part of the syntax. They denote that the enclosed part is optional. Yes, you can declare a Python variable without assigning it a value:
```py
>>> number: int

>>> number
Traceback (most recent call last):
    ...
NameError: name 'number' is not defined
```
The variable declaration on the first line works and is valid Python syntax. However, this declaration doesn’t really create a new variable for you. That’s why when you try to access the number variable, you get a NameError exception. Even though number isn’t defined, Python has recorded the type hint:
```py
>>> __annotations__
{'number': <class 'int'>}
```

When it comes to basic data types such as numbers and strings, type hints may look superfluous:
```py
>>> language: str = "Python"
>>> number: int = 42
>>> coefficient: float = 2.87
```
#### Using Complementary Ways to Create Variables
In Python, you’ll find a few alternative ways to create new variables. Sometimes, defining several variables simultaneously with the same initial value is convenient or needed. To do this, you can use a parallel assignment.

In other situations, you may need to initialize several variables with values from a sequence data type, like a list or tuple. In this case, you can use a technique called iterable unpacking.

You’ll also find situations where you need to retain the value that results from a given expression. In this case, you can use an assignment expression.

In the following sections, you’ll learn about all these alternative or complementary ways to create Python variables.

##### Parallel Assignment
Python also allows you to run multiple assignments in a single line of code. This feature makes it possible to assign the same value to several variables simultaneously:

```py
>>> is_authenticated = is_active = is_admin = False

>>> is_authenticated
False
>>> is_active
False
>>> is_admin
False
```

The parallel assignment in this example initializes three different but related variables to False simultaneously. This way of creating and initializing variables is more concise and less repetitive than the following:
```py
>>> is_authenticated = False
>>> is_active = False
>>> is_admin = False

>>> is_authenticated
False
>>> is_active
False
>>> is_admin
False
```
By using parallel assignments instead of dedicated assignments, you make your code more concise and less repetitive.

##### Iterable Unpacking
Iterable unpacking is a cool Python feature also known as tuple unpacking. It consists of distributing the values in an iterable into a series of variables. In most cases, the number of variables will match the number of items in the iterable. However, you can also use the *variable syntax to grab several items in a list.

You can use iterable unpacking to create multiple variables at a time using an iterable of values. For example, say that you have some data about a person and want to create dedicated variables for each piece of data:

```py
>>> person = ("Jane", 25, "Python Dev")
```
If you didn’t know about iterable unpacking, then your first approach might be to distribute the data into different variables manually, as shown below:
```py
>>> name = person[0]
>>> age = person[1]
>>> job = person[2]

>>> name
'Jane'
>>> age
25
>>> job
'Python Dev'
```
This code works. However, using indices to extract the data may lead to an error-prone and hard-to-read result. Instead of using this technique, you can take advantage of iterable unpacking and end up with the following code:
```py
>>> name, age, job = person

>>> name
'Jane'
>>> age
25
>>> job
'Python Dev'
```
Now, your code looks cleaner and more readable. So, when you find yourself creating variables from iterables using indices, consider using unpacking instead.

A great use case for unpacking is when you need to swap the values between two variables:

```py
>>> a = 5
>>> b = 10

>>> a, b = b, a

>>> a
10
>>> b
5
```
In the highlighted line, you swap the values of a and b without using a temporary variable, as you saw before. In this example, it’s important to note that the iterable to the right of the equal sign is a tuple of variables. 

#### Summary
* A variable is a label that you can assign a value to it. The value of a variable can change throughout the program.
* Use the variable_name = value to create a variable.
* The variable names should be as concise and descriptive as possible. Also, they should adhere to Python variable naming rules.

### Data types
#### Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
A               | B
----------------|--------------------------------
Text Type:	    |      str
Numeric Types:	|   int, float, complex
Sequence Types:	|   list, tuple, range
Mapping Type:	|   dict
Set Types:	    |   set, frozenset
Boolean Type:	|   bool
Binary Types:	|   bytes, bytearray, memoryview
None Type:	    |   NoneType
|

##### Getting the Data Type
You can get the data type of any object by using the type() function:

ExampleGet your own Python Server
Print the data type of the variable x:
```py
x = 5
print(type(x))
```
##### Setting the Data Type
In Python, the data type is set when you assign a value to a variable:

Example	          |      Data Type
------------------|----------------	
x = "Hello World" |	str	
x = 20	          | int	
x = 20.5	      | float
|. . .

##### Numbers
There are three numeric types in Python:

* int
* float
* complex

Variables of numeric types are created when you assign a value to them:
```py
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```

To verify the type of any object in Python, use the type() function:
```py
print(type(x))
print(type(y))
print(type(z))
```

###### Int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.


Integers:
```py
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```

###### Float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

```py
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```

Float can also be scientific numbers with an "e" to indicate the power of 10.
```py
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```

###### Complex
Complex numbers are written with a "j" as the imaginary part:

Example
Complex:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

##### Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:

Convert from one type to another:
```py
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

##### Booleans
Booleans represent one of two values: True or False.

###### Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:
```py
print(10 > 9)
print(10 == 9)
print(10 < 9)
```

###### Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return,

Evaluate a string and a number:
```py
print(bool("Hello"))
print(bool(15))
```

Evaluate two variables:
```py
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
```

###### Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

```Python
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
```
###### Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

```Python
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```
##### Operators
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:
```py
print(10 + 5)
```

Python divides the operators in the following groups:
* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators
* Identity operators
* Membership operators
* Bitwise operators

###### Python Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator | Name            | Example  |
|----------|-----------------|----------|
| +        | Addition        | x + y    |
| -        | Subtraction     | x - y    |
| *        | Multiplication  | x * y    |
| /        | Division        | x / y    |
| %        | Modulus         | x % y    |
| **       | Exponentiation  | x ** y   |
| //       | Floor division  | x // y   |

###### Python Assignment Operators

Assignment operators are used to assign values to variables:

| Operator | Example     | Same As          |
|----------|-------------|------------------|
| =        | x = 5       | x = 5            |
| +=       | x += 3      | x = x + 3        |
| -=       | x -= 3      | x = x - 3        |
| *=       | x *= 3      | x = x * 3        |
| /=       | x /= 3      | x = x / 3        |
| %=       | x %= 3      | x = x % 3        |
| //=      | x //= 3     | x = x // 3       |
| **=      | x **= 3     | x = x ** 3       |
| &=       | x &= 3      | x = x & 3        |
| \|=      | x \|= 3      | x = x | 3        |
| ^=       | x ^= 3      | x = x ^ 3        |
| >>=      | x >>= 3     | x = x >> 3       |
| <<=      | x <<= 3     | x = x << 3       |
| :=       | print(x := 3) | x = 3<br>print(x) |

---

###### Python Comparison Operators

Comparison operators are used to compare two values:

| Operator | Name                      | Example    |
|----------|---------------------------|------------|
| ==       | Equal                     | x == y     |
| !=       | Not equal                 | x != y     |
| >        | Greater than              | x > y      |
| <        | Less than                 | x < y      |
| >=       | Greater than or equal to  | x >= y     |
| <=       | Less than or equal to     | x <= y     |

---

###### Python Logical Operators

Logical operators are used to combine conditional statements:

| Operator | Description                          | Example                           |
|----------|--------------------------------------|-----------------------------------|
| and      | Returns True if both statements are true | x < 5 and x < 10                  |
| or       | Returns True if one of the statements is true | x < 5 or x < 4                  |
| not      | Reverse the result, returns False if the result is true | not(x < 5 and x < 10)             |

---

###### Python Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

| Operator  | Description                                   | Example    |
|-----------|-----------------------------------------------|------------|
| is        | Returns True if both variables are the same object | x is y     |
| is not    | Returns True if both variables are not the same object | x is not y |

---

###### Python Membership Operators

Membership operators are used to test if a sequence is presented in an object:

| Operator   | Description                                      | Example    |
|------------|--------------------------------------------------|------------|
| in         | Returns True if a sequence with the specified value is present in the object | x in y     |
| not in     | Returns True if a sequence with the specified value is not present in the object | x not in y |

---

###### Python Bitwise Operators

Bitwise operators are used to compare (binary) numbers:

| Operator | Name                 | Description                                                             | Example    |
|----------|----------------------|-------------------------------------------------------------------------|------------|
| &        | AND                  | Sets each bit to 1 if both bits are 1                                   | x & y      |
| \|       | OR                   | Sets each bit to 1 if one of two bits is 1                              | x \| y     |
| ^        | XOR                  | Sets each bit to 1 if only one of two bits is 1                         | x ^ y      |
| ~        | NOT                  | Inverts all the bits                                                   | ~x         |
| <<       | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off | x << 2     |
| >>       | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off | x >> 2     |

##### Operator Precedence
Operator precedence describes the order in which operations are performed.

Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

```py
print((6 + 3) - (6 + 3))
```

Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:

```py
print(100 + 5 * 3)
```

The precedence order is described in the table below, starting with the highest precedence at the top:

| Operator                         | Description                                              |
|----------------------------------|----------------------------------------------------------|
| ()                               | Parentheses                                              |
| **                               | Exponentiation                                           |
| +x, -x, ~x                       | Unary plus, unary minus, and bitwise NOT                 |
| *, /, //, %                      | Multiplication, division, floor division, and modulus    |
| +, -                             | Addition and subtraction                                 |
| <<, >>                           | Bitwise left and right shifts                            |
| &                                | Bitwise AND                                              |
| ^                                | Bitwise XOR                                              |
| \|                               | Bitwise OR                                               |
| ==, !=, >, >=, <, <=, is, is not, in, not in | Comparisons, identity, and membership operators         |
| not                              | Logical NOT                                              |
| and                              | AND                                                      |
| or                               | OR                                                       |


##### Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
```py
print("Hello")
print('Hello')
```

###### Quotes Inside Quotes
You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
```py
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
```
###### Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

```py
a = "Hello"
print(a)
```
###### Multiline Strings
You can assign a multiline string to a variable by using three quotes:


You can use three double quotes:
```py
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```
Or three single quotes:

```py
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```

###### Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

Get the character at position 1 (remember that the first character has the position 0):

```py
a = "Hello, World!"
print(a[1])
```

###### String Length
To get the length of a string, use the len() function.


The len() function returns the length of a string:
```py
a = "Hello, World!"
print(len(a))
```

###### Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.


Check if "free" is present in the following text:
```py
txt = "The best things in life are free!"
print("free" in txt)
```

###### Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

Check if "expensive" is NOT present in the following text:
```py
txt = "The best things in life are free!"
print("expensive" not in txt)
```

###### Slicing Strings
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Get the characters from position 2 to position 5 (not included):

```py
b = "Hello, World!"
print(b[2:5])
```

> *Note*: The first character has index 0.

###### Slice From the Start
By leaving out the start index, the range will start at the first character:

* Example: Get the characters from the start to position 5 (not included):
```py
b = "Hello, World!"
print(b[:5])
```

###### Negative Indexing
Use negative indexes to start the slice from the end of the string:

Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
```py
b = "Hello, World!"
print(b[-5:-2])
```

###### Concatenation

To concatenate, or combine, two strings you can use the + operator.

Merge variable a with variable b into variable c:
```py
a = "Hello"
b = "World"
c = a + b
print(c)
```

To add a space between them, add a " ":
```py
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```

###### Format - Strings

String Format
As we know, we cannot combine strings and numbers like this:
```py
age = 36
txt = "My name is John, I am " + age
print(txt)
```
But we can combine strings and numbers by using f-strings or the format() method!

###### F-Strings

F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

Create an f-string:
```py
age = 36
txt = f"My name is John, I am {age}"
print(txt)
```
###### Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.

Add a placeholder for the price variable:
```py
price = 59
txt = f"The price is {price} dollars"
print(txt)
```
A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

```py
Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
```

A placeholder can contain Python code, like math operations:

Perform a math operation in the placeholder, and return the result:
```py
txt = f"The price is {20 * 59} dollars"
print(txt)
```

###### Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

You will get an error if you use double quotes inside a string that is surrounded by double quotes:
```py
txt = "We are the so-called "Vikings" from the north."
```
To fix this problem, use the escape character \":

The escape character allows you to use double quotes when you normally would not be allowed:
```py
txt = "We are the so-called \"Vikings\" from the north."
```
Escape Characters

Code	    |Result	
------------|-------------------
\\'	        |    Single Quote	
\\\         |    Backslash	
\n	        |    New Line	
\r	        |    Carriage Return	
\t	        |    Tab	
\b	        |    Backspace	
\f	        |    Form Feed	
\ooo	    |    Octal value	
\xhh	    |    Hex value
|

###### Modify Strings
Python has a set of built-in methods that you can use on strings.

`upper()`

The upper() method returns the string in upper case:
```py
a = "Hello, World!"
print(a.upper())
```

`lower()`

The lower() method returns the string in lower case:
```py
a = "Hello, World!"
print(a.lower())
```

`strip()`

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

The strip() method removes any whitespace from the beginning or the end:

```
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```

`replace()`
The replace() method replaces a string with another string:
```py
a = "Hello, World!"
print(a.replace("H", "J"))
```

`split()`
The split() method returns a list where the text between the specified separator becomes the list items.

The split() method splits the string into substrings if it finds instances of the separator:

```py
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
```

###### String Methods
Method	                |            Description
------------------------|-----------------------------------------------------
capitalize()            |   Converts the first character to upper case|
casefold()              |  	Converts string into lower case
center()                |  	Returns a centered string
count()                 |	Returns the number of times a specified value occurs in a string
encode()                |  	Returns an encoded version of the string
endswith()              |  	Returns true if the string ends with the specified value
expandtabs()            |   Sets the tab size of the string
find()                  |	Searches the string for a specified value and returns the position of where it was found
format()                |  	Formats specified values in a string
format_map()            |   Formats specified values in a string
index()                 |	Searches the string for a specified value and returns the position of where it was found
isalnum()               |  	Returns True if all characters in the string are alphanumeric
isalpha()               |  	Returns True if all characters in the string are in the alphabet
isascii()               |  	Returns True if all characters in the string are ascii characters
isdecimal()             |  	Returns True if all characters in the string are decimals
isdigit()               |  	Returns True if all characters in the string are digits
isidentifier()          |   Returns True if the string is an identifier
islower()               |  	Returns True if all characters in the string are lower case
isnumeric()             |  	Returns True if all characters in the string are numeric
isprintable()           |   Returns True if all characters in the string are printable
isspace()               |  	Returns True if all characters in the string are whitespaces
istitle()               |  	Returns True if the string follows the rules of a title
isupper()               |  	Returns True if all characters in the string are upper case
join()                  |	Joins the elements of an iterable to the end of the string
ljust()                 |	Returns a left justified version of the string
lower()                 |	Converts a string into lower case
maketrans()             |  	Returns a translation table to be used in translations
lstrip()                |  	Returns a left trim version of the string
partition()             |  	Returns a tuple where the string is parted into three parts
replace()               |  	Returns a string where a specified value is replaced with a specified value
rfind()                 |	Searches the string for a specified value and returns the last position of where it was found
rindex()                |  	Searches the string for a specified value and returns the last position of where it was found
rjust()                 |	Returns a right justified version of the string
rpartition()            |   Returns a tuple where the string is parted into three parts
rsplit()                |  	Splits the string at the specified separator, and returns a list
rstrip()                |  	Returns a right trim version of the string
split()                 |	Splits the string at the specified separator, and returns a list
splitlines()            |   Splits the string at line breaks and returns a list
startswith()            |   Returns true if the string starts with the specified value
strip()                 |	Returns a trimmed version of the string
swapcase()              |  	Swaps cases, lower case becomes upper case and vice versa
title()                 |	Converts the first character of each word to upper case
translate()             |  	Returns a translated string
upper()                 |	Converts a string into upper case
zfill()                 |	Fills the string with a specified number of 0 values at the beginning
|

### Conditionals
Conditional Statements in Python perform different actions depending on whether a specific condition evaluates to true or false. 
Conditional Statements are handled by if-elif-else statements and MATCH-CASE statements in Python.

#### Conditional Statements in Python
##### if
We’ll start by looking at the most basic type of if statement. In its simplest form, it looks like this:

```py
if <expr>:
    <statement>
```

In the form shown above:
* **<expr\>** is an expression evaluated in a Boolean context, as discussed in the section on Logical Operators in the Operators and Expressions in Python tutorial.
* **<statement\>** is a valid Python statement, which must be indented. (You will see why very soon.)

If <expr\> is true (evaluates to a value that is “truthy”), then <statement\> is executed. If <expr> is false, then <statement> is skipped over and not executed.

Note that the colon (:) following <expr\> is required. Some programming languages require <expr> to be enclosed in parentheses, but Python does not.

Here are several examples of this type of if statement:
```py
>>> x = 0
>>> y = 5

>>> if x < y:                            # Truthy
...     print('yes')
...
yes
>>> if y < x:                            # Falsy
...     print('yes')
...

>>> if x:                                # Falsy
...     print('yes')
...
>>> if y:                                # Truthy
...     print('yes')
...
yes

>>> if x or y:                           # Truthy
...     print('yes')
...
yes
>>> if x and y:                          # Falsy
...     print('yes')
...

>>> if 'aul' in 'grault':                # Truthy
...     print('yes')
...
yes
>>> if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
...     print('yes')
...
```

###### Grouping Statements: Indentation and Blocks
So far, so good.

But let’s say you want to evaluate a condition and then do more than one thing if it is true:
>
> If the weather is nice, then I will:
>
> * Mow the lawn
>
> * Weed the garden
>
> * Take the dog for a walk
>
>(If the weather isn’t nice, then I won’t do any of these things.)

In all the examples shown above, each if `<expr>`: has been followed by only a single `<statement>`. There needs to be some way to say “If `<expr>` is true, do all of the following things.”

The usual approach taken by most programming languages is to define a syntactic device that groups multiple statements into one compound statement or block. A block is regarded syntactically as a single entity. When it is the target of an if statement, and `<expr>` is true, then all the statements in the block are executed. If `<expr>` is false, then none of them are.

Virtually all programming languages provide the capability to define blocks, but they don’t all provide it in the same way. Let’s see how Python does it.

###### Python: It’s All About the Indentation
Python follows a convention known as the off-side rule, a term coined by British computer scientist Peter J. Landin. (The term is taken from the offside law in association football.) Languages that adhere to the off-side rule define blocks by indentation. Python is one of a relatively small set of off-side rule languages.

Recall from the previous tutorial on Python program structure that indentation has special significance in a Python program. Now you know why: indentation is used to define compound statements or blocks. In a Python program, contiguous statements that are indented to the same level are considered to be part of the same block.

Thus, a compound if statement in Python looks like this:
```py
if <expr>:
    <statement>
    <statement>
    ...
    <statement>
<following_statement>
```

Here, all the statements at the matching indentation level (lines 2 to 5) are considered part of the same block. The entire block is executed if `<expr>` is true, or skipped over if `<expr>` is false. Either way, execution proceeds with `<following_statement>` (line 6) afterward.

![alt text](image-3.png)

Notice that there is no token that denotes the end of the block. Rather, the end of the block is indicated by a line that is indented less than the lines of the block itself.

>Note: In the Python documentation, a group of statements defined by indentation is often referred to as a suite. This tutorial series uses the terms block and suite interchangeably.

Consider this script file foo.py:

```py
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')
```

Running foo.py produces this output:

```
C:\> python foo.py
After conditional
```

The four print() statements on lines 2 to 5 are indented to the same level as one another. They constitute the block that would be executed if the condition were true. But it is false, so all the statements in the block are skipped. After the end of the compound if statement has been reached (whether the statements in the block on lines 2 to 5 are executed or not), execution proceeds to the first statement having a lesser indentation level: the print() statement on line 6.

Blocks can be nested to arbitrary depth. Each indent defines a new block, and each outdent ends the preceding block. The resulting structure is straightforward, consistent, and intuitive.

Here is a more complicated script file called blocks.py:

```py
# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x
```
The output generated when this script is run is shown below:
```
C:\> python blocks.py
Outer condition is true
Between inner conditions
Inner condition 2
End of outer condition
After outer condition
```
> Note: In case you have been wondering, the off-side rule is the reason for the necessity of the extra newline when entering multiline statements in a REPL session. The interpreter otherwise has no way to know that the last statement of the block has been entered.

##### The else and elif Clauses

Now you know how to use an if statement to conditionally execute a single statement or a block of several statements. It’s time to find out what else you can do.

Sometimes, you want to evaluate a condition and take one path if it is true but specify an alternative path if it is not. This is accomplished with an else clause:

```py
if <expr>:
    <statement(s)>
else:
    <statement(s)>
```
If `<expr>` is true, the first suite is executed, and the second is skipped. If `<expr>` is false, the first suite is skipped and the second is executed. Either way, execution then resumes after the second suite. Both suites are defined by indentation, as described above.

In this example, x is less than 50, so the first suite (lines 4 to 5) are executed, and the second suite (lines 7 to 8) are skipped:
```py
>>> x = 20

>>> if x < 50:
...     print('(first suite)')
...     print('x is small')
... else:
...     print('(second suite)')
...     print('x is large')
...
(first suite)
x is small
```
Here, on the other hand, x is greater than 50, so the first suite is passed over, and the second suite executed:
```py
>>> x = 120
>>>
>>> if x < 50:
...     print('(first suite)')
...     print('x is small')
... else:
...     print('(second suite)')
...     print('x is large')
...
```
```
(second suite)
x is large
```
There is also syntax for branching execution based on several alternatives. For this, use one or more elif (short for else if) clauses. Python evaluates each <expr> in turn and executes the suite corresponding to the first that is true. If none of the expressions are true, and an else clause is specified, then its suite is executed:

```py
if <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
    ...
else:
    <statement(s)>
```
An arbitrary number of elif clauses can be specified. The else clause is optional. If it is present, there can be only one, and it must be specified last:

```py
>>> name = 'Joe'
>>> if name == 'Fred':
...     print('Hello Fred')
... elif name == 'Xander':
...     print('Hello Xander')
... elif name == 'Joe':
...     print('Hello Joe')
... elif name == 'Arnold':
...     print('Hello Arnold')
... else:
...     print("I don't know who you are!")
...
```
```
Hello Joe
```
At most, one of the code blocks specified will be executed. If an else clause isn’t included, and all the conditions are false, then none of the blocks will be executed.

> Note: Using a lengthy if/elif/else series can be a little inelegant, especially when the actions are simple statements like print(). In many cases, there may be a more Pythonic way to accomplish the same thing.
> 
> Here’s one possible alternative to the example above using the dict.get() method:
> ```py
> >>> names = {
> ...     'Fred': 'Hello Fred',
> ...     'Xander': 'Hello Xander',
> ...     'Joe': 'Hello Joe',
> ...     'Arnold': 'Hello Arnold'
> ... }
> 
> >>> print(names.get('Joe', "I don't know who you are!"))
> Hello Joe
> >>> print(names.get('Rick', "I don't know who you are!"))
> I don't know who you are!
> ```
> Recall from the tutorial on Python dictionaries that the dict.get() method searches a dictionary for the specified key and returns the associated value if it is found, or the given default value if it isn’t.

An if statement with elif clauses uses short-circuit evaluation, analogous to what you saw with the and and or operators. Once one of the expressions is found to be true and its block is executed, none of the remaining expressions are tested. This is demonstrated below:

```py
>>> var  # Not defined
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    var
NameError: name 'var' is not defined

>>> if 'a' in 'bar':
...     print('foo')
... elif 1/0:
...     print("This won't happen")
... elif var:
...     print("This won't either")
...
```
```
foo
```

The second expression contains a division by zero, and the third references an undefined variable var. Either would raise an error, but neither is evaluated because the first condition specified is true.

###### One-Line if Statements
It is customary to write if <expr> on one line and <statement> indented on the following line like this:

```py
if <expr>:
    <statement>
```
But it is permissible to write an entire if statement on one line. The following is functionally equivalent to the example above:

```py
if <expr>: <statement>
```
There can even be more than one <statement> on the same line, separated by semicolons:
```py
if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
```

But what does this mean? There are two possible interpretations:

1. If `<expr>` is true, execute `<statement_1>`.

    Then, execute <statement_2> ... <statement_n> unconditionally, irrespective of whether <expr> is true or not.

2. If `<expr>` is true, execute all of `<statement_1>` ... `<statement_n>`. Otherwise, don’t execute any of them.

Python takes the latter interpretation. The semicolon separating the <statements> has higher precedence than the colon following <expr>—in computer lingo, the semicolon is said to bind more tightly than the colon. Thus, the <statements> are treated as a suite, and either all of them are executed, or none of them are:

```py
>>> if 'f' in 'foo': print('1'); print('2'); print('3')
...
1
2
3
>>> if 'z' in 'foo': print('1'); print('2'); print('3')
...
```
Multiple statements may be specified on the same line as an elif or else clause as well:

```py
>>> x = 2
>>> if x == 1: print('foo'); print('bar'); print('baz')
... elif x == 2: print('qux'); print('quux')
... else: print('corge'); print('grault')
...
```
```
qux
quux
```
```py
>>> x = 3
>>> if x == 1: print('foo'); print('bar'); print('baz')
... elif x == 2: print('qux'); print('quux')
... else: print('corge'); print('grault')
...
```
```
corge
grault
```
While all of this works, and the interpreter allows it, it is generally discouraged on the grounds that it leads to poor readability, particularly for complex if statements. PEP 8 specifically recommends against it.

As usual, it is somewhat a matter of taste. Most people would find the following more visually appealing and easier to understand at first glance than the example above:

```py
>>> x = 3
>>> if x == 1:
...     print('foo')
...     print('bar')
...     print('baz')
... elif x == 2:
...     print('qux')
...     print('quux')
... else:
...     print('corge')
...     print('grault')
...
```
```
corge
grault
```

If an if statement is simple enough, though, putting it all on one line may be reasonable. Something like this probably wouldn’t raise anyone’s hackles too much:
```py
debugging = True  # Set to True to turn debugging on.

    .
    .
    .

if debugging: print('About to call function foo()')
foo()
```

###### Conditional Expressions (Python’s Ternary Operator)

Python supports one additional decision-making entity called a conditional expression. 
(It is also referred to as a conditional operator or ternary operator in various places in the Python documentation.) 
Conditional expressions were proposed for addition to the language in PEP 308 and green-lighted by Guido in 2005.

In its simplest form, the syntax of the conditional expression is as follows:

```py
<expr1> if <conditional_expr> else <expr2>
```

This is different from the if statement forms listed above because it is not a control structure that directs the flow of program execution. It acts more like an operator that defines an expression. In the above example, `<conditional_expr>` is evaluated first. If it is true, the expression evaluates to `<expr1>`. If it is false, the expression evaluates to `<expr2>`.

Notice the non-obvious order: the middle expression is evaluated first, and based on that result, one of the expressions on the ends is returned. Here are some examples that will hopefully help clarify:

```py
>>> raining = False
>>> print("Let's go to the", 'beach' if not raining else 'library')
Lets go to the beach
>>> raining = True
>>> print("Lets go to the", 'beach' if not raining else 'library')
Lets go to the library

>>> age = 12
>>> s = 'minor' if age < 21 else 'adult'
>>> s
'minor'

>>> 'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
'no'
```
> Note: Python’s conditional expression is similar to the <conditional_expr> ? <expr1> : <expr2> syntax used by many other languages—C, Perl and Java to name a few. In fact, the ?: operator is commonly called the ternary operator in those languages, which is probably the reason Python’s conditional expression is sometimes referred to as the Python ternary operator.
>
> You can see in PEP 308 that the <conditional_expr> ? <expr1> : <expr2> syntax was considered for Python but ultimately rejected in favor of the syntax shown above.

A common use of the conditional expression is to select variable assignment. For example, suppose you want to find the larger of two numbers. Of course, there is a built-in function, max(), that does just this (and more) that you could use. But suppose you want to write your own code from scratch.

You could use a standard if statement with an else clause:

```py
>>> if a > b:
...     m = a
... else:
...     m = b
...
```
But a conditional expression is shorter and arguably more readable as well:

```py
>>> m = a if a > b else b
```

Remember that the conditional expression behaves like an expression syntactically. It can be used as part of a longer expression. The conditional expression has lower precedence than virtually all the other operators, so parentheses are needed to group it by itself.

In the following example, the + operator binds more tightly than the conditional expression, so 1 + x and y + 2 are evaluated first, followed by the conditional expression. The parentheses in the second case are unnecessary and do not change the result:
```py
>>> x = y = 40

>>> z = 1 + x if x > y else y + 2
>>> z
42

>>> z = (1 + x) if x > y else (y + 2)
>>> z
42
```

If you want the conditional expression to be evaluated first, you need to surround it with grouping parentheses. In the next example, (x if x > y else y) is evaluated first. The result is y, which is 40, so z is assigned 1 + 40 + 2 = 43:
```py
>>> x = y = 40

>>> z = 1 + (x if x > y else y) + 2
>>> z
43
```

If you are using a conditional expression as part of a larger expression, it probably is a good idea to use grouping parentheses for clarification even if they are not needed.

Conditional expressions also use short-circuit evaluation like compound logical expressions. Portions of a conditional expression are not evaluated if they don’t need to be.

In the expression` <expr1>` if `<conditional_expr>` else `<expr2>`:
* If `<conditional_expr>` is true, `<expr1>` is returned and `<expr2>` is not evaluated.
* If `<conditional_expr>` is false, `<expr2>` is returned and `<expr1>` is not evaluated.

As before, you can verify this by using terms that would raise an error:

```py
>>> 'foo' if True else 1/0
'foo'
>>> 1/0 if False else 'bar'
'bar'
```
In both cases, the 1/0 terms are not evaluated, so no exception is raised.

Conditional expressions can also be chained together, as a sort of alternative if/elif/else structure, as shown here:

```py
>>> s = ('foo' if (x == 1) else
...      'bar' if (x == 2) else
...      'baz' if (x == 3) else
...      'qux' if (x == 4) else
...      'quux'
... )
>>> s
'baz'
```

It’s not clear that this has any significant advantage over the corresponding if/elif/else statement, but it is syntactically correct Python.

###### The Python pass Statement
Occasionally, you may find that you want to write what is called a code stub: a placeholder for where you will eventually put a block of code that you haven’t implemented yet.

In languages where token delimiters are used to define blocks, like the curly braces in Perl and C, empty delimiters can be used to define a code stub. For example, the following is legitimate Perl or C code:

```Perl
# This is not Python
if (x) {

}
```

Here, the empty curly braces define an empty block. Perl or C will evaluate the expression x, and then even if it is true, quietly do nothing.

Because Python uses indentation instead of delimiters, it is not possible to specify an empty block. If you introduce an if statement with if <expr>:, something has to come after it, either on the same line or indented on the following line.

Consider this script foo.py:

```py
if True:

print('foo')
```

If you try to run foo.py, you’ll get this:

```sh
C:\> python foo.py
  File "foo.py", line 3
    print('foo')
        ^
IndentationError: expected an indented block
```

The Python pass statement solves this problem. It doesn’t change program behavior at all. It is used as a placeholder to keep the interpreter happy in any situation where a statement is syntactically required, but you don’t really want to do anything:

```py
if True:
    pass

print('foo')
```
Now foo.py runs without error:
```sh
C:\> python foo.py
foo
```

### Loops
**`Iteration`** means executing the same block of code over and over, potentially many times. A programming structure that implements `iteration` is called a `loop`.

In programming, there are two types of `iteration`, indefinite and definite:

*   With `indefinite iteration`, the number of times the loop is executed isn’t specified explicitly in advance. Rather, the designated block is executed repeatedly as long as some condition is met.

*   With `definite iteration`, the number of times the designated block will be executed is specified explicitly at the time the loop starts.

In this tutorial, you’ll:

*   Learn about the while loop, the Python control structure used for indefinite `iteration`
*   See how to break out of a loop or loop `iteration` prematurely
*   Explore infinite loops

When you’re finished, you should have a good grasp of how to use indefinite `iteration` in Python.

#### The while Loop
Let’s see how Python’s while statement is used to construct loops. We’ll start simple and embellish as we go.

The format of a rudimentary while loop is shown below:

```py
while <expr>:
    <statement(s)>
```
`<statement(s)>` represents the block to be repeatedly executed, often referred to as the body of the loop. This is denoted with indentation, just as in an if statement.

> **Remember:** All control structures in Python use indentation to define blocks. See the discussion on grouping statements in the previous tutorial to review.

The controlling expression, `<expr>`, typically involves one or more variables that are initialized prior to starting the loop and then modified somewhere in the loop body.

When a while loop is encountered, `<expr>` is first evaluated in Boolean context. If it is true, the loop body is executed. Then `<expr>` is checked again, and if still true, the body is executed again. This continues until `<expr>` becomes false, at which point program execution proceeds to the first statement beyond the loop body.

Consider this loop:

```py
>>> n = 5
>>> while n > 0:
...     n -= 1
...     print(n)
...
4
3
2
1
0
```
Here’s what’s happening in this example:

*   n is initially 5. The expression in the while statement header on line 2 is n > 0, which is true, so the loop body executes. Inside the loop body on line 3, n is decremented by 1 to 4, and then printed.

*   When the body of the loop has finished, program execution returns to the top of the loop at line 2, and the expression is evaluated again. It is still true, so the body executes again, and 3 is printed.

*   This continues until n becomes 0. At that point, when the expression is tested, it is false, and the loop terminates. Execution would resume at the first statement following the loop body, but there isn’t one in this case.

Note that the controlling expression of the while loop is tested first, before anything else happens. If it’s false to start with, the loop body will never be executed at all:

```py
>>> n = 0
>>> while n > 0:
...     n -= 1
...     print(n)
...
```

In the example above, when the loop is encountered, n is 0. The controlling expression n > 0 is already false, so the loop body never executes.

Here’s another while loop involving a list, rather than a numeric comparison:

```py
>>> a = ['foo', 'bar', 'baz']
>>> while a:
...     print(a.pop(-1))
...
baz
bar
foo
```
When a list is evaluated in Boolean context, it is truthy if it has elements in it and falsy if it is empty. In this example, a is true as long as it has elements in it. Once all the items have been removed with the .pop() method and the list is empty, a is false, and the loop terminates.

##### The Python break and continue Statements


In each example you have seen so far, the entire body of the while loop is executed on each iteration. Python provides two keywords that terminate a loop iteration prematurely:

*   The Python break statement immediately terminates a loop entirely. Program execution proceeds to the first statement following the loop body.

*   The Python continue statement immediately terminates the current loop iteration. Execution jumps to the top of the loop, and the controlling expression is re-evaluated to determine whether the loop will execute again or terminate.

The distinction between break and continue is demonstrated in the following diagram:

![alt text](image-4.png) - break and continue

Here’s a script file called break.py that demonstrates the break statement:

```py
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')
```

Running break.py from a command-line interpreter produces the following output:
```sh
C:\Users\john\Documents>python break.py
4
3
Loop ended.
```
When n becomes 2, the break statement is executed. The loop is terminated completely, and program execution jumps to the print() statement on line 7.

> **Note**: If your programming background is in C, C++, Java, or JavaScript, then you may be wondering where Python’s do-while loop is. Well, the bad news is that Python doesn’t have a do-while construct. But the good news is that you can use a while loop with a break statement to emulate it.

The next script, continue.py, is identical except for a continue statement in place of the break:
```py
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')
```

The output of continue.py looks like this:

```py
C:\Users\john\Documents>python continue.py
4
3
1
0
Loop ended.
```
This time, when n is 2, the continue statement causes termination of that iteration. Thus, 2 isn’t printed. Execution returns to the top of the loop, the condition is re-evaluated, and it is still true. The loop resumes, terminating when n becomes 0, as previously.

##### The else Clause

Python allows an optional else clause at the end of a while loop. This is a unique feature of Python, not found in most other programming languages. The syntax is shown below:

```py
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```

The `<additional_statement(s)>` specified in the else clause will be executed when the while loop terminates.


About now, you may be thinking, “How is that useful?” You could accomplish the same thing by putting those statements immediately after the while loop, without the else:

```py
while <expr>:
    <statement(s)>
<additional_statement(s)>
```

What’s the difference?

In the latter case, without the else clause, `<additional_statement(s)>` will be executed after the while loop terminates, no matter what.

When `<additional_statement(s)>` are placed in an else clause, they will be executed only if the loop terminates “by exhaustion”—that is, if the loop iterates until the controlling condition becomes false. If the loop is exited by a break statement, the else clause won’t be executed.

Consider the following example:

```py
>>> n = 5
>>> while n > 0:
...     n -= 1
...     print(n)
... else:
...     print('Loop done.')
...
4
3
2
1
0
Loop done.
```

In this case, the loop repeated until the condition was exhausted: n became 0, so n > 0 became false. Because the loop lived out its natural life, so to speak, the else clause was executed. Now observe the difference here:

```py
>>> n = 5
>>> while n > 0:
...     n -= 1
...     print(n)
...     if n == 2:
...         break
... else:
...     print('Loop done.')
...
4
3
2
```

This loop is terminated prematurely with break, so the else clause isn’t executed.

It may seem as if the meaning of the word else doesn’t quite fit the while loop as well as it does the if statement. Guido van Rossum, the creator of Python, has actually said that, if he had it to do over again, he’d leave the while loop’s else clause out of the language.

One of the following interpretations might help to make it more intuitive:

*   Think of the header of the loop (while n > 0) as an if statement (if n > 0) that gets executed over and over, with the else clause finally being executed when the condition becomes false.

*   Think of else as though it were nobreak, in that the block that follows gets executed if there wasn’t a break.

If you don’t find either of these interpretations helpful, then feel free to ignore them.

When might an else clause on a while loop be useful? One common situation is if you are searching a list for a specific item. You can use break to exit the loop if the item is found, and the else clause can contain code that is meant to be executed if the item isn’t found:

```py
>>> a = ['foo', 'bar', 'baz', 'qux']
>>> s = 'corge'

>>> i = 0
>>> while i < len(a):
...     if a[i] == s:
...         # Processing for item found
...         break
...     i += 1
... else:
...     # Processing for item not found
...     print(s, 'not found in list.')
...
corge not found in list.
```

> Note: The code shown above is useful to illustrate the concept, but you’d actually be very unlikely to search a list that way.
> 
> First of all, lists are usually processed with definite iteration, not a while loop. Definite iteration is covered in the next tutorial in this series.
> 
> Secondly, Python provides built-in ways to search for an item in a list. You can use the in operator:
> ```py
> >>> if s in a:
> ...     print(s, 'found in list.')
> ... else:
> ...     print(s, 'not found in list.')
> ...
> corge not found in list.
> ```
> The list.index() method would also work. This method raises a ValueError exception if the item isn’t found in the list, so you need to understand exception handling to use it. In Python, you use a try statement to handle an exception. An example is given below:
> ```py
> >>> try:
> ...     print(a.index('corge'))
> ... except ValueError:
> ...     print(s, 'not found in list.')
> ...
> corge not found in list.
> ```
> You will learn about exception handling later in this series.

An else clause with a while loop is a bit of an oddity, not often seen. But don’t shy away from it if you find a situation in which you feel it adds clarity to your code!

##### Infinite Loops

Suppose you write a while loop that theoretically never ends. Sounds weird, right?

Consider this example:

```py
>>> while True:
...     print('foo')
...
foo
foo
foo
  .
  .
  .
foo
foo
foo
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    print('foo')
KeyboardInterrupt
````

This code was terminated by Ctrl+C, which generates an interrupt from the keyboard. Otherwise, it would have gone on unendingly. Many foo output lines have been removed and replaced by the vertical ellipsis in the output shown.

Clearly, True will never be false, or we’re all in very big trouble. Thus, while True: initiates an infinite loop that will theoretically run forever.

Maybe that doesn’t sound like something you’d want to do, but this pattern is actually quite common. For example, you might write code for a service that starts up and runs forever accepting service requests. “Forever” in this context means until you shut it down, or until the heat death of the universe, whichever comes first.

More prosaically, remember that loops can be broken out of with the break statement. It may be more straightforward to terminate a loop based on conditions recognized within the loop body, rather than on a condition evaluated at the top.

Here’s another variant of the loop shown above that successively removes items from a list using .pop() until it is empty:

```py
>>> a = ['foo', 'bar', 'baz']
>>> while True:
...     if not a:
...         break
...     print(a.pop(-1))
...
baz
bar
foo
```
When a becomes empty, not a becomes true, and the break statement exits the loop.

You can also specify multiple break statements in a loop:

```py
while True:
    if <expr1>:  # One condition for loop termination
        break
    ...
    if <expr2>:  # Another termination condition
        break
    ...
    if <expr3>:  # Yet another
        break
```

In cases like this, where there are multiple reasons to end the loop, it is often cleaner to break out from several different locations, rather than try to specify all the termination conditions in the loop header.

Infinite loops can be very useful. Just remember that you must ensure the loop gets broken out of at some point, so it doesn’t truly become infinite.

##### Nested while Loops

In general, Python control structures can be nested within one another. For example, if/elif/else conditional statements can be nested:
```py
if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')
```

Similarly, a while loop can be contained within another while loop, as shown here:
```py
>>> a = ['foo', 'bar']
>>> while len(a):
...     print(a.pop(0))
...     b = ['baz', 'qux']
...     while len(b):
...         print('>', b.pop(0))
...
foo
> baz
> qux
bar
> baz
> qux
```

A break or continue statement found within nested loops applies to the nearest enclosing loop:
```py
while <expr1>:
    statement
    statement

    while <expr2>:
        statement
        statement
        break  # Applies to while <expr2>: loop

    break  # Applies to while <expr1>: loop
```

Additionally, while loops can be nested inside if/elif/else statements, and vice versa:
```py
if <expr>:
    statement
    while <expr>:
        statement
        statement
else:
    while <expr>:
        statement
        statement
    statement
```
```py
while <expr>:
    if <expr>:
        statement
    elif <expr>:
        statement
    else:
        statement

    if <expr>:
        statement
```

In fact, all the Python control structures can be intermingled with one another to whatever extent you need. That is as it should be. Imagine how frustrating it would be if there were unexpected restrictions like “A while loop can’t be contained within an if statement” or “while loops can only be nested inside one another at most four deep.” You’d have a very difficult time remembering them all.

Seemingly arbitrary numeric or logical limitations are considered a sign of poor program language design. Happily, you won’t find many in Python.

##### One-Line while Loops
As with an if statement, a while loop can be specified on one line. If there are multiple statements in the block that makes up the loop body, they can be separated by semicolons (;):

```py
>>> n = 5
>>> while n > 0: n -= 1; print(n)

4
3
2
1
0
```

This only works with simple statements though. You can’t combine two compound statements into one line. Thus, you can specify a while loop all on one line as above, and you write an if statement on one line:

```py
>>> if True: print('foo')

foo
```
But you can’t do this:

```py
>>> while n > 0: n -= 1; if True: print('foo')
SyntaxError: invalid syntax
```
Remember that PEP 8 discourages multiple statements on one line. So you probably shouldn’t be doing any of this very often anyhow.

#### The for Loop
This tutorial will show you how to perform definite iteration with a Python for loop.

In the previous tutorial in this introductory series, you learned the following:

Repetitive execution of the same block of code over and over is referred to as iteration.
There are two types of iteration:
Definite iteration, in which the number of repetitions is specified explicitly in advance
Indefinite iteration, in which the code block executes until some condition is met
In Python, indefinite iteration is performed with a while loop.
Here’s what you’ll cover in this tutorial:

You’ll start with a comparison of some different paradigms used by programming languages to implement definite iteration.

Then you will learn about iterables and iterators, two concepts that form the basis of definite iteration in Python.

Finally, you’ll tie it all together and learn about Python’s for loops.

##### A Survey of Definite Iteration in Programming


### Functions
You may be familiar with the mathematical concept of a function. A function is a relationship or mapping between one or more inputs and a set of outputs. In mathematics, a function is typically represented like this:

![alt text](image-5.png)

Here, f is a function that operates on the inputs x and y. The output of the function is z. However, programming functions are much more generalized and versatile than this mathematical definition. In fact, appropriate function definition and use is so critical to proper software development that virtually all modern programming languages support both built-in and user-defined functions.

In programming, a function is a self-contained block of code that encapsulates a specific task or related group of tasks. In previous tutorials in this series, you’ve been introduced to some of the built-in functions provided by Python. id(), for example, takes one argument and returns that object’s unique integer identifier:
```py
>>> s = 'foobar'
>>> id(s)
56313440
```

len() returns the length of the argument passed to it:

```py
>>> a = ['foo', 'bar', 'baz', 'qux']
>>> len(a)
4
```
any() takes an iterable as its argument and returns True if any of the items in the iterable are truthy and False otherwise:
```py
>>> any([False, False, False])
False
>>> any([False, True, False])
True

>>> any(['bar' == 'baz', len('foo') == 4, 'qux' in {'foo', 'bar', 'baz'}])
False
>>> any(['bar' == 'baz', len('foo') == 3, 'qux' in {'foo', 'bar', 'baz'}])
True
```
Each of these built-in functions performs a specific task. The code that accomplishes the task is defined somewhere, but you don’t need to know where or even how the code works. All you need to know about is the function’s interface:

1.   What arguments (if any) it takes
2.   What values (if any) it returns

Then you call the function and pass the appropriate arguments. Program execution goes off to the designated body of code and does its useful thing. When the function is finished, execution returns to your code where it left off. The function may or may not return data for your code to use, as the examples above do.

When you define your own Python function, it works just the same. From somewhere in your code, you’ll call your Python function and program execution will transfer to the body of code that makes up the function.

> Note: In this case, you will know where the code is and exactly how it works because you wrote it!

When the function is finished, execution returns to the location where the function was called. Depending on how you designed the function’s interface, data may be passed in when the function is called, and return values may be passed back when it finishes.

#### The Importance of Python Functions
Virtually all programming languages used today support a form of user-defined functions, although they aren’t always called functions. In other languages, you may see them referred to as one of the following:

*   Subroutines
*   Procedures
*   Methods
*   Subprograms

So, why bother defining functions? There are several very good reasons. Let’s go over a few now.

##### Abstraction and Reusability
Suppose you write some code that does something useful. As you continue development, you find that the task performed by that code is one you need often, in many different locations within your application. What should you do? Well, you could just replicate the code over and over again, using your editor’s copy-and-paste capability.

Later on, you’ll probably decide that the code in question needs to be modified. You’ll either find something wrong with it that needs to be fixed, or you’ll want to enhance it in some way. If copies of the code are scattered all over your application, then you’ll need to make the necessary changes in every location.

> Note: At first blush, that may seem like a reasonable solution, but in the long term, it’s likely to be a maintenance nightmare! While your code editor may help by providing a search-and-replace function, this method is error-prone, and you could easily introduce bugs into your code that will be difficult to find.

A better solution is to define a Python function that performs the task. Anywhere in your application that you need to accomplish the task, you simply call the function. Down the line, if you decide to change how it works, then you only need to change the code in one location, which is the place where the function is defined. The changes will automatically be picked up anywhere the function is called.

The abstraction of functionality into a function definition is an example of the Don’t Repeat Yourself (DRY) Principle of software development. This is arguably the strongest motivation for using functions.

##### Modularity

Functions allow complex processes to be broken up into smaller steps. 
Imagine, for example, that you have a program that reads in a file, processes the file contents, and then writes an output file. Your code could look like this:

```py
# Main program

# Code to read file in
<statement>
<statement>
<statement>
<statement>

# Code to process file
<statement>
<statement>
<statement>
<statement>

# Code to write file out
<statement>
<statement>
<statement>
<statement>
```

In this example, the main program is a bunch of code strung together in a long sequence, with whitespace and comments to help organize it. However, if the code were to get much lengthier and more complex, then you’d have an increasingly difficult time wrapping your head around it.

Alternatively, you could structure the code more like the following:

```py
def read_file():
    # Code to read file in
    <statement>
    <statement>
    <statement>
    <statement>

def process_file():
    # Code to process file
    <statement>
    <statement>
    <statement>
    <statement>

def write_file():
    # Code to write file out
    <statement>
    <statement>
    <statement>
    <statement>


# Main program
read_file()
process_file()
write_file()
```
This example is modularized. Instead of all the code being strung together, it’s broken out into separate functions, each of which focuses on a specific task. Those tasks are read, process, and write. The main program now simply needs to call each of these in turn.

> Note: The def keyword introduces a new Python function definition. You’ll learn all about this very soon.

1. In life, you do this sort of thing all the time, even if you don’t explicitly think of it that way. If you wanted to move some shelves full of stuff from one side of your garage to the other, then you hopefully wouldn’t just stand there and aimlessly think, “Oh, geez. I need to move all that stuff over there! How do I do that???” You’d divide the job into manageable steps:
1. Take all the stuff off the shelves.
1. Take the shelves apart.
1. Carry the shelf parts across the garage to the new location.
1. Re-assemble the shelves.
1. Carry the stuff across the garage.
1. Put the stuff back on the shelves.


### classes
In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.

