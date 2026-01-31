from io import TextIOWrapper


# Define the compiling function
def compile_file(filename: str, output_filename: str) -> None:
    "The compiling function of the compiler"
    file: TextIOWrapper = open(filename, "r") # Open the input file

    lines: list[str] = file.read().split("\n") # Get the lines

    output: str = f"""<!DOCTYPE html>
<html>
    <head>
        <title>{lines[0]}</title>
    </head>
    <body>
""" # Define the output

    # Compile the lines and add to the output
    for line in lines[1:]:
        splitted_line: list[str] = line.split(": ") # Split the line

        # Get the tag and the value
        tag: str = splitted_line[0]
        value: str = splitted_line[1]

        # Check which tag it is and then add to the output with the value
        if tag == "big_header":
            output += f"        <h1>{value}</h1>\n"
        elif tag == "small_header":
            output += f"        <h3>{value}</h3>\n"
        elif tag == "paragraph":
            output += f"        <p>{value}</p>\n"
        elif tag == "openable":
            output += f"""        <details>
            <summary>{value.split("!-!")[0]}</summary>
            <div class='openable_content'>{value.split("!-!")[1]}</div>
        </details>\n"""
        else:
            # Print the error message and then exit program
            print("[ERROR] Unknown tag!")
            quit(-1)

    file.close() # Close the input file

    output += "    </body>\n</html>\n" # Finish the output

    # Open the output file
    output_file: TextIOWrapper = open(output_filename, "w")

    output_file.write(output) # Write the output into the output file

    output_file.close() # Close the output file
