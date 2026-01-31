# Import the necessary libraries
from sys import argv
from .compiler import compile_file


# Define the running function
def run() -> None:
    "The main function of the compiler"
    # Check if the arguments are right
    if not argv[1] == "" and not argv[1] == None:
        filename: str = argv[1]
        if argv[2] == "" or argv[2] == None:
            output_filename = "output.html"
        else:
            output_filename = argv[2]
        compile_file(filename, output_filename) # Start compiling the file
    else:
        # Print the error message and then exit
        print("[ERROR] No filename entered!")
        quit(-1)
