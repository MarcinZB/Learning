start_str = input()
table = list(start_str)
num_of_iter = len(table)

if table[0] == 'a' and table[1] =='a':
    print("REJECTED")

for i in table:
    if i == num_of_iter:
        break
    if i == 'b':
        print("accept")
