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

#### Summary
* A variable is a label that you can assign a value to it. The value of a variable can change throughout the program.
* Use the variable_name = value to create a variable.
* The variable names should be as concise and descriptive as possible. Also, they should adhere to Python variable naming rules.
