def the_list(a,b,c):
    the_list = [a,b,c]
    counter = 0
    for ix in range(len(the_list)):
        print(the_list[ix], end=' ')
        the_list[ix] = counter
        counter +=1
    for ix in range(len(the_list)):
        print(the_list[ix], end=" ")
   
def list_try(a,b,c):
    empty_list = []
    three_elements = [a,b,c]
    print(three_elements[-1])
    print(empty_list)

angle = 1
"""for i in range(5):
    if i % 2 ==1:
        angle+=1
else:
    angle-=1
"""

the_list = [x for x in range(1,5)]
print(the_list)