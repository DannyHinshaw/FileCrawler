import os, sys, re


def edit(x, t, r):
    # 'x' will be the filename passed to editor, 't' is the target string, 'r' is the replacement string
    print(x)
    global file_data

    # Open and read our given file and save it's contents to file_data variable
    with open(x, 'r') as file:
        file_data = file.read()

    # Using regex do a find and replace with our given strings
    file_data = re.sub(t, r, file_data)

    # Reopen the given file and write over it with our new file_data content
    with open(x, 'w') as file:
        file.write(file_data)


def commandErr():

    print('You entered an invalid command, please try again')


def typeCheck(ext):

    # regex variable to be used to detect any html/xml extensions in files
    warn = re.compile(r'\.htm$|\.html$|\.xml$')

    # Loop to go through all given files and check for file extensions
    for x in ext:

        # If one of the above extension types is found, program flow will alter to this
        if warn.search(x):
            user_input = input('WARNING: Parsing html/xml with regex may give unexpected results. Continue? (y/n): ')
            user_input = user_input.lower().strip()

            # Check user input and make sure it's valid
            if user_input in 'n':
                endOptions()
            elif user_input not in 'y':
                commandErr()
                typeCheck(ext)

            break


def restart():
    # File path to our filecrawler.py file
    python = sys.executable
    # For any file path leading to filecrawler.py that may contain a space
    if " " in python:
        main()
    # Otherwise, restart by completely closing and restarting program
    else:
        os.execl(python, python, * sys.argv)


def endOptions():

    user_input = input('Would you like to exit (e) or restart (r) the program? (e/r): ').lower()
    if user_input == 'r':
        restart()
    elif user_input == 'e':
        sys.exit()
    else:
        commandErr()
        endOptions()


def main():
    # Prompt the user for input variables
    path = input('Enter the file directory to crawl: ')
    file_types = [f.strip() for f in input('Enter the files you would like to edit (separated by commas): ').split(",")]
    typeCheck(file_types)
    target = input('Enter Regex for string to replace: ')
    replacement = input('Enter replacement string: ')

    # List comprehension used to crawl the given directory and search for matching files
    for root, dirs, files in os.walk(path):
        [edit(os.path.join(root, name), target, replacement) for name in files for ft in file_types if ft in name]


if __name__ == "__main__":
    print('\n*************************************       FileCrawler       **************************************\n'
          '- First, specify the full path of the directory you want to work within\n'
          '- If you are editing multiple files separate them by commas\n'
          '- You can choose specific files by entering their names and extensions (ie example.txt, example.css)\n'
          '- You can select all files with a certain extension by entering the extensions (ie .txt, .css)\n'
          '****************************************************************************************************\n')

    main()
