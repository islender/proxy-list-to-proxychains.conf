import os

filename = input("Please choose the input file name (must be in same directory as script. Please include the .txt)\n")
proxtype = input("What type of proxy file is this? (socks4, socks5, https)?\n")
outputfile = input("Name the output file (.txt not necessary)\n")

with open(filename, "r+") as file:
    line = file.readline()

    print(line)

    if os.path.exists("newproxies.txt"):
        os.remove("newproxies.txt")
    else:
        print("The file does not exist")

    while line:
        line = proxtype + " 	 " + line.replace(":", " ")

        with open(outputfile + '.txt', 'a') as out:
            out.write(line)
            print(line)

        line = file.readline()

print("-----------------------------------------")
print("FINISHED! Find new file in " + outputfile +".txt")
print("-----------------------------------------")
