Exception handling in Python is a mechanism to manage errors gracefully during program execution. It involves using **try** and **except** blocks to catch and handle exceptions that occur, 
preventing the program from crashing. The **try** block contains the code that might raise an exception, while the **except** block handles the exception if it occurs. Python also provides 
**else** and **finally** blocks for code that should run if no exception is raised or for cleanup actions, respectively. This approach ensures that programs can handle unexpected situations 
robustly, improving reliability and user experience.

**Built-in Exceptions**
**ZeroDivisionError**: Raised when attempting to divide by zero.

**IndexError**: Raised when trying to access an index that is out of range in a list or other indexable object.

**KeyError**: Raised when accessing a dictionary with a key that does not exist.

**FileNotFoundError**: Raised when trying to open a file that does not exist.

**ValueError**: Raised when a function receives an argument of the right type but inappropriate value (e.g., converting a non-numeric string to an integer).

**TypeError**: Raised when an operation or function is applied to an object of inappropriate type.

**AttributeError**: Raised when an attribute reference or assignment fails.

**NameError**: Raised when a local or global name is not found.

**OverflowError**: Raised when the result of an arithmetic operation is too large to be expressed within the range of the numeric type.

**RuntimeError**: Raised when an error is detected that doesn’t fall into any other category.

**ImportError**: Raised when an import statement fails to find the module or package.

**SyntaxError**: Raised when there is an error in Python syntax.

**IndentationError**: Raised when there is an incorrect indentation level in the code.

**Exception**: The base class for all built-in exceptions except for system-exiting exceptions. It can be used to catch all exceptions that are not caught by more specific exception types.
