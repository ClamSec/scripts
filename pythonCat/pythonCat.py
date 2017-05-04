"""Concatenates the three largest files in a directory, saving them to file."""

import os
# Write a Python function
# that takes a directory as an argument
# finds the 3 biggest files in that directory
# and concatenates those files together into a new file


class File:
    """Object representing some operating system file."""

    def __init__(self, filename, fileSize, fileContents):
        """Initialize a File object.

        Args:
            filename: the name of a file.
            fileSize: the size of the file.
            fileContents: the contents of the file.
        """
        self.filename = filename
        self.fileSize = fileSize
        self.fileContents = fileContents

    def getFilename(self):
        """Return the object's filename.

        Returns:
            The object's filename.

        """
        return self.filename

    def getFileSize(self):
        """Return the object's filesize.

        Returns:
            The object's file size.

        """
        return self.fileSize

    def getFileContents(self):
        """Return the object's contents.

        Returns:
            The object's contents.

        """
        return self.fileContents

    def printFileNameAndSize(self):
        """Print the file's filename and file size."""
        filename = self.getFilename()
        fileSize = self.getFileSize()
        print("{0:<32.32} {1:>8}".format(filename, fileSize))


def pythonCat(someDirectory):
    """
    Concatenates the three largest files in a directory, saving them to file.

    Python Concatenater (pythonCat) searches a given directory for the three
    largest files and concatenates their contents into a new file. This new
    file is called newFile.txt by default.

    Currently, the program only works on text files that Python can easily
    convert into strings. This should be fixed in the future.

    Args:
        someDirectory: any given directory.
    Raises:
        UnicodeDecodeError: if a file contains characters that can't be Unicode
        decoded, the issue is caught and that file is skipped.
    """
    files = []
    # Do not include this program or any files this program creates.
    invalidFiles = ["pythonCat.py", "newFile.txt"]
    for systemFile in os.listdir(someDirectory):
        if os.path.isfile(systemFile) and systemFile not in invalidFiles:
            try:
                filename = systemFile
                fileSize = os.stat(systemFile).st_size
                with open(systemFile, 'r') as openSystemFile:
                    fileContents = openSystemFile.read()
                files.append(File(filename, fileSize, fileContents))
            except UnicodeDecodeError:
                print("File: {} contains characters that the 'ascii' codec "
                      "can't decode. Skipping.".format(filename))
                continue

    generateFileTable(files)

    files.sort(key=lambda x: x.getFileSize(), reverse=True)

    print("\n\nFILES SORTED BY SIZE IN DESCENDING ORDER")

    generateFileTable(files)

    concatenatedString = ""
    for i in range(0, 3):
        concatenatedString += files[i].getFileContents()

    with open("newFile.txt", 'w') as newFile:
        newFile.write(concatenatedString)

    print("\nnewFile.txt created from three largest files.")


def generateFileTable(listOfFiles):
    """Print a table showing information on a list of SystemFile objects.

    Args:
        listOfFiles: any list of File objects.

    """
    print("{0:<32} {1:>8}".format("FILE", "SIZE"))
    for item in listOfFiles:
        item.printFileNameAndSize()


def main():
    """Test pythonCat."""
    pythonCat(".")


if __name__ == "__main__":
    main()
