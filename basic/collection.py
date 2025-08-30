from datetime import datetime

if __name__ == "__main__":
    list = [1, 3, True, 6.5, "jack"]
    print(list)

    print(list[0] is 1)
    print(list[4] == "jack")

    print(list + list == list * 2)

    print(1 in list)
    print(6.5 in list)

    print(list[1:3][1] in list)

    newlist = [list] * 3
    print(newlist)

    list[1] = 10
    print(newlist)
    print(newlist[0][1] is newlist[1][1] is newlist[2][1] is 10)

    newlist[0][1] = 20
    print(newlist)
    print(newlist[0][1] is newlist[1][1] is newlist[2][1] is 20)
    print(newlist[0][1] == newlist[1][1] == newlist[2][1] == 20)

    list.append(33)
    print(list)
    print(list[len(list) - 1] == 33)

    dt = datetime(year = 2025, month = 8, day = 28)
    list.insert(1, dt)
    print(list)
    print(type(list[1]) is datetime)

    print(list.pop() == 33)
    print(list.pop(1) == dt)

    list = [10, 2, 11, 43, 8, 6]
    list.sort()
    print(list)
    list.reverse()
    print(list)

    list = [10, 9, 3, 2, 77, 35]
    list.reverse()
    print(list)

    del list[1]
    print(list)

    list.append(2)
    print(list.index(2) is 1)

    print(list.count(9) == 1)
    print(list.count(2) == 2)

    list.remove(2)
    print(list.count(2) == 1)

    list.remove(10)
    print(list.count(10) == 0)

    print((54).__add__(12) == 66)
