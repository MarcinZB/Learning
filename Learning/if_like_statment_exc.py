import os

path = r"D:\Zainteresowania\PYTHON\nauka\whatIsee.txt"


'''
if os.path.isfile(path):
    print("Exists")
    file = os.open(path, os.O_RDONLY)
    read = os.read(file, 50)
    splited = read.split()
    words_number = len(splited)
    print(words_number)

    
    
else:
    print("Creating ...")
    with open(path,"w") as f:
        f.write("I see fire inside the mountain")
    print("File has been created")
'''
result = os.path.isfile(path) and open(path,"w").write("I see fire inside the mountain")
print(result)

