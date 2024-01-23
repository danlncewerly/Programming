
def get_subset(elements):
    elements = list(set(elements)) #преобразуем список в множество, чтобы убрать повторяющееся элементы, затем обратно преоюразуем в список
    if not elements:
        return [set()] #если список пустой, то возвращает список с пустым множеством
    subsets = [[]] #создаем список с пустым подмножеством
    for i in elements:
        new_subset = [subset+[i] for subset in subsets] #создаем новое подмножество добавляя i
        subsets.extend(new_subset) #добавляем его в subsets
    return [set(subset) for subset in subsets]
if __name__ == '__main__':
    s1=[1,2,3,4]
    s2=['a','b','c','d','d']
    print('подмножества:',get_subset(s1)[1:])
    print('количество подмножеств:', len(get_subset(s1))-1)
    print('подмножества:',get_subset(s2)[1:])
    print('количество подмножеств:', len(get_subset(s2))-1)
