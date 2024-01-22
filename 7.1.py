def santa_users(x):
    dict={}
    for user_info in x:
        if len(user_info) == 2:
            dict[user_info[0]] = user_info[1]
        else:
            dict[user_info[0]] = None
    return dict

if __name__ == '__main__':
    user_list = [["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]
    print(santa_users(user_list))
