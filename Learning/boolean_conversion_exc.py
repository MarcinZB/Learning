choices = ['load data','export data','analyze & predict']

choices_dict = {
    int(1): choices[0],
    int(2): choices[1],
    int(3): choices[2]
}
try:
    while choices_dict:
        choice = int(input(f"1 - load data \n2 - export data \n3 - analyze & predict \nSelect option above or press enter: "))
        if choice:
            if choice in range(0,4):
                print(f"You've choosen: {choices_dict[choice]}, with number {choice}")
                break
            else:
                print("Please use numbers in range 1-3")
            continue
        else:
            print("Select number") 
        continue
except ValueError:
    print("It has to be an int type")


