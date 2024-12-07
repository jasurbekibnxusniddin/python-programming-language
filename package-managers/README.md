# Package Managers

ackage managers allow you to manage the dependencies (external code written by you or someone else) that your project needs to work correctly.

PyPI and Pip are the most common contenders but there are some other options available as well.

Visit the following resources to learn more:

## Pip
The standard package manager for Python is pip. It allows you to install and manage packages that aren’t part of the Python standard library.

In this tutorial, you’ll learn how to:

* Set up pip in your working environment
* Fix common errors related to working with pip
* Install and uninstall packages with pip
* Manage projects’ dependencies using requirements files

You can do a lot with pip, but the Python community is very active and has created some neat alternatives to pip. You’ll learn about those later in this tutorial.

### Getting Started With pip

So, what exactly does pip do? pip is a package manager for Python. That means it’s a tool that allows you to install and manage libraries and dependencies that aren’t distributed as part of the standard library. The name pip was introduced by Ian Bicking in 2008:

> I’ve finished renaming pyinstall to its new name: pip. The name pip is [an] acronym and declaration: pip installs packages. (Source)

Package management is so important that Python’s installers have included pip since versions 3.4 and 2.7.9, for Python 3 and Python 2, respectively. Many Python projects use pip, which makes it an essential tool for every Pythonista.

The concept of a package manager might be familiar to you if you’re coming from another programming language. JavaScript uses npm for package management, Ruby uses gem, and the .NET platform uses NuGet. In Python, pip has become the standard package manager.

#### Finding pip on Your System

The Python installer gives you the option to install pip when installing Python on your system. In fact, the option to install pip with Python is checked by default, so pip should be ready for you to use after installing Python.

> Note: On some Linux (Unix) systems like Ubuntu, pip comes in a separate package called python3-pip, which you need to install with sudo apt install python3-pip. It’s not installed by default with the interpreter.

You can verify that pip is available by looking for the pip3 executable on your system. Select your operating system below and use your platform-specific command accordingly:

> #### windows
>```sh
> PS> where pip3
>```

> #### linux + macOS
>```sh
> $ which pip3
>```

The which command on Linux systems and macOS shows you where the pip3 binary file is located.

On Windows and Unix systems, pip3 may be found in more than one location. This can happen when you have multiple Python versions installed. If you can’t find pip in any location on your system, then you may consider reinstalling pip.

Instead of running your system pip directly, you can also run it as a Python module. In the next section, you’ll learn how.

#### Running pip as a Module

When you run your system pip directly, the command itself doesn’t reveal which Python version pip belongs to. This unfortunately means that you could use pip to install a package into the site-packages of an old Python version without noticing. To prevent this from happening, you should run pip as a Python module:
```sh
$ python -m pip
```

Notice that you use python -m to run pip. The -m switch tells Python to run a module as an executable of the python interpreter. This way, you can ensure that your system default Python version runs the pip command. If you want to learn more about this way of running pip, then you can read Brett Cannon’s insightful article about the advantages of using python -m pip.

> Note: Depending on how you installed Python, your Python executable may have a different name than python. You’ll see python used in this tutorial, but you may have to adapt the commands to use something like py or python3 instead.

Sometimes you may want to be more explicit and limit packages to a specific project. In situations like this, you should run pip inside a virtual environment.

### Using pip in a Python Virtual Environment

To avoid installing packages directly into your system Python installation, you can use a virtual environment. A virtual environment provides an isolated Python interpreter for your project. Any packages that you use inside this environment will be independent of your system interpreter. This means that you can keep your project’s dependencies separate from other projects and the system at large.

Using pip inside a virtual environment has three main advantages. You can:

1. Be sure that you’re using the right Python version for the project at hand
1. Be confident that you’re referring to the correct pip instance when running pip or pip3
1. Use a specific package version for your project without affecting other projects

Python has the built-in venv module for creating virtual environments. This module helps you create virtual environments with an isolated Python installation. Once you’ve activated the virtual environment, then you can install packages into this environment. The packages that you install into one virtual environment are isolated from all other environments on your system.

You can follow these steps to create a virtual environment and verify that you’re using the pip module inside the newly created environment:

> #### on windows
> ```sh
> PS> python -m venv venv\
> PS> venv\Scripts\activate.bat
> 
> (venv) PS>  pip3 --version
> pip 24.2 from ...\lib\site-packages\pip (python 3.12)
> 
> (venv) PS>  pip --version
> pip 24.2 from ...\lib\site-packages\pip (python 3.12)
> ```

> #### on linux/macOS
> ```sh
> $ python -m venv venv/
> $ source venv/bin/activate
> 
> (venv) $ pip3 --version
> pip 24.2 from .../python3.12/site-packages/pip (python 3.12)
> 
> (venv) $ pip --version
> pip 24.2 from .../python3.12/site-packages/pip (python 3.12)
> ```

Here you initialize a virtual environment named venv by using Python’s built-in venv module. After running the command above, Python creates a directory named venv/ in your current working directory. Then, you activate the virtual environment with the source command. The parentheses (()) surrounding your venv name indicate that you successfully activated the virtual environment.

Finally, you check the version of the pip3 and pip executables inside your activated virtual environment. Both point to the same pip module, so once your virtual environment is activated, you can use either pip or pip3. For consistency, you can also continue to use python -m pip inside the virtual environment.

#### Reinstalling pip When Errors Occur

When you run the pip command, you may get an error in some cases. Your specific error message will depend on your operating system:

------------------------------------------------------------------------------
Operating System    |	Error Message
--------------------|----------------------------------------------------------
Windows	            |'pip' is not recognized as an internal or external command operable program or batch file.
Linux	            |bash: pip: command not found
macOS	            |zsh: command not found: pip
-----------------------------------------------------------------------------


Error messages like these indicate that something went wrong with the installation of pip.

> Note: Before you start any troubleshooting when the pip command doesn’t work, you can try out using the pip3 command with the three (3) at the end or the python -m pip alternative calling pip through your Python installation.

































