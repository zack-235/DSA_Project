def selection_sort(list):

    for i in range(len(list)):

        min=i

        for j in range(i+1,len(list)):

            if list[min]>list[j]:
                min=j

        list[i],list[min]=list[min],list[i]

    return list

    
            

arr=[2,8,6,4,1,3]
print(selection_sort(arr))





