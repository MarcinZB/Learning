list_of_errors = [100,101,102]
print(f"Variable list of errors: {list_of_errors}, {type(list_of_errors)}, {id(list_of_errors)}")
#sprawdzenie czy w liście błędów cokolwiek się znajduje
if list_of_errors:
    print(True)
else:
    print(False)
#sprawdzenie dzięki logice
if len(list_of_errors)>0:
    print(True)
else:
    print(False)