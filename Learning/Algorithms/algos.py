# Sortowanie bombelkowe

def bubble(list):

    numberofElements = len(list)-1

    for i in range(numberofElements):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
        print(i+1, list)

def bubble_final(list):
     
    numberofElements = len(list)-1
    for no_result in range(numberofElements, 0, -1):
        for i in range(no_result):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

#Sortowanie przez wstawienie

def InsertionSort(list):

    for i in range(1,len(list)):
        j = i-1
        element_next = list[i]
        while(list[j] > element_next) and (j>=0):
            list[j+1] = list[j]
            j = j-1
        list[j+1] = element_next
    return list


#Sortowanie przez scalenie 

def MergeSort(list):

    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        
        MergeSort(left)
        MergeSort(right)

        i = 0
        j = 0 

        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left [i]
                i+=1
        
            else:
                list[k] = right[j]
                
                j+=1
            k+=1

        while i < len(left):
            list[k] = left[i]
            i+=1
            k+=1

        while j<len(right):
            list[k] = right[j]
            j+=1
            k+=1

def ShellSort(list):
    distance = len(list)//2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i

            while j >= distance and list[j-distance] > temp:
                list[j] = list[j-distance]
                j = j - distance
            list[j] = temp
        
        distance = distance // 2
    return list

def SelectionSort(list):
    for fill_slot in range(len(list)-1, 0,-1):
        max_index = 0
        for location in range(1, fill_slot+1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_slot], list[max_index] = list[max_index], list[fill_slot]
    return list
myList = [70,15,25,19,34,44]
print(myList)
SelectionSort(myList)
print(myList)