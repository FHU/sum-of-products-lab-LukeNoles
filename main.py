newlist=[]
list1 = input()
list2 = input()
def sum_of_products(list1, list2):
    for i in range(0, len(list1)):
        newlist.append(int(list1[i]) * int(list2[i]))
    print (sum(newlist))

if __name__ == '__main__':
    if len(list1) == len(list2):
        sum_of_products(list1, list2)
    else:
        print ("error")
