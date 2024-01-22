
def compare_lists(l1, l2):
    elements_in_1list_and_2list=set(l1) & set(l2)
    unique_in_list1=set(l1) - set(l2)
    unique_in_list2=set(l2) - set(l1)
    list1_minus_common=set(l1) - elements_in_1list_and_2list
    list2_minus_common= set(l2) - elements_in_1list_and_2list

    return len(elements_in_1list_and_2list), len(unique_in_list1)+len(unique_in_list2),len(list1_minus_common),len(list2_minus_common)



if __name__ == '__main__':
    list1, list2 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
    result = compare_lists(list1, list2)
    print(result[0],'элемента',{', '.join(map(str, sorted(set(list1) & set(list2))) )})
    print(result[1],'элементов',{', '.join(map(str, sorted(set(list1) ^ set(list2))) )})
    print(result[2],'элементов',{', '.join(map(str, sorted(list(set(list1) - set(list2)))) )})
    print(result[3],'элементов',{', '.join(map(str, sorted(list(set(list2) - set(list1)))) )})
