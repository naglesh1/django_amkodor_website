def new_get_queryset(list_obj, N):
    obj_list = []
    minilist = []
    n, m = 0, 0

    for i in list_obj:
        n += 1
        m += 1
        minilist += [i]
        if n == N:
            obj_list.append(minilist)
            minilist = []
            n = 0
        elif m == len(list_obj):
            obj_list.append(minilist)

    return obj_list

