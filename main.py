def sum_of_products(list1, list2):
    list1 =list1.split()
    list2 = list2.split()
    for i in range(0, len(list1)):
        newlist.append(int(list1[i]) * int(list2[i]))
    return sum(newlist)

if __name__ == '__main__':
    newlist=[]
    list1 = input()
    list2 = input() 
    if len(list1) == len(list2):
        
        print (sum_of_products(list1, list2))
    else:
        print ("error")
