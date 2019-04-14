#File Handling
#write and read in files
file = open("Session15D.py","r")
print(type(file))
filecontents = file.read() #read() -> reads all the contents from file
print(type(filecontents))  #str
print(filecontents)

filecontents = file.read()
print("+++++++++")
print(filecontents) #Nothing to show
#Once a file is read, it will not to be re-read

"""
"""
