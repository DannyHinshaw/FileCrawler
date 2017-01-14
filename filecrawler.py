import os, sys, re

# TODO:
"""
1. Examples: Hex codes , id's and CSS classes (ie #248B5, #I'm_an-ID, .stupid_fucking_class).
"""


def edit(x, t, r):

    print(x)
    global file_data

    with open(x, 'r') as file:
        file_data = file.read()

    file_data = re.sub(t, r, file_data)

    with open(x, 'w') as file:
        file.write(file_data)


def commandErr():

    print('You entered an invalid command, please try again')


def typeCheck(ext):

    warn = re.compile(r'\.htm$|\.html$|\.xml$')

    for x in ext:

        if warn.search(x):
            user_input = input('WARNING: Parsing html/xml with regex may give unexpected results. Continue? (y/n): ')
            user_input = user_input.lower().strip()

            if user_input in 'n':
                endOptions()
                """ Not sure if necessary...
                try:
                    endOptions()
                except TypeError:
                    commandErr()
                    typeCheck(ext)
                """
            elif user_input not in 'y':
                commandErr()
                typeCheck(ext)

            break


def restart():

    python = sys.executable
    # For any file path that may contain a space
    if " " in python:
        main()
    else:
        # Preferable restart method... why?
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

    path = input('Enter the file directory to crawl: ')
    file_types = input('Enter the files you would like to edit (separated by commas): ').replace(" ", "").split(",")

    typeCheck(file_types)

    target = input('Enter Regex for string to replace: ')
    replacement = input('Enter replacement string: ')

    for root, dirs, files in os.walk(path):
        [edit(os.path.join(root, name), target, replacement) for name in files for ft in file_types if ft in name]

    print('Program complete.')
    endOptions()


if __name__ == "__main__":
    print('\n*************************************       FileCrawler       **************************************\n'
          '- First, specify the full path of the directory you want to work within\n'
          '- If you are editing multiple files separate them by commas\n'
          '- You can choose specific files by entering their names and extensions (ie example.txt, example.css)\n'
          '- You can select all files with a certain extension by entering the extensions (ie .txt, .css)\n'
          '****************************************************************************************************\n')

    main()
