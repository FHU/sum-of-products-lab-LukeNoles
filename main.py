def sum_of_products(list1, list2):
    for i in range(0, len(list1)):
        newlist.append(int(list1[i]) * int(list2[i]))12
    return sum(newlist)

if __name__ == '__main__':
    newlist=[]
    list1 = input()
    list2 = input() 
    if len(list1) == len(list2):
        
        print (sum_of_products(list1, list2))
    else:
        print ("error")
