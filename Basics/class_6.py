#🎁 Exception handling in python

"""
Python provides a try, except, else, and finally block structure for exception handling.

🚀 Try Block: The code that you want to monitor for exceptions is placed inside the try block.

🚀 Except Block: If an exception occurs within the try block, the control immediately jumps to the corresponding except block. Here, you can handle the exception, log the error, or take any necessary corrective actions.

🚀 Else Block (Optional): The else block is executed if no exceptions occur in the try block. It's typically used for code that should only run when no exceptions are raised.

🚀 Finally Block (Optional): The finally block is always executed, regardless of whether an exception occurred. It's useful for cleanup operations like closing files or releasing resources.
"""

try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handling the specific exception
    print("Error: Division by zero!")
except Exception as e:
    # Handling other exceptions
    print(f"An error occurred: {e}")
else:
    # Executed if no exceptions occur
    print("Division successful!")
finally:
    # Cleanup code, always executed
    print("Exiting try-except block")

