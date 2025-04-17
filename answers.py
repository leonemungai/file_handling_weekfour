def modify_content(content):
    """
    Modify the file content.
     ie, Converts text to uppercase.
    """
    return content.upper()

def main():
    try:
        # Ask user for the input filename
        input_file = input("Enter the name of the file to read: ")

        # Attempt to read the file
        with open(input_file, 'r') as file:
            original_content = file.read()

        # Modify the content
        modified_content = modify_content(original_content)

        # Ask user for the output filename
        output_file = input("Enter the name for the new file to save modified content: ")

        # Write the modified content to a new file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to '{output_file}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please check the filename.")
    except IOError:
        print(f"Error: There was a problem reading or writing files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
