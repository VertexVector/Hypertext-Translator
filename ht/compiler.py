from io import TextIOWrapper


# Define the compiling function
def compile_file(filename: str, output_filename: str, style: str) -> None:
    "The compiling function of the compiler"
    file: TextIOWrapper = open(filename, "r") # Open the input file

    lines: list[str] = file.read().split("\n") # Get the lines

    # Check the style and define the output for it
    if style == "--classic-dark":
        output: str = """<!DOCTYPE html>
<html>
    <head>
        <title>""" + lines[0] + """</title>
    </head>
    <body>
        <style>
            * {
                color: white;
                font-family: "Segoe UI";
            }
            body {
                background-color: black;
            }
            h1 {
                text-shadow: 2px 2px rgb(150, 150, 150);
            }
            h1, h3, p {
                text-align: center;
            }
            details {
                width: fit-content;
                display: block;
                margin: auto;
            }
            input {
                background-color: black;
                border: 1px solid white;
                box-shadow: 3px 3px 0px rgb(150, 150, 150);
                padding: 5px;
                display: block;
                margin: auto;
                transition: background-color 0.2s ease-in-out;
            }
            input:hover {
                background-color: rgb(40, 40, 40);
            }
            form {
                width: fit-content;
                background-color: black;
                border: 1px solid white;
                box-shadow: 5px 5px 0px rgb(150, 150, 150);
                padding: 20px;
                display: block;
                margin: auto;
            }
        </style>
"""
    elif style == "--none":
        output: str = f"""<!DOCTYPE html>
<html>
    <head>
        <title>{lines[0]}</title>
    </head>
    <body>
"""
    else:
        output: str = f"""<!DOCTYPE html>
<html>
    <head>
        <title>{lines[0]}</title>
    </head>
    <body>
"""

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
        elif tag == "form":
            output += f"        <form method='post'>\n" # Prepare the output

            # Get the inputs and the button
            inputs: list[str] = value.split("!-!")[0].split("**")
            button: str = value.split("!-!")[1]

            # Check the inputs and their type and add to the output
            for input in inputs:
                splitted_input: list[str] = input.split("$")

                if splitted_input[0] == "file":
                    output += f"            <input type='file' name='{splitted_input[1]}'>\n"
                else:
                    output += f"            <input type='text' name='{splitted_input[0]}' placeholder='{splitted_input[1]}'>\n"

            # Add the button
            output += f"            <input type='submit' value='{button}' style='cursor: pointer;'>\n"

            output += "        </form>\n" # Finish the output
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
