"""
    The three functions in this file are used as database
    utilities. The database is used as a phone book.
"""

def DBcreate():
    """ Create a new database with some data """

    # Ask the user for the file name of the database
    # Complete this
    fileName = input("Enter the name of the file to write: ")

    # Open the file for writing
    # Complete this
    dbFile = open(fileName, "w")

    # Ask the user for the name of the new contact
    # Complete this
    name = input("Enter a name: ")

    # Now we will use a while loop to repeatedly ask for new
    # contacts.
    # The while loop ends when the entered name is "done".
    # Complete this inside the while loop:
    while name != "done":

        # 1. Ask the user for the phone number
        # Complete this
        number = input("Enter a phone number: ")

        # 2. Write the new contact to the database file
        # Complete this
        dbFile.write(name + "\n")        
        dbFile.write(number + "\n")

        # 3. Ask the user for the name of the new contact
        # Complete this
        name = input("Enter a name: ")

    # Say "Goodbye!"
    # Complete this
    print("Goodbye!")

    # Close the database file
    # Complete this
    dbFile.close()


# This function, DBappend(), is already completed for you.
# This is given to you. You do not need to change it.
def DBappend():
    """ Append new data to an existing database """

    # Keep trying until we have a valid file name
    while True:
        try:
            # Ask the user for the file name of the database
            fileName = input( \
                    "Enter the name of the file to write: " \
                    )
            # Try reading the file with the given name
            dbFile = open(fileName, "r")
        except IOError: # If the file does not exist
            print("There is no file by that name. Try again...")
        else: # No problem opening the file
            # Close it
            dbFile.close()
            # Open the file again to append new contact data
            dbFile = open(fileName, "a")
            # Exit the infinite while loop
            break

    # Ask the user for the name of the new contact
    name = input("Enter a name: ")

    # Now we will use a while loop to repeatedly ask for new
    # contacts.
    # The while loop ends when the entered name is "done".
    while name != "done":
        # Ask the user for the phone number of the new contact
        number = input("Enter a phone number: ")

        # Write the new contact to the database file
        dbFile.write(name + "\n")
        dbFile.write(number + "\n")

        # Ask the user for the name of the new contact
        name = input("Enter a name: ")

    # Say "Goodbye!"
    print("Goodbye!")

    # Close the database file
    dbFile.close()


def DBquery():
    """ Retrieve contact data from the database """

    # Keep trying until we successfully read 
    # an existing database file
    while True:
        try:
            # Ask the user for the file name of the database
            # Complete this
            fileName = input("Enter the name of the file to read: ")

            # Try reading the file with the given name
            # Complete this
            dbFile = open(fileName, "r")

        except IOError: # If the file does not exist
            print("There is no file by that name. Try again...")
        else: # No problem opening the file
            # Read all the lines from the file
            # Complete this
            dbList = dbFile.readlines()

            # Close the file
            # Complete this
            dbFile.close()
            break

    # Create the phone book, an empty dictionary
    phoneBook = {}

    # Remove all the '\n' from the data loaded from the file
    # Complete this
    for i in range(len(dbList)):
        dbList[i] = dbList[i][:len(dbList[i])-1]

    # Now we will use a for loop to go through all the lines
    # of the data loaded from the file (already done above),
    # two lines at once. The first line is the contact name
    # and the second line is the phone number.
    # Complete this inside the for loop:
    for i in range(len(dbList)//2):
        # Add new contact into the dictionary
        # Complete this
        phoneBook[dbList[i * 2]] = dbList[i * 2 +1]

    # Ask the user for the name to be searched for
    # Complete this
    name = input("Enter a name: ")

    # Now we will use a while loop to repeatedly ask for names
    # to be searched for.
    # The while loop ends when the entered name is "done".
    # Complete this inside the while loop:
    while name != "done":
        # 1. Check if the contact name can be found in 
        #    the phone book
        #    1.1. If yes, then show the phone number
        #    1.2. If no, then show an error message
        # Complete this
        try:
            print(phoneBook[name])
        except KeyError:
            print("Sorry, there is no number for that name.")

        # 2. Ask the user for the name to be searched for
        name = input("Enter a name: ")

    # Say "Goodbye!"
    print("Goodbye!")
