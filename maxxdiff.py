def new_index(maxx,minn,my_list):
    my_list.pop(minn)
    num=min(my_list)
    minn=my_list.index(num)

    if maxx>minn:
        return my_list[maxx] - my_list[minn]
    elif mann<minn and my_list:
        return new_index(maxx,minn,my_list)
    else:
        return "bad luck"

def maxxdiff(my_list):
    max_num=max(my_list)
    maxx=my_list.index(max_num)

    min_num=min(my_list)
    minn=my_list.index(min_num)

    if maxx>minn:
        print (my_list[maxx]-my_list[minn])
    else:
        sol=new_index(maxx,minn,my_list)
        print (sol)

my_list=[9,5,6,8,10]
print (maxxdiff(my_list))
