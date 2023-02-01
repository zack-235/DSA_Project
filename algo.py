
def selection_sort(list1, render):
    list2 = list1
    for i in range(len(list2)):

        min=i

        for j in range(i+1,len(list2)):

            if list2[min]>list2[j]:
                min=j

        list2[i],list2[min]=list2[min],list2[i]
        render(list2)

    return list2

def quick_sort(list1):
    if len(list1) <= 1:
        return list1

    pivot = list1[len(list1) // 2]
    middle=list()
    left=list()
    right=list()

    for i in range(len(list1)):
        if list1[i]<pivot:
            left.append(list1[i])

        if list1[i]>pivot:
            right.append(list1[i])
            

        if list1[i]==pivot:
            middle.append(list1[i])
            

    return quick_sort(left)+middle+quick_sort(right)

def insertion_sort(list1):

    for i in range(1, len(list1)):

        j = i

        while j>0 and list1[j-1] > list1[j]:
            list1[j], list1[j-1] = list1[j-1], list1[j]
            j -= 1

    return list1

def bubble_sort(list1):
    #todo
    return list1

def linear_search(key, list1):
    index=0
    for i in range(0,len(list1)):
        if list1[i]==key:
            index=i
            break

    return index

def binary_search(key, list1):
    index=0
    start=0;
    end=len(list1)-1
    

    while start<end:
        mid=(start+end)//2
        if list1[mid]<key:
            start=mid+1

        elif list1[mid]>key:
            end=mid-1

        elif list1[mid]==key:
            index=mid;
            break;

    return index


if __name__ == '__main__':
    arr=[2,8,6,4,1,3]
    print('selection_sort',selection_sort(arr))
    print('insertion_sort',insertion_sort(arr))
    print('quick sort',quick_sort(arr))
    print('linear search, key index:',linear_search(6,arr))
    print('binary search, key index:',binary_search(6,quick_sort(arr)))