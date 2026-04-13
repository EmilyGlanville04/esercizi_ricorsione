def count_leaf_nodes(input_list):
    #terminale
    if len(input_list) == 0:
        return 0
    #non terminale
    else:
        counter = 0
        for element in input_list:
            #controllo se l'elemento sia una lista
            #se è una lista, contiamo i suoi elementi con una ricursione
            if type(element) == list:
                counter += count_leaf_nodes(element)
            else: #aggiungiamo 1
                counter +=1
        return counter


if __name__=="__main__":
    names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names)) #ci aspettiamo 10