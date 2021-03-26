    index = 0
    for toTop in toTopIns:
        if (index % 2 == 0):
            print('name::',toTop.text)
        else:
            print('comment',toTop.text)
        index = index + 1