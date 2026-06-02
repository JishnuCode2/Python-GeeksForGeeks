arr = [1,5,4,2,3,1];



def rotate_list_by_one(li):
    li_0 = li[0];
    li.remove(li_0);
    li.append(li_0);

    return li;

print(rotate_list_by_one(arr))