import os

path = r"D:\Zainteresowania\PYTHON\nauka\mydata.txt"

#os.remove(path) 
'''
if os.path.isfile(path):
    print("file %s exists" % path)
else:
    print('Creating a file %s'%path)
    open(path,'x').close()
    print("File %s created"%path)
'''
result = os.path.isfile(path) or open(path, "x").close() #tworzenie pliku jeśli nie istnieje ! jeżeli pierwszy element zwraca true przerywa 
print(result)
