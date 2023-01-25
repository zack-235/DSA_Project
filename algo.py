def selection_sort(list1):

    for i in range(len(list1)):

        min=i

        for j in range(i+1,len(list1)):

            if list1[min]>list1[j]:
                min=j

        list1[i],list1[min]=list1[min],list1[i]

    return list1

if __name__ == '__main__':
    arr=[2,8,6,4,1,3]
    print(selection_sort(arr))
