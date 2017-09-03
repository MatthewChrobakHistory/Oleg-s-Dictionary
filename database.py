import os.path

# The location of the data file.
filepath = "data.txt"
# The dictionary containing our keys and values.
dict = { }

# File buffer containing data.
buffer = []


# Check if the data file exists.
if (os.path.isfile(filepath)):
    fs = open(filepath, 'r')
    buffer = list(fs.read().splitlines())
    fs.close()

# Update our dictionary.
for line in buffer:
    key = line[:line.rindex(' ')]
    val = line[line.rindex(' ') + 1:]

    dict.update({key:val})


# Loop forever
while (True):
    # Ask the user for input.
    cmd = raw_input("What would you like to do?")

    # Help menu
    if (cmd.startswith("help")):
        print("\nCommands:")
        print("\t[add <key> <value>]")
        print("\t\tAdds the value specified to the current value associated to the key in the database.")
        print("\t\tThe key will be added to the database if it does not exist yet.")
        print("\t[status]")
        print("\t\tDisplays the contents of the entire database.")
        print("\t[display <key>]")
        print("\t\tDisplays the current value associated to the key in the database.")
        print("\t[save]")
        print("\t\tSaves data in the database.")
        print("\t[exit]")
        print("\t\tSaves data in the database, and then exits the application.")

    # Are we adding a value?
    if (cmd.startswith("add")):
        # Get the key and value.
        body = cmd[4:]
        key = body[:body.rindex(' ')]
        val = body[body.rindex(' ') + 1:]

        # Make sure the key and value exist.
        if (not len(str(key)) == 0):
            if (not len(str(val)) == 0):

                # Add the key to the dictionary if it does not already exist.
                if (not dict.has_key(key)):
                    dict.update({ key: 0})

                # Add the desired value to the dictionary key.
                dict[key] = dict[key] + int(val)

                # Display the current value.
                print(key + " has the value of " + str(dict[key]))

    # Display all values in the dictionary.
    if (cmd.startswith("status")):
        for key in dict.keys():
            print(key + ": " + str(dict[key]))

    # Display an individual dictionary entry value.
    if (cmd.startswith("display")):
        # Get the key value, and make sure it's not empty.
        key = cmd[8:]
        if (not len(key) == 0):

            # Add the key to the dictionary if it does not exist already.
            if (not dict.has_key(key)):
                dict.update({ key: 0})

            # Display the status of the current key.
            print(key + " has the value of " + str(dict[key]))

    # Do we wish to save data?
    if (cmd.startswith("exit") or cmd.startswith("save")):

        # Delete the previous file if it exists.
        if (os.path.isfile(filepath)):
            os.remove(filepath)

        # Open the data file for writing.
        fs = open(filepath, 'w')

        # Append dictionary values to the filestream.
        for key in dict.keys():
            fs.write(key + " " + str(dict[key]) + "\n")

        # Close the filestream and exit.
        fs.close()
        
        print("Data saved!")
		
	# Break out of the loop if we wish to exit.
        if (cmd.startswith("exit")):
            break
        
print("Goodbye")
